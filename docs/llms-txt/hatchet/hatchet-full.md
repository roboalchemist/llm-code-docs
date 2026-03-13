# Hatchet Documentation

> Hatchet is a distributed task queue and workflow engine for modern applications. It provides durable execution, concurrency control, rate limiting, and observability for background tasks and workflows in Python, TypeScript, and Go.

---

<!-- Source: https://docs.hatchet.run/v1/index -->

---
asIndexPage: true
---

import { Callout } from "nextra/components";
import LanguageSwitcher from "@/components/LanguageSwitcher";

# What is Hatchet?

Hatchet is a modern orchestration platform that helps engineering teams build low-latency and high-throughput data ingestion and agentic AI pipelines.

You write functions in Python, Typescript, Go, or Ruby and let Hatchet handle scheduling, retries, fault tolerance, and observability.


The core mental model has three parts:

- **[Tasks](/v1/tasks)** — the fundamental unit of work. A task wraps a single function and gives Hatchet everything it needs to schedule, execute, and observe it.
- **[Workers](/v1/workers)** — long-running processes in your infrastructure that pick up and execute tasks.
- **[Durable Workflows](/v1/durable-workflows)** — compose multiple tasks into durable pipelines with dependencies, retries, and checkpointing.

All tasks and workflows are **defined as code**, making them easy to version, test, and deploy.

## Use cases

While Hatchet is a general-purpose orchestration platform, it's particularly well-suited for:

- **Real-time data processing** — data ingestion for keeping LLM contexts up-to-date, ETL pipelines that require fast execution and high throughput.
- **AI agents** — features like [webhooks](/v1/webhooks), [child spawning](/v1/child-spawning), and dynamic workflows are designed to support agentic patterns.
- **Event-driven systems** — Hatchet's [eventing features](/v1/external-events/run-on-event) let you build event-driven architectures without additional infrastructure.

## Why Hatchet?

⚡️ **Low-Latency For Real-Time Workloads** - Sub-25ms task dispatch for hot workers with thousands of concurrent tasks. Smart assignment rules handle [rate-limits](/v1/rate-limits), [fairness](/v1/concurrency), and [priorities](/v1/priority) without complex configuration.

🪨 **Durability for Long Running Jobs** - Every task invocation is durably logged to PostgreSQL. With [durable execution](/v1/patterns/durable-task-execution), when jobs fail your workflow will resume exactly where you left off — no lost work, no duplicate LLM calls, no engineer headaches.

🧘‍♂️ **Zen Developer Experience** - Hatchet SDKs (Python, Typescript, and Go) are built with modern tooling and are designed to be easy to use. Hatchet has built-in observability and debugging tools for things like replays, logs, and alerts.

If you plan on self-hosting or have requirements for an on-premise deployment, there are some additional considerations:

🐘 **Minimal Infra Dependencies** - Hatchet is built on top of PostgreSQL and for simple workloads, [its all you need](/self-hosting/hatchet-lite).

⬆️ **Fully Featured Open Source** - Hatchet is 100% MIT licensed, so you can run the same application code against [Hatchet Cloud](https://cloud.onhatchet.run) to get started quickly or [self-host](/self-hosting) when you need more control.

## Hatchet vs. Alternatives

Today, developers who need background task processing and workflow orchestration face two main options:

1. Adopt external services like Temporal or Airflow, which are powerful but complex to run or introduce latency, or
2. Use simple task queue libraries like Celery or BullMQ, which lack critical workflow features and become difficult to debug at scale.

| Feature                                     | Hatchet | Celery     | Airflow    | Temporal     |
| ------------------------------------------- | ------- | ---------- | ---------- | ------------ |
| **Task Start Latency**                      | 25ms    | 5-100ms+   | 5-30s      | 25ms         |
| **Concurrent Tasks**                        | 1000s   | Variable\* | Variable\* | 10000        |
| **Code-First Workflows**                    | ✅      | ✅         | ✅         | ✅           |
| **Cron Jobs and Scheduling**                | ✅      | ✅         | ✅         | ✅           |
| **Priority Queues**                         | ✅      | ✅         | ✅         | ✅ (beta)    |
| **Durable Sleep/Checkpoints**               | ✅      | ❌         | ❌         | ✅           |
| **Sticky Assignment/Complex Routing Logic** | ✅      | ❌         | ❌         | ✅ (limited) |
| **Event-Based Triggering**                  | ✅      | ❌         | ✅         | ❌           |
| **Real-time Streaming**                     | ✅      | ❌         | ❌         | ❌           |
| **Global Rate Limits**                      | ✅      | ❌         | ❌         | ❌           |
| **Event Streaming**                         | ✅      | ❌         | ❌         | ❌           |

\*Requires careful configuration and infrastructure scaling

## Production Readiness

Hatchet has been battle-tested in production environments, processing billions of tasks per month for scale-ups and enterprises across various industries. Our open source offering is deployed over 10k times per month, while Hatchet Cloud supports hundreds of companies running at scale.

> "With Hatchet, we've scaled our indexing workflows effortlessly, reducing failed runs by 50% and doubling our user base in just two weeks!"
> — Soohoon, Co-Founder @ Greptile

> "Hatchet enables Aevy to process up to 50,000 documents in under an hour through optimized parallel execution, compared to nearly a week with our previous setup."
> — Ymir, CTO @ Aevy

## Ready to dive deeper?

Check out the **[Architecture & Guarantees](/v1/architecture-and-guarantees)** page to learn how Hatchet is built, its guarantees, and when to use it.

Or get started with the **[Hatchet Cloud Quickstart](/v1/quickstart)** or **[self-hosting](/self-hosting)**.


---

<!-- Source: https://docs.hatchet.run/v1/quickstart -->

---
asIndexPage: true
---

import { snippets } from "@/lib/generated/snippets";
import { Snippet } from "@/components/code";
import { Callout, Card, Cards, Steps, Tabs } from "nextra/components";
import UniversalTabs from "../../components/UniversalTabs";

# Hatchet Cloud Quickstart

By the end of this guide you'll have a worker running locally that executes a simple task triggered from the CLI.

> **Info:** This guide walks you through getting set up on Hatchet Cloud. If you'd like to
>   self-host Hatchet, please see the [self-hosted quickstart](/self-hosting)
>   instead.


### Sign up

If you haven't already signed up for Hatchet Cloud, please register [here](https://cloud.onhatchet.run).

### Set up your tenant

In Hatchet Cloud, you'll be shown a screen to create your first tenant. A tenant is a logical separation of your environments (e.g. `dev`, `staging`, `production`). Each tenant has its own set of users who can access it.

After creating the tenant, you can simply follow the instructions in the Hatchet Cloud dashboard to set up your first quickstart project and workflow. We have copied the instructions in the following steps.

### Install the Hatchet CLI

#### Native Install (Recommended)

**MacOS, Linux, WSL**

```sh
    curl -fsSL https://install.hatchet.run/install.sh | bash
```

#### Homebrew

**MacOS**

```sh
    brew install hatchet-dev/hatchet/hatchet --cask
```

### Set your Hatchet profile

You will need to create a Hatchet CLI profile to connect to your Hatchet Cloud tenant. You can do this using the `hatchet profile add` command:

```sh
hatchet profile add
```

Note that the Hatchet Cloud dashboard will provide you with an API token to use when creating your profile.

### Run the quickstart

You can run the Hatchet Cloud quickstart using the `hatchet quickstart` command:

```sh
hatchet quickstart
```

### Run your worker

After setting up the quickstart project, you can run your worker locally by following the instructions printed after the quickstart command. This will involve using the `hatchet worker dev` command:

```sh
hatchet worker dev
```

### Trigger a workflow

Finally, you can trigger your workflow using the `hatchet trigger simple` command:

```sh
hatchet trigger simple
```

### (Optional) Install Hatchet docs MCP and Agent Skills

Get Hatchet documentation directly in your AI coding assistant (Cursor, Claude Code, and more):

```sh copy
hatchet docs install
```

Get agent skills for common CLI operations:

```sh copy
hatchet skills install
```

See the [full setup guide](/v1/using-coding-agents) for manual configuration options.


And that's it! You should now have a Hatchet project set up on Hatchet Cloud with a worker running locally.

## Next Steps

Once you've completed the quickstart, continue to the next section to learn how to [create your first task](/v1/tasks).


---

<!-- Source: https://docs.hatchet.run/v1/using-coding-agents -->

McpUrl,
  CursorDeeplinkButton,
  CursorMcpConfig,
  ClaudeCodeCommand,
  CursorTabLabel,
  ClaudeCodeTabLabel,
  OtherAgentsTabLabel,
} from "@/components/McpSetup";

# Using Coding Agents

Hatchet is designed to work well with AI coding agents. This page covers how to give your agent access to Hatchet documentation and step-by-step skills for common CLI operations.

> **Info:** **Prerequisite:** The `hatchet skills install` and `hatchet docs install`
>   commands require the Hatchet CLI. See the [CLI reference](/cli) for
>   installation instructions.

## Agent Skills

Agent skills are reference documents that teach AI coding agents how to use the Hatchet CLI — triggering workflows, starting workers, debugging runs, and more.

Run the following command in your project root to install the skill package:

```bash copy
hatchet skills install
```

This creates a `skills/hatchet-cli/` directory with step-by-step reference files and appends a section to your project's `AGENTS.md` (and `CLAUDE.md`) pointing agents to the right file for each task.

**Install to a custom directory:**

```bash copy
hatchet skills install --dir ./my-project
```

After installation, commit the `skills/` directory and `AGENTS.md` to version control so all agents working in the repo benefit automatically.

### Available references

| Reference                         | When to use                                           |
| --------------------------------- | ----------------------------------------------------- |
| `references/setup-cli.md`         | Installing the CLI, creating or listing profiles      |
| `references/start-worker.md`      | Starting a dev worker for local development           |
| `references/trigger-and-watch.md` | Triggering a workflow and polling for completion      |
| `references/debug-run.md`         | Diagnosing a failed, stuck, or unexpected run         |
| `references/replay-run.md`        | Re-running a previous workflow with same or new input |

## MCP Server

Hatchet documentation is available as an **MCP (Model Context Protocol) server**, so AI coding assistants like Cursor and Claude Code can search and reference Hatchet docs directly.

MCP endpoint: 


  
  

    #### Hatchet CLI

```bash copy
        hatchet docs install claude-code
```

If `claude` is on your PATH, this runs the command automatically. Otherwise it prints it for you to copy.

#### Command

Run this command in your terminal:


  
  

    For any AI tool that supports [llms.txt](https://llmstxt.org/), Hatchet docs are available at:

    | Resource | URL |
    |----------|-----|
    | **llms.txt** (index) | [docs.hatchet.run/llms.txt](https://docs.hatchet.run/llms.txt) |
    | **llms-full.txt** (all docs) | [docs.hatchet.run/llms-full.txt](https://docs.hatchet.run/llms-full.txt) |
    | **Per-page markdown** | `docs.hatchet.run/llms/{section}/{page}.md` |
    | **MCP endpoint** |  |

    Every documentation page also includes a `<link rel="alternate" type="text/markdown">` header
    pointing to its markdown version, and a "View as Markdown" link at the top of the page.

  


## llms.txt

For any AI tool that supports [llms.txt](https://llmstxt.org/), Hatchet docs are available at:

| Resource                     | URL                                                                      |
| ---------------------------- | ------------------------------------------------------------------------ |
| **llms.txt** (index)         | [docs.hatchet.run/llms.txt](https://docs.hatchet.run/llms.txt)           |
| **llms-full.txt** (all docs) | [docs.hatchet.run/llms-full.txt](https://docs.hatchet.run/llms-full.txt) |
| **Per-page markdown**        | `docs.hatchet.run/llms/{section}/{page}.md`                              |
| **MCP endpoint**             |                                                                |

Every documentation page also includes a `<link rel="alternate" type="text/markdown">` header
pointing to its markdown version, and a "View as Markdown" link at the top of the page.


---

<!-- Source: https://docs.hatchet.run/v1/tasks -->

# Tasks

Everything you run in Hatchet is a **task** - a named function that you can trigger, retry, schedule, and observe. Tasks can be configured to handle the problems that come up in real systems: transient failures, resource contention, overloaded downstream services, and more.

## Defining a task

At minimum, a task needs a name and a function. The returned object is a **runnable** - you'll use it directly to [trigger](/v1/running-your-task) the task.

#### Python

```python
class SimpleInput(BaseModel):
    message: str


class SimpleOutput(BaseModel):
    transformed_message: str


# Declare the task to run
@hatchet.task(name="first-task", input_validator=SimpleInput)
def first_task(input: SimpleInput, ctx: Context) -> SimpleOutput:
    print("first-task task called")

    return SimpleOutput(transformed_message=input.message.lower())
```

#### Typescript

```typescript
import { hatchet } from '../hatchet-client';

// (optional) Define the input type for the workflow
export type SimpleInput = {
  Message: string;
};

export const simple = hatchet.task({
  name: 'simple',
  retries: 3,
  fn: async (input: SimpleInput) => {
    return {
      TransformedMessage: input.Message.toLowerCase(),
    };
  },
});
```

#### Go

```go
type SimpleInput struct {
	Message string `json:"message"`
}

type SimpleOutput struct {
	Result string `json:"result"`
}

task := client.NewStandaloneTask("process-message", func(ctx hatchet.Context, input SimpleInput) (SimpleOutput, error) {
	return SimpleOutput{
		Result: "Processed: " + input.Message,
	}, nil
})
```

#### Ruby

```ruby
FIRST_TASK = HATCHET.task(name: "first-task") do |input, ctx|
  puts "first-task called"
  { "transformed_message" => input["message"].downcase }
end
```

When you define a task, you are telling Hatchet: "here is a piece of work that a worker can pick up." The task carries a name, the function to run, and optional configuration. Tasks are registered on [workers](/v1/workers), which are the long-running processes that actually execute them.

## Task lifecycle

When you trigger a task, it moves through three phases: queued, running, and a terminal state.

```mermaid
graph LR
    Triggered --> QUEUED
    QUEUED -->|Assigned to worker| RUNNING
    RUNNING -->|Success| COMPLETED
    RUNNING -->|Failure + retries left| QUEUED
    RUNNING -->|Failure + no retries| FAILED
```

A task can also be **CANCELLED** at any point - either explicitly or by a [timeout](/v1/timeouts) expiring.

## Triggering a task

The runnable returned by a task definition supports several trigger methods:

| Method                                               | What it does                                            |
| ---------------------------------------------------- | ------------------------------------------------------- |
| [Run](/v1/running-your-task#run-and-wait)            | Trigger the task and wait for the result.               |
| [Run no wait](/v1/running-your-task#fire-and-forget) | Enqueue the task and return immediately.                |
| [Schedule](/v1/scheduled-runs)                       | Schedule the task to run at a specific time.            |
| [Cron](/v1/cron-runs)                                | Run the task on a recurring schedule.                   |
| [Bulk run](/v1/bulk-run)                             | Trigger many instances of the task at once.             |
| [On event](/v1/external-events/run-on-event)         | Trigger the task automatically when an event is pushed. |
| [Webhook](/v1/webhooks)                              | Trigger the task from an external HTTP request.         |

## Configuring a task

Tasks can be configured to handle common problems in distributed systems. For example, you might want to automatically retry a task when an external API returns a transient error, or limit how many instances of a task run at the same time to avoid overwhelming a downstream service.

| Concept                                                    | What it does                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- |
| [Retries](/v1/retry-policies)                              | Retry the task on failure, with optional backoff.          |
| [Timeouts](/v1/timeouts)                                   | Limit how long a task may wait to be scheduled or to run.  |
| [Concurrency](/v1/concurrency)                             | Limit how many runs of this task execute at once.          |
| [Rate limits](/v1/rate-limits)                             | Throttle task execution over a time window.                |
| [Priority](/v1/priority)                                   | Influence scheduling order relative to other queued tasks. |
| [Worker affinity](/v1/advanced-assignment/worker-affinity) | Prefer or require specific workers for this task.          |

## Input and output

Every task receives an **input** - a JSON-serializable object passed when the task is triggered. The value you return from the task function becomes the task's **output**, which callers receive when they await the result.

When a task is part of a [workflow](/v1/durable-workflows), its output is also available to downstream tasks through the context object, so data flows naturally from one step to the next. See [Accessing Parent Task Outputs](/v1/patterns/directed-acyclic-graphs#accessing-parent-task-outputs) for details.

## The context object

Every task function receives a **context** alongside its input. The context is your handle to the Hatchet runtime while the task is executing. Through it you can perform various operations:

- **Runtime information** like the task's run ID, workflow ID, and more.
- **Check for cancellation** and respond to it gracefully ([Cancellation](/v1/cancellation)).
- **Refresh timeouts** if a long-running operation needs more time ([Timeouts](/v1/timeouts)).
- **Release a worker slot** early to free capacity for other tasks ([Manual Slot Release](/v1/advanced-assignment/manual-slot-release)).

## How tasks execute on workers

Tasks don't run on their own - they are assigned to and executed by [workers](/v1/workers). A worker is a long-running process in your infrastructure that registers one or more tasks with Hatchet. When a task is triggered, Hatchet places it in a queue and assigns it to an available worker that has registered that task.

Each worker has a fixed number of **slots** that determine how many tasks it can run concurrently. When all slots are occupied, new tasks stay queued until a slot opens up. You can control this behavior further with [concurrency limits](/v1/concurrency), [rate limits](/v1/rate-limits), and [priority](/v1/priority).

If you need tasks to run on specific workers - for example, because a worker has a GPU or a particular model loaded in memory - you can use [worker affinity](/v1/advanced-assignment/worker-affinity) or [sticky assignment](/v1/advanced-assignment/sticky-assignment) to influence where tasks are placed.

## Tasks vs. workflows

A task on its own is a standalone runnable - you can trigger it, wait for its result, schedule it, or fire it off without waiting. When you need to coordinate multiple tasks together (run B after A, fan out across N inputs, etc.), you compose them into a [workflow](/v1/durable-workflows-overview). Both share the same trigger interface - the difference is scope. A task does one thing; a workflow orchestrates many things.

Next, read about how tasks compose into [workflows](/v1/durable-workflows-overview).


---

<!-- Source: https://docs.hatchet.run/v1/workers -->

# Workers

Workers are the processes that actually execute your [tasks](/v1/tasks). Each worker is a long-running process in your infrastructure that maintains a persistent gRPC connection to the Hatchet engine. Workers receive task assignments, run your code, and report results back. You can run them locally during development, in containers, or on VMs - and scale them independently from the rest of your stack.

## Declaring a worker

A worker needs a name and a set of tasks to handle. Call the `worker` method on the Hatchet client with both.

#### Python

```python
def main() -> None:
    worker = hatchet.worker("dag-worker", workflows=[dag_workflow])

    worker.start()
```

#### Typescript

```typescript
import { hatchet } from '../hatchet-client';
import { simple } from './workflow';
import { parent, child } from './workflow-with-child';
import { simpleWithZod } from './zod';

async function main() {
  const worker = await hatchet.worker('simple-worker', {
    // 👀 Declare the workflows that the worker can execute
    workflows: [simple, simpleWithZod, parent, child],
    // 👀 Declare the number of concurrent task runs the worker can accept
    slots: 100,
  });

  await worker.start();
}

if (require.main === module) {
  main();
}
```

#### Go

```go
worker, err := client.NewWorker("simple-worker", hatchet.WithWorkflows(task))
if err != nil {
	log.Fatalf("failed to create worker: %v", err)
}

interruptCtx, cancel := cmdutils.NewInterruptContext()
defer cancel()

err = worker.StartBlocking(interruptCtx)
if err != nil {
	log.Fatalf("failed to start worker: %v", err)
}
```

#### Ruby

```ruby
def main
  worker = HATCHET.worker("dag-worker", workflows: [DAG_WORKFLOW])
  worker.start
end
```

When a worker starts, it registers each of its tasks with the Hatchet engine. From that point on, Hatchet knows to route matching tasks to that worker. Multiple workers can register the same task - Hatchet distributes work across all of them.

## Starting a worker

#### CLI (recommended)

The fastest way to run a worker during development is with the Hatchet CLI. This handles authentication and hot-reloads your worker when code changes:

```bash
hatchet worker dev
```

#### Script

You can also run the worker script directly. This requires a `HATCHET_CLIENT_TOKEN` environment variable. You can generate an API token from the Hatchet dashboard by navigating to the **Settings** tab and clicking **API Tokens**. Click **Generate API Token** to create a new token, and do not share it publicly.

```bash
export HATCHET_CLIENT_TOKEN="<your-client-token>"
```

If you are a self-hosted user without TLS enabled, also set:

```bash
export HATCHET_CLIENT_TLS_STRATEGY=none
```

Then run your worker:

#### Python

```bash
python worker.py
```

#### Typescript

Add a script to your `package.json`:

```json
"scripts": {
  "start:worker": "ts-node src/worker.ts"
}
```

Then run it:

```bash
npm run start:worker
```

#### Go

```bash
go run main.go
```

#### Ruby

```bash
bundle exec ruby worker.rb
```

Once the worker starts, you will see logs confirming it is connected:

```
[INFO]  🪓 -- STARTING HATCHET...
[DEBUG] 🪓 -- 'test-worker' waiting for ['simpletask:step1']
[DEBUG] 🪓 -- acquired action listener: efc4aaf2-...
[DEBUG] 🪓 -- sending heartbeat
```

> **Info:** For self-hosted users, you may need to set additional gRPC configuration
>   options. See the [Self-Hosting](/self-hosting/worker-configuration-options)
>   docs for details.

## Worker lifecycle

A worker moves through four phases during its lifetime:

```mermaid
graph LR
    Created -->|Connects to engine| ACTIVE
    ACTIVE -->|Heartbeat timeout| INACTIVE
    ACTIVE -->|Graceful shutdown| STOPPED
    INACTIVE -->|Reconnects| ACTIVE
```

- **ACTIVE** - the worker is connected and accepting tasks.
- **INACTIVE** - the engine has not received a heartbeat within the expected window. Tasks assigned to this worker will be reassigned.
- **STOPPED** - the worker shut down gracefully. In-flight tasks are allowed to complete before the process exits.

Hatchet uses heartbeats to monitor worker health. Workers send a heartbeat every **4 seconds**. If the engine does not receive a heartbeat for **30 seconds**, the worker is marked INACTIVE and its in-flight tasks are re-queued for other workers to pick up.

Common reasons a worker misses heartbeats:

- **Process crash** - the worker process exits unexpectedly (OOM kill, unhandled exception, SIGKILL).
- **Network disruption** - the connection between the worker and the Hatchet engine is interrupted (DNS failure, firewall change, cloud network blip).
- **Blocked main thread** - a long-running synchronous computation (e.g. CPU-intensive work, a blocking FFI call) starves the heartbeat loop and prevents it from sending on time.

## Slots

Every worker has a fixed number of **slots** that control how many tasks it can run concurrently. You configure them with the `slots` option on the worker. If you set `slots=5`, the worker will run up to five tasks at the same time. Any additional tasks wait in the queue until a slot opens up.

Slots are a **local** limit - they protect the individual worker process from overcommitting its CPU, memory, or event loop. [Concurrency controls](/v1/concurrency) are a **global** limit across your entire fleet - use them to prevent a single tenant or use-case from monopolizing capacity, or to respect the limits of an external resource like a third-party API or database connection pool. The two work together: concurrency controls decide how many runs Hatchet will allow to be active; slots decide how many of those runs each individual worker is willing to accept.

### Choosing a slot count

Start with a slot count that matches the degree of parallelism your worker can sustain. For CPU-heavy tasks, that is typically the number of available cores. For I/O-heavy tasks (HTTP calls, database queries), you can safely go higher because most of the time is spent waiting.

> **Info:** Adding slots is only helpful up to the point where the worker is not
>   bottlenecked by another resource. If your worker is CPU-bound, memory-bound,
>   or waiting on network I/O, more slots will just increase contention. Monitor
>   memory usage and event loop lag after changing slot counts - if either climbs,
>   you have gone too far.

## Scaling workers

You can increase throughput in two ways: add more slots to a single worker, or run more worker processes. In most workloads, horizontal scaling (more workers) is the simplest path because each worker brings its own pool of slots and its own resources.

When running in Kubernetes or a similar orchestrator, you can autoscale workers based on queue depth using the [Task Stats API](/v1/autoscaling-workers). Hatchet also supports [KEDA integration](/v1/autoscaling-workers#autoscaling-with-keda) for event-driven autoscaling.

## Task assignment

By default, Hatchet distributes tasks to any available worker that has registered the task. You can influence this behavior in several ways:

| Concept                                                            | What it does                                                    |
| ------------------------------------------------------------------ | --------------------------------------------------------------- |
| [Worker Affinity](/v1/advanced-assignment/worker-affinity)         | Prefer or require specific workers based on labels and weights. |
| [Sticky Assignment](/v1/advanced-assignment/sticky-assignment)     | Pin related tasks in a workflow to the same worker.             |
| [Manual Slot Release](/v1/advanced-assignment/manual-slot-release) | Free a worker slot before the task function returns.            |

These are useful when a worker has specialized hardware (a GPU, a loaded ML model), or when co-locating related tasks on the same worker avoids redundant setup.

## Running in production

In development, the fastest way to run a worker is `hatchet worker dev`, which handles authentication and hot-reloads your code on changes. In production, you'll run workers as standalone processes or containers.

| Concept                                         | What it does                                                            |
| ----------------------------------------------- | ----------------------------------------------------------------------- |
| [Running with Docker](/v1/docker)               | Containerize workers for deployment.                                    |
| [Autoscaling Workers](/v1/autoscaling-workers)  | Scale workers dynamically based on queue depth.                         |
| [Worker Health Checks](/v1/worker-healthchecks) | Expose `/health` and `/metrics` endpoints for monitoring.               |
| [Preparing for Production](/v1/production)      | Operational best practices for monitoring, error handling, and scaling. |

## Workers and tasks

Workers and tasks have a many-to-many relationship. A single worker can register many tasks, and a single task can be registered on many workers. This means you can organize your workers by resource requirements, deployment boundary, or any other criterion - and Hatchet handles routing tasks to the right place.

If you haven't already, read about [tasks](/v1/tasks) to understand how work is defined and configured.


---

<!-- Source: https://docs.hatchet.run/v1/running-your-task -->

# Running Tasks

With your task defined and a worker running, you can import the task wherever you need it and invoke it.

## Run and wait

Call a task and block until you get the result back. Use this for synchronous workflows like fan-out, LLM calls, or any time you need the output before continuing.

#### Python

You can use your `Task` object to run a task and wait for it to complete by calling the `run` method. This method will block until the task completes and return the result.

```python
from examples.child.worker import SimpleInput, child_task

child_task.run(SimpleInput(message="Hello, World!"))
```

You can also `await` the result of `aio_run`:

```python
result = await child_task.aio_run(SimpleInput(message="Hello, World!"))
```

Note that the type of `input` here is a Pydantic model that matches the input schema of your workflow.

#### Typescript

You can use your `Task` object to run a task and wait for it to complete by calling the `run` method. This method will return a promise that resolves when the task completes and returns the result.

```typescript
const res = await parent.run(
  {
    Message: 'HeLlO WoRlD',
  },
  {
    additionalMetadata: {
      test: 'test',
    },
  }
);

// 👀 Access the results of the Task
console.log(res.TransformedMessage);
```

#### Go

You can use your `Task` object to run a task and wait for it to complete by calling the `Run` method. This method will block until the task completes and return the result.

```go
result, err := task.Run(context.Background(), SimpleInput{Message: "Hello, World!"})
if err != nil {
	return err
}
```

#### Ruby

```ruby
result = CHILD_TASK_WF.run({ "message" => "Hello, World!" })
```
```ruby
# In Ruby, run is synchronous
result = CHILD_TASK_WF.run({ "message" => "Hello, World!" })
```

### Spawning tasks from within a task

You can spawn tasks from within a task. This is useful for composing tasks together, fanning out batched tasks, or creating conditional workflows.

#### Python

You can run a task from within a task by calling the `aio_run` method on the task object from within a task function. This will associate the runs in the dashboard for easier debugging.

```python
@hatchet.task(name="SpawnTask")
async def spawn(input: EmptyModel, ctx: Context) -> dict[str, Any]:
    # Simply run the task with the input we received
    result = await child_task.aio_run(
        input=SimpleInput(message="Hello, World!"),
    )

    return {"results": result}
```

The parent task will run and spawn the child task, then collect the results.

#### Typescript

You can spawn a task from within a task by calling the `run` method on the task object from within a task function. This will associate the runs in the dashboard for easier debugging.

```typescript
const parentTask = hatchet.task({
  name: 'parent',
  fn: async (input, ctx) => {
    // Simply the task and it will be spawned from the parent task
    const child = await simple.run({
      Message: 'HeLlO WoRlD',
    });

    return {
      result: child.TransformedMessage,
    };
  },
});
```

#### Go

You can run a task from within a task by calling the `Run` method on the task object from within a task function. This will associate the runs in the dashboard for easier debugging.

```go
parent := workflow.NewTask("parent-task", func(ctx hatchet.Context, input SimpleInput) (*SimpleOutput, error) {
	// Run the child task
	_, err := task.Run(ctx, SimpleInput{Message: input.Message})
	if err != nil {
		return nil, err
	}

	return &SimpleOutput{
		Result: "Processed: " + input.Message,
	}, nil
})
```

#### Ruby

```ruby
SPAWN_TASK = hatchet.task(name: "SpawnTask") do |input, ctx|
  result = CHILD_TASK_WF.run({ "message" => "Hello, World!" })
  { "results" => result }
end
```

### Running tasks in parallel

#### Python

Since the `aio_run` method returns a coroutine, you can spawn multiple tasks in parallel and await using `asyncio.gather`.

```python
result1 = child_task.aio_run(SimpleInput(message="Hello, World!"))
result2 = child_task.aio_run(SimpleInput(message="Hello, Moon!"))

#  gather the results of the two tasks
results = await asyncio.gather(result1, result2)

#  print the results of the two tasks
print(results[0]["transformed_message"])
print(results[1]["transformed_message"])
```

#### Typescript

Since the `run` method returns a promise, you can spawn multiple tasks in parallel and await using `Promise.all`.

```typescript
const res1 = simple.run({
  Message: 'HeLlO WoRlD',
});

const res2 = simple.run({
  Message: 'Hello MoOn',
});

const results = await Promise.all([res1, res2]);

console.log(results[0].TransformedMessage);
console.log(results[1].TransformedMessage);
```

#### Go

You can run multiple tasks in parallel by calling `Run` multiple times in goroutines and using a `sync.WaitGroup` to wait for them to complete.

```go
var results []string
var resultsMutex sync.Mutex
var errs []error
var errsMutex sync.Mutex

wg := sync.WaitGroup{}
wg.Add(2)

go func() {
	defer wg.Done()
	result, err := task.Run(context.Background(), SimpleInput{
		Message: "Hello, World!",
	})

	if err != nil {
		errsMutex.Lock()
		errs = append(errs, err)
		errsMutex.Unlock()
		return
	}

	resultsMutex.Lock()

	var resultOutput SimpleOutput
	err = result.Into(&resultOutput)
	if err != nil {
		return
	}
	results = append(results, resultOutput.Result)
	resultsMutex.Unlock()
}()

go func() {
	defer wg.Done()
	result, err := task.Run(context.Background(), SimpleInput{
		Message: "Hello, Moon!",
	})

	if err != nil {
		errsMutex.Lock()
		errs = append(errs, err)
		errsMutex.Unlock()
		return
	}

	resultsMutex.Lock()

	var resultOutput SimpleOutput
	err = result.Into(&resultOutput)
	if err != nil {
		return
	}
	results = append(results, resultOutput.Result)
	resultsMutex.Unlock()
}()

wg.Wait()
```

#### Ruby

```ruby
results = CHILD_TASK_WF.run_many(
  [
    CHILD_TASK_WF.create_bulk_run_item(input: { "message" => "Hello, World!" }),
    CHILD_TASK_WF.create_bulk_run_item(input: { "message" => "Hello, Moon!" })
  ]
)
puts results
```

> **Info:** While you can run multiple tasks in parallel using the `Run` method, this is
>   not recommended for large numbers of tasks. Instead, use [bulk run
>   methods](/v1/bulk-run) for large parallel task execution.

## Fire and forget

Enqueue a task without waiting for the result. Use this for background jobs like sending emails, processing uploads, or kicking off long-running pipelines.

#### Python

```python
class HelloInput(BaseModel):
    name: str


class HelloOutput(BaseModel):
    greeting: str


@hatchet.task(input_validator=HelloInput)
async def say_hello(input: HelloInput, ctx: Context) -> HelloOutput:
    return HelloOutput(greeting=f"Hello, {input.name}!")
```

You can use your task object to enqueue a task by calling the `run_no_wait` method. This returns a `WorkflowRunRef` without waiting for the result.

```python
ref = say_hello.run_no_wait(input=HelloInput(name="World"))
```

You can also `await` the result of `aio_run_no_wait`:

```python
ref = await say_hello.aio_run_no_wait(input=HelloInput(name="Async World"))
```

Note that the type of `input` here is a Pydantic model that matches the input schema of your task.

#### Typescript

You can use your task object to enqueue a task by calling the `run_no_wait` method. This returns a `WorkflowRunRef` without waiting for the result.

```typescript
import { simple } from './workflow';
// ...

async function main() {
  // 👀 Enqueue the workflow
  const run = await simple.runNoWait({
    Message: 'hello',
  });

  // 👀 Get the run ID of the workflow
  const runId = await run.getWorkflowRunId();
  // It may be helpful to store the run ID of the workflow
  // in a database or other persistent storage for later use
  console.log(runId);
```

#### Go

You can use your task object to enqueue a task by calling the `RunNoWait` method. This returns a `WorkflowRunRef` without waiting for the result.

```go
runRef, err := task.RunNoWait(context.Background(), SimpleInput{Message: "Hello, World!"})
if err != nil {
	return err
}

fmt.Println(runRef.RunId)
```

#### Ruby

```ruby
SAY_HELLO = hatchet.task(name: "say_hello") do |input, ctx|
  { "greeting" => "Hello, #{input['name']}!" }
end
```
```ruby
ref = SAY_HELLO.run_no_wait({ "name" => "World" })
```
```ruby
# In Ruby, run_no_wait is the equivalent of async enqueuing
ref = SAY_HELLO.run_no_wait({ "name" => "World" })
```

### Subscribing to results later

The `run_no_wait` method returns a `WorkflowRunRef` which includes a listener for the result of the task, so you can subscribe at a later time.

#### Python

Use `ref.result()` to block until the result is available:

```python
result = ref.result()
```

or await `aio_result`:

```python
result = await ref.aio_result()
```

#### Typescript

```typescript
// the return object of the enqueue method is a WorkflowRunRef which includes a listener for the result of the workflow
const result = await run.output;
console.log(result);

// if you need to subscribe to the result of the workflow at a later time, you can use the runRef method and the stored runId
const ref = hatchet.runRef(runId);
const result2 = await ref.output;
console.log(result2);
```

#### Go

```go
result, err := runRef.Result()
if err != nil {
	return err
}

var resultOutput SimpleOutput
err = result.TaskOutput("process-message").Into(&resultOutput)
if err != nil {
	return err
}

fmt.Println(resultOutput.Result)
```

#### Ruby

```ruby
result = ref.result
```
```ruby
# In Ruby, result is synchronous - use poll for async-like behavior
result = ref.result
```

### Triggering from the dashboard

In the Hatchet Dashboard, navigate to "Task Runs" in the left sidebar and click "Trigger Run" at the top right. You can specify run parameters such as Input, Additional Metadata, and the Scheduled Time.

![Create Scheduled Run](../../public/schedule-dash.gif)

## Where you can trigger from

- **Same codebase or monorepo** - import your task and call `run`, `run_no_wait`, or other trigger methods directly. Your API server, CLI, or another service in the same repo can use the same task definition.
- **External API or separate service (polyrepo)** - when the triggering code can't import the task definition (different repo, language, or microservice), use a **stub**: a Hatchet task with the same name and input/output types but no implementation. See [Inter-Service Triggering](/v1/inter-service-triggering) for details.
- **From the CLI** - use the `hatchet run` command to trigger tasks from the command line.
- **From the Dashboard** - use the Hatchet dashboard to trigger tasks from the web interface.

## Other trigger styles

Hatchet supports additional trigger patterns for more advanced use cases:

| Style         | Use case                                             | Doc                                               |
| ------------- | ---------------------------------------------------- | ------------------------------------------------- |
| **Scheduled** | Run once at a specific time in the future            | [Scheduled Trigger](/v1/scheduled-runs)           |
| **Cron**      | Run on a recurring schedule (daily, weekly, etc.)    | [Cron Trigger](/v1/cron-runs)                     |
| **Events**    | Run when an event is emitted (e.g. webhooks, queues) | [Event Trigger](/v1/external-events/run-on-event) |
| **Bulk**      | Run the same task many times with different inputs   | [Bulk Run Many](/v1/bulk-run)                     |
| **Webhooks**  | Let external systems trigger workflows via HTTP      | [Webhooks](/v1/webhooks)                          |

## Next steps

Now that you can run tasks, explore [Durable Workflows](/v1/durable-workflows) to compose multiple tasks into pipelines with dependencies and checkpointing.


---

<!-- Source: https://docs.hatchet.run/v1/durable-workflows-overview -->

# Durable Workflows

A **durable workflow** is work whose execution state lives in Hatchet instead of in your process. When you run a durable workflow, the orchestrator owns that state: it records progress, survives your worker crashing or scaling down, and resumes from the last checkpoint so work is not lost or duplicated.

## Why durable?

With ordinary tasks, "where we are" in the workflow lives in memory. If the process dies, that state is gone. With durable workflows, execution state is stored in the Hatchet event log. The orchestrator can therefore:

- **Recover from failures** — replay from the last recorded step on another worker instead of restarting from scratch.
- **Handle long waits** — release the worker slot during "wait 24 hours" or "wait for this event" steps, then resume when the wait completes.
- **Manage distributed state** — keep multi-step, branching, or long-running flows consistent and replayable across workers and restarts.

Your code describes the steps; Hatchet makes them durable and resumable.

## Two patterns

Hatchet supports two patterns for building durable workflows, and you can [mix them](/v1/patterns/mixing-patterns) within the same application. Both are durable — the difference is how you express the work. The key difference is whether you know the **shape of work** ahead of time.


**Durable task execution** — The shape of work is **dynamic**. A single long-running function that can pause for time or external signals (`SleepFor`, `WaitForEvent`) and [spawn child tasks](/v1/child-spawning) at runtime. Use durable tasks when:

- The work is IO-bound — waiting for time to pass, external events, or human approval
- The number of subtasks is determined at runtime (dynamic fan-out)
- You need procedural control flow — loops, branches, or agent-style reasoning

**Directed acyclic graphs (DAGs)** — The shape of work is **known upfront**. You declare which tasks run, in what order, and what depends on what. Hatchet handles execution, parallelism, and retries within that fixed structure. Use DAGs when:

- You have a well-defined pipeline (ETL, multi-step data processing)
- Every task and dependency is known before the workflow starts
- You want the full graph visible in the dashboard for debugging and monitoring

## Choosing a pattern

DAGs are **easier to visualize and reason about** — every task, dependency, and data flow is visible as a graph. Durable tasks offer **more flexibility** — they can branch, loop, and spawn children dynamically — but their runtime behavior is harder to predict from the code alone. When in doubt, start with a DAG and reach for a durable task only when you need capabilities a static graph can't express. You can always [mix both patterns](/v1/patterns/mixing-patterns) in the same application.

## How workflows relate to tasks

A workflow is a **container of tasks**. Both standalone tasks and workflows are **runnables** — they share the same API (`run`, `run_no_wait`, `schedule`, and the other trigger methods all work identically).


  
    Checkpoints, durable context, and when to use it.
  
  
    Multi-task workflows with dependencies and parallel execution.
  
  
    Combine durable tasks and DAGs within the same workflow.


---

<!-- Source: https://docs.hatchet.run/v1/scheduled-runs -->

# Scheduled Runs

> This example assumes we have a [task](/v1/tasks) registered on a running [worker](/v1/workers).

Scheduled runs allow you to trigger a task at a specific time in the future. Some example use cases of scheduling runs might include:

- Sending a reminder email at a specific time after a user took an action.
- Running a one-time maintenance task at a predetermined time as determined by your application. For instance, you might want to run a database vacuum during a maintenance window any time a task matches a certain criteria.
- Allowing a customer to decide when they want your application to perform a specific task. For instance, if your application is a simple alarm app that sends a customer a notification at a time that they specify, you might create a scheduled run for each alarm that the customer sets.

Hatchet supports scheduled runs to run on a schedule defined in a few different ways:

- [Programmatically](/v1/scheduled-runs#programmatically-creating-scheduled-runs): Use the Hatchet SDKs to dynamically set the schedule of a task.
- [Hatchet Dashboard](/v1/scheduled-runs#managing-scheduled-runs-in-the-hatchet-dashboard): Manually create scheduled runs from the Hatchet Dashboard.

> **Warning:** The scheduled time is when Hatchet **enqueues** the task, not when the run
>   starts. Scheduling constraints like concurrency limits, rate limits, and retry
>   policies can affect run start times.

## Programmatically Creating Scheduled Runs

### Create a Scheduled Run

You can create dynamic scheduled runs programmatically via the API to run tasks at a specific time in the future.

Here's an example of creating a scheduled run to trigger a task tomorrow at noon:

#### Python

```python
from datetime import datetime

from examples.simple.worker import simple

schedule = simple.schedule(datetime(2025, 3, 14, 15, 9, 26))

## 👀 do something with the id
print(schedule.id)
```

#### Typescript

```typescript
const runAt = new Date(new Date().setHours(12, 0, 0, 0) + 24 * 60 * 60 * 1000);

const scheduled = await simple.schedule(runAt, {
  Message: 'hello',
});

// 👀 Get the scheduled run ID of the workflow
// it may be helpful to store the scheduled run ID of the workflow
// in a database or other persistent storage for later use
const scheduledRunId = scheduled.metadata.id;
console.log(scheduledRunId);
```

#### Go

```go
scheduledRun, err := client.Schedules().Create(
	context.Background(),
	"scheduled",
	features.CreateScheduledRunTrigger{
		TriggerAt: time.Now().Add(1 * time.Minute),
		Input:     map[string]interface{}{"message": "Hello, World!"},
	},
)
if err != nil {
	log.Fatalf("failed to create scheduled run: %v", err)
}
```

#### Ruby

```ruby
schedule = SIMPLE.schedule(Time.now + 86_400, input: { "message" => "Hello, World!" })

## do something with the id
puts schedule.metadata.id
```

In this example you can have different scheduled times for different customers, or dynamically set the scheduled time based on some other business logic.

When creating a scheduled run via the API, you will receive a scheduled run object with a metadata property containing the id of the scheduled run. This id can be used to reference the scheduled run when deleting the scheduled run and is often stored in a database or other persistence layer.

> **Info:** Note: Be mindful of the time zone of the scheduled run. Scheduled runs are
>   **always** stored and returned in UTC.

### Deleting a Scheduled Run

You can delete a scheduled run by calling the `delete` method on the scheduled client.

#### Python

```python
hatchet.scheduled.delete(scheduled_id=scheduled_run.metadata.id)
```

#### Typescript

```typescript
await hatchet.scheduled.delete(scheduled);
```

#### Go

```go
err = client.Schedules().Delete(
	context.Background(),
	scheduledRun.Metadata.Id,
)
if err != nil {
	log.Fatalf("failed to delete scheduled run: %v", err)
}
```

#### Ruby

```ruby
hatchet.scheduled.delete(scheduled_run.metadata.id)
```

### Listing Scheduled Runs

You can list all scheduled runs for a task by calling the `list` method on the scheduled client.

#### Python

```python
scheduled_runs = hatchet.scheduled.list()
```

#### Typescript

```typescript
const scheduledRuns = await hatchet.scheduled.list({
  workflow: simple,
});
console.log(scheduledRuns);
```

#### Go

```go
scheduledRuns, err := client.Schedules().List(
	context.Background(),
	rest.WorkflowScheduledListParams{},
)
if err != nil {
	log.Fatalf("failed to list scheduled runs: %v", err)
}
```

#### Ruby

```ruby
scheduled_runs = hatchet.scheduled.list
```

### Rescheduling a Scheduled Run

If you need to change the trigger time for an existing scheduled run, you can reschedule it by updating its `triggerAt`.

#### Python

```python
hatchet.scheduled.update(
    scheduled_id=scheduled_run.metadata.id,
    trigger_at=datetime.now(tz=timezone.utc) + timedelta(hours=1),
)
```

#### Typescript

```typescript
await hatchet.scheduled.update(scheduledRunId, {
  triggerAt: new Date(Date.now() + 60 * 60 * 1000),
});
```

#### Ruby

```ruby
hatchet.scheduled.update(
  scheduled_run.metadata.id,
  trigger_at: Time.now + 3600
)
```

> **Warning:** You can only reschedule scheduled runs created via the API (not runs created
>   via a code-defined schedule), and Hatchet may reject rescheduling if the run
>   has already triggered.

### Bulk operations (delete / reschedule)

Hatchet supports bulk operations for scheduled runs. You can bulk delete scheduled runs, and you can bulk reschedule scheduled runs by providing a list of updates.

#### Python

```python
hatchet.scheduled.bulk_delete(scheduled_ids=[id])

hatchet.scheduled.bulk_delete(
    workflow_id="workflow_id",
    statuses=[ScheduledRunStatus.SCHEDULED],
    additional_metadata={"customer_id": "customer-a"},
)
```
```python
hatchet.scheduled.bulk_update(
    [
        (id, datetime.now(tz=timezone.utc) + timedelta(hours=2)),
    ]
)
```

#### Typescript

```typescript
await hatchet.scheduled.bulkDelete({
  scheduledRuns: [scheduledRunId],
});
```
```typescript
await hatchet.scheduled.bulkUpdate([
  { scheduledRun: scheduledRunId, triggerAt: new Date(Date.now() + 2 * 60 * 60 * 1000) },
]);
```

#### Ruby

```ruby
hatchet.scheduled.bulk_delete(scheduled_ids: [id])
```
```ruby
hatchet.scheduled.bulk_update(
  [[id, Time.now + 7200]]
)
```

## Managing Scheduled Runs in the Hatchet Dashboard

In the Hatchet Dashboard, you can view and manage scheduled runs for your tasks.

Navigate to "Triggers" > "Scheduled Runs" in the left sidebar and click "Create Scheduled Run" at the top right.

You can specify run parameters such as Input, Additional Metadata, and the Scheduled Time.

![Create Scheduled Run](../../public/schedule-dash.gif)

You can also manage existing scheduled runs:

- **Single-run actions**: Use the per-row actions menu to **Reschedule** or **Delete** an individual scheduled run.
- **Bulk actions**: Use the **Actions** menu to bulk **Delete** or **Reschedule** either:
  - The selected rows, or
  - All rows matching the current filters (including “all” if no filters are set).

> **Info:** In the dashboard, reschedule/delete actions may be disabled for runs that were
>   created via a code-defined schedule, and rescheduling may be disabled for runs
>   that have already triggered.

## Scheduled Run Considerations

When using scheduled runs, there are a few considerations to keep in mind:

1. **Time Zone**: Scheduled runs are stored and returned in UTC. Make sure to consider the time zone when defining your scheduled time.

2. **Execution Time**: The actual execution time of a scheduled run may vary slightly from the scheduled time. Hatchet makes a best-effort attempt to enqueue the task as close to the scheduled time as possible, but there may be slight delays due to system load or other factors.

3. **Missed Schedules**: If a scheduled task is missed (e.g., due to system downtime), Hatchet will not automatically run the missed instances when the service comes back online.

4. **Overlapping Schedules**: If a task is still running when a second scheduled run is scheduled to start, Hatchet will start a new instance of the task or respect [concurrency](/v1/concurrency) policy.


---

<!-- Source: https://docs.hatchet.run/v1/cron-runs -->

# Recurring Runs with Cron

> This example assumes we have a [task](/v1/tasks) registered on a running [worker](/v1/workers).

A [Cron](https://en.wikipedia.org/wiki/Cron) is a time-based job scheduler that allows you to define when a task should be executed automatically on a pre-determined schedule.

Some example use cases for cron-style tasks might include:

1. Running a daily report at a specific time.
2. Sending weekly digest emails to users about their activity from the past week.
3. Running a monthly billing process to generate invoices for customers.

Hatchet supports cron triggers to run on a schedule defined in a few different ways:

- [Task Definitions](/v1/cron-runs#defining-a-cron-in-your-task-definition): Define a cron expression in your task definition to trigger the task on a predefined schedule.
- [Dynamic Programmatically](/v1/cron-runs#programmatically-creating-cron-triggers): Use the Hatchet SDKs to dynamically set the cron schedule of a task.
- [Hatchet Dashboard](/v1/cron-runs#managing-cron-jobs-in-the-hatchet-dashboard): Manually create cron triggers from the Hatchet Dashboard.

> **Warning:** The expression is when Hatchet **enqueues** the task, not when the run starts.
>   Scheduling constraints like concurrency limits, rate limits, and retry
>   policies can affect run start times.

### Cron Expression Syntax

Cron expressions in Hatchet follow the standard cron syntax. Hatchet supports both 5-field and 6-field expressions.
A cron expression consists 5 to 6 fields separated by spaces. If there are 6 fields, the first field is seconds; if
there are 5 fields, the first field is minutes.

```
┌───────────── second (0 - 59) (optional)
| ┌───────────── minute (0 - 59)
│ │ ┌───────────── hour (0 - 23)
│ │ │ ┌───────────── day of the month (1 - 31)
│ │ │ │ ┌───────────── month (1 - 12)
│ │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday)
* * * * * *
```

Each field can contain a specific value, an asterisk (`*`) to represent all possible values, or a range of values. Here are some examples of cron expressions:

- `0 0 * * *`: Run every day at midnight
- `*/15 * * * *`: Run every 15 minutes
- `0 9 * * 1`: Run every Monday at 9 AM
- `0 0 1 * *`: Run on the first day of every month at midnight
- `30 * * * * *`: Run at 30 seconds past every minute (6-field)

> **Info:** Keep in mind, Hatchet Cloud meters by Task runs so use seconds wisely. Have
>   questions about pricing? [Contact us](https://hatchet.run/office-hours)

## Defining a Cron in Your Task Definition

You can define a task with a cron schedule by configuring the cron expression as part of the task definition:

#### Python-Sync

```python
# Adding a cron trigger to a workflow is as simple
# as adding a `cron expression` to the `on_cron`
# prop of the workflow definition

cron_workflow = hatchet.workflow(name="CronWorkflow", on_crons=["* * * * *"])


@cron_workflow.task()
def step1(input: EmptyModel, ctx: Context) -> dict[str, str]:
    return {
        "time": "step1",
    }
```

#### Python-Async

```python
# Adding a cron trigger to a workflow is as simple
# as adding a `cron expression` to the `on_cron`
# prop of the workflow definition

cron_workflow = hatchet.workflow(name="CronWorkflow", on_crons=["* * * * *"])


@cron_workflow.task()
def step1(input: EmptyModel, ctx: Context) -> dict[str, str]:
    return {
        "time": "step1",
    }
```

#### Typescript

```typescript
export const onCron = hatchet.workflow({
  name: 'on-cron-workflow',
  on: {
    // 👀 add a cron expression to run the workflow every 15 minutes
    cron: '*/15 * * * *',
  },
});
```

#### Go

```go
dailyCleanup := client.NewStandaloneTask("cleanup-temp-files", func(ctx hatchet.Context, input CronInput) (CronOutput, error) {
	log.Printf("Running daily cleanup at %s", input.Timestamp)

	time.Sleep(2 * time.Second)

	return CronOutput{
		JobName:    "daily-cleanup",
		ExecutedAt: time.Now().Format(time.RFC3339),
		NextRun:    "Next run: tomorrow at 2 AM",
	}, nil
},
	hatchet.WithWorkflowCron("0 2 * * *"),
	hatchet.WithWorkflowCronInput(CronInput{
		Timestamp: time.Now().Format(time.RFC3339),
	}),
	hatchet.WithWorkflowDescription("Daily cleanup and maintenance tasks"),
)
```

#### Ruby

```ruby
CRON_WORKFLOW = HATCHET.workflow(
  name: "CronWorkflow",
  on_crons: ["*/5 * * * *"]
)

CRON_WORKFLOW.task(:cron_task) do |input, ctx|
  puts "Cron task executed at #{Time.now}"
  { "status" => "success" }
end
```

In the examples above, we set the `on cron` property of the task. The property specifies the cron expression that determines when the task should be triggered.


  Note: When modifying a cron in your task definition, it will override any cron
  schedule for previous crons defined in previous task definitions, but crons
  created via the API or Dashboard will still be respected.


## Programmatically Creating Cron Triggers

### Create a Cron Trigger

You can create dynamic cron triggers programmatically via the API. This is useful if you want to create a cron trigger that is not known at the time of task definition,

Here's an example of creating a a cron to trigger a report for a specific customer every day at noon:

#### Python-Sync

```python
cron_trigger = dynamic_cron_workflow.create_cron(
    cron_name="customer-a-daily-report",
    expression="0 12 * * *",
    input=DynamicCronInput(name="John Doe"),
    additional_metadata={
        "customer_id": "customer-a",
    },
)


id = cron_trigger.metadata.id  # the id of the cron trigger
```

#### Python-Async

```python
cron_trigger = await dynamic_cron_workflow.aio_create_cron(
    cron_name="customer-a-daily-report",
    expression="0 12 * * *",
    input=DynamicCronInput(name="John Doe"),
    additional_metadata={
        "customer_id": "customer-a",
    },
)

cron_trigger.metadata.id  # the id of the cron trigger
```

#### Typescript

```typescript
const cron = await simple.cron('simple-daily', '0 0 * * *', {
  Message: 'hello',
});

// it may be useful to save the cron id for later
const cronId = cron.metadata.id;
```

#### Go

```go
createdCron, err := client.Crons().Create(context.Background(), "cleanup-temp-files", features.CreateCronTrigger{
	Name:       "daily-cleanup",
	Expression: "0 0 * * *",
	Input: map[string]interface{}{
		"timestamp": time.Now().Format(time.RFC3339),
	},
	AdditionalMetadata: map[string]interface{}{
		"description": "Daily cleanup and maintenance tasks",
	},
})
if err != nil {
	return err
}
```

#### Ruby

```ruby
cron_trigger = dynamic_cron_workflow.create_cron(
  "customer-a-daily-report",
  "0 12 * * *",
  input: { "name" => "John Doe" }
)

id = cron_trigger.metadata.id
```

In this example you can have different expressions for different customers, or dynamically set the expression based on some other business logic.

When creating a cron via the API, you will receive a cron trigger object with a metadata property containing the id of the cron trigger. This id can be used to reference the cron trigger when deleting the cron trigger and is often stored in a database or other persistence layer.


  Note: Cron Name and Expression are required fields when creating a cron
  trigger and we enforce a unique constraint on the two.


### Delete a Cron Trigger

You can delete a cron trigger by passing the cron object or a cron trigger id to the delete method.

#### Python-Sync

```python
hatchet.cron.delete(cron_id=cron_trigger.metadata.id)
```

#### Python-Async

```python
await hatchet.cron.aio_delete(cron_id=cron_trigger.metadata.id)
```

#### Typescript

```typescript
await hatchet.crons.delete(cronId);
```

#### Go

```go
err = client.Crons().Delete(context.Background(), createdCron.Metadata.Id)
if err != nil {
	return err
}
```

#### Ruby

```ruby
hatchet.cron.delete(cron_trigger.metadata.id)
```


  Note: Deleting a cron trigger will not cancel any currently running instances
  of the task. It will simply stop the cron trigger from triggering the task
  again.


### List Cron Triggers

Retrieves a list of all task cron triggers matching the criteria.

#### Python-Sync

```python
cron_triggers = hatchet.cron.list()
```

#### Python-Async

```python
await hatchet.cron.aio_list()
```

#### Typescript

```typescript
const crons = await hatchet.crons.list({
  workflow: simple,
});
```

#### Go

```go
cronList, err := client.Crons().List(context.Background(), rest.CronWorkflowListParams{
	AdditionalMetadata: &[]string{"description:Daily cleanup and maintenance tasks"},
})
if err != nil {
	return err
}
```

#### Ruby

```ruby
cron_triggers = hatchet.cron.list
```

## Managing Cron Triggers in the Hatchet Dashboard

In the Hatchet Dashboard, you can view and manage cron triggers for your tasks.

Navigate to "Triggers" > "Cron Jobs" in the left sidebar and click "Create Cron Job" at the top right.

You can specify run parameters such as Input, Additional Metadata, and the Expression.

![Create Cron Job](../../public/cron-dash.gif)

## Cron Considerations

When using cron triggers, there are a few considerations to keep in mind:

1. **Time Zone**: Cron schedules are UTC. Make sure to consider the time zone when defining your cron expressions.

2. **Execution Time**: The actual execution time of a cron-triggered task may vary slightly from the scheduled time. Hatchet makes a best-effort attempt to enqueue the task as close to the scheduled time as possible, but there may be slight delays due to system load or other factors.

3. **Missed Schedules**: If a scheduled task is missed (e.g., due to system downtime), Hatchet will **not** automatically run the missed instances. It will wait for the next scheduled time to trigger the task.

4. **Overlapping Schedules**: If a task is still running when the next scheduled time arrives, Hatchet will start a new instance of the task or respect the [concurrency](/v1/concurrency) policy.


---

<!-- Source: https://docs.hatchet.run/v1/bulk-run -->

# Bulk Run Many Tasks

Often you may want to run a task multiple times with different inputs. There is significant overhead (i.e. network roundtrips) to write the task, so if you're running multiple tasks, it's best to use the bulk run methods.

#### Python

You can use the `aio_run_many` method to bulk run a task. This will return a list of results.

```python
greetings = ["Hello, World!", "Hello, Moon!", "Hello, Mars!"]

results = await child_task.aio_run_many(
    [
        # run each greeting as a task in parallel
        child_task.create_bulk_run_item(
            input=SimpleInput(message=greeting),
        )
        for greeting in greetings
    ]
)

# this will await all results and return a list of results
print(results)
```

> **Info:** `Workflow.create_bulk_run_item` is a typed helper to create the inputs for
>   each task.

There are additional bulk methods available on the `Workflow` object.

- `aio_run_many`
- `aio_run_many_no_wait`

And blocking variants:

- `run_many`
- `run_many_no_wait`

As with the run methods, you can call bulk methods from within a task and the runs will be associated with the parent task in the dashboard.

#### Typescript

You can use the `run` method directly to bulk run tasks by passing an array of inputs. This will return a list of results.

```typescript
const res = await simple.run([
  {
    Message: 'HeLlO WoRlD',
  },
  {
    Message: 'Hello MoOn',
  },
]);

// 👀 Access the results of the Task
console.log(res[0].TransformedMessage);
console.log(res[1].TransformedMessage);
```

There are additional bulk methods available on the `Task` object.

- `run`
- `runNoWait`

As with the run methods, you can call bulk methods on the task fn context parameter within a task and the runs will be associated with the parent task in the dashboard.

```typescript
const parent = hatchet.task({
  name: 'simple',
  fn: async (input: SimpleInput, ctx) => {
    // Bulk run two tasks in parallel
    const child = await ctx.bulkRunChildren([
      {
        workflow: simple,
        input: {
          Message: 'Hello, World!',
        },
      },
      {
        workflow: simple,
        input: {
          Message: 'Hello, Moon!',
        },
      },
    ]);

    return {
      TransformedMessage: `${child[0].TransformedMessage} ${child[1].TransformedMessage}`,
    };
  },
});
```

Available bulk methods on the `Context` object are: - `bulkRunChildren` - `bulkRunChildrenNoWait`

#### Go

You can use the `RunMany` method directly on the `Workflow` or `StandaloneTask` instance to bulk run tasks by passing an array of inputs. This will return a list of run IDs.

```go
// Prepare inputs as []RunManyOpt for bulk run
inputs := make([]hatchet.RunManyOpt, len(bulkInputs))
for i, input := range bulkInputs {
	inputs[i] = hatchet.RunManyOpt{
		Input: input,
	}
}

// Run workflows in bulk
ctx := context.Background()
runRefs, err := workflow.RunMany(ctx, inputs)
if err != nil {
	log.Fatalf("failed to run bulk workflows: %v", err)
}
```

Additional bulk methods are coming soon for the Go SDK. Join our [Discord](https://hatchet.run/discord) to stay up to date.

#### Ruby

```ruby
greetings = ["Hello, World!", "Hello, Moon!", "Hello, Mars!"]

results = CHILD_TASK_WF.run_many(
  greetings.map do |greeting|
    CHILD_TASK_WF.create_bulk_run_item(
      input: { "message" => greeting }
    )
  end
)

puts results
```


---

<!-- Source: https://docs.hatchet.run/v1/webhooks -->

# Webhooks


  This feature is currently in development and might change. Reach out for
  feedback or if you encounter any problems registering any external webhooks.


Webhooks allow external systems to trigger Hatchet workflows by sending HTTP requests to dedicated endpoints. This enables real-time integration with third-party services like GitHub, Stripe, Slack, or any system that can send webhook events.

## Creating a webhook

To create a webhook, you'll need to fill out some fields that tell Hatchet how to determine which workflows to trigger from your webhook, and how to validate it when it arrives from the sender. In particular, you'll need to provide the following fields:

#### Name

The **Webhook Name** is tenant-unique (meaning a single tenant can only use each name once), and is used to create the URL for where the incoming webhook request should be sent. For instance, if your tenant id was `d60181b7-da6c-4d4c-92ec-8aa0fc74b3e5` and your webhook name was `my-webhook`, then the URL might look like `https://cloud.onhatchet.run/api/v1/stable/tenants/d60181b7-da6c-4d4c-92ec-8aa0fc74b3e5/webhooks/my-webhook`. Note that you can copy this URL in the dashboard.

#### Source

The **Source** indicates the source of the webhook, which can be a pre-provided one for easy setup like Stripe or Github, or a "generic" one, which lets you configure all of the necessary fields for your webhook integration based on what the webhook sender provides.

#### Event Key Expression

The **Event Key Expression** is a [CEL](https://cel.dev/) expression that you can use to create a dynamic event key from the payload and headers of the incoming webhook. You can either set this to a constant value, like `webhook`, or you could set it to something dynamic using those two options. Some examples:

1. `'stripe:' + input.type` would create event keys where `'stripe:'` is a prefix for all keys indicating the webhook came from Stripe, and `input.type` selects the `type` field off of the webhook payload and uses it to create the final event key. The result might look something like `stripe:payment_intent.created`.
2. `'github:' + headers['x-github-event'] + ':' + input.action` could create a key like `github:star:created`

> **Info:** The result of the event key expression is what Hatchet will use as the event
>   key, so you'd need to set a matching event key as a trigger on your workflows
>   in order to trigger them from the webhooks you create. For instance, you might
>   add `on_events=["stripe:payment_intent.created"]` to listen for payment intent
>   created events in the previous example.

#### Scope Expression (Optional)

The **Scope Expression** is an optional [CEL](https://cel.dev/) expression that evaluates to a string used to filter which workflows to trigger. This is useful when you have multiple workflows listening to the same event key but want to route to specific workflows based on the webhook content.

Like the event key expression, you have access to `input` (the webhook payload) and `headers` (the request headers). Some examples:

1. `input.customer_id` would use the customer ID from the payload as the scope
2. `headers['x-organization-id']` would use a header value as the scope
3. `input.metadata.environment` could route to different workflows based on environment

#### Static Payload (Optional)

The **Static Payload** is an optional JSON object that gets merged with the incoming webhook payload before it's passed to your workflows. This is useful for:

- Adding constant metadata to all events from this webhook
- Injecting configuration values that aren't in the original payload
- Overriding specific fields from the incoming payload

> **Info:** When there's a key collision between the incoming webhook payload and the
>   static payload, the static payload values take precedence.

For example, if you set a static payload of `{"source": "stripe", "environment": "production"}` and receive a webhook with `{"type": "payment_intent.created", "source": "api"}`, the final payload passed to your workflow would be `{"type": "payment_intent.created", "source": "stripe", "environment": "production"}`.

#### Authentication

Finally, you'll need to specify how Hatchet should authenticate incoming webhook requests. For non-generic sources like Stripe and Github, Hatchet has presets for most of the fields, so in most cases you'd only need to provide a secret.

If you're using a generic source, then you'll need to specify an authentication method (either basic auth, an API key, HMAC-based auth), and provide the required fields (such as a username and password in the basic auth case).

> **Warning:** Hatchet encrypts any secrets you provide for validating incoming webhooks.

The different authentication methods require different fields to be provided:

- **Pre-configured sources** (Stripe, GitHub, Slack): Only require a webhook secret
- **Generic sources** require different fields depending on the selected authentication method:
  - **Basic Auth**: Requires a username and password
  - **API Key**: Requires header name containing the key on incoming requests, and secret key itself
  - **HMAC**: Requires a header name containing the secret on incoming requests, the secret itself, an encoding method (e.g. hex, base64), and an algorithm (e.g. `SHA256`, `SHA1`, etc.).

## Usage

While you're creating your webhook (and also after you've created it), you can copy the webhook URL, which is what you'll provide to the webhook _sender_.

Once you've done that, the last thing to do is register the event keys you want your workers to listen for so that they can be triggered by incoming webhooks.

For examples on how to do this, see the [documentation on event triggers](/v1/external-events/run-on-event).


---

<!-- Source: https://docs.hatchet.run/v1/external-events/pushing-events -->

# Pushing Events

You can push an event to Hatchet by calling the `push` method on the Hatchet event client and providing the event name and payload. Any tasks that have registered an [event trigger](/v1/external-events/run-on-event) for that event key will be run.

#### Python

```python
hatchet.event.push("user:create", {"should_skip": False})
```

#### Typescript

```typescript
const res = await hatchet.events.push('simple-event:create', {
  Message: 'hello',
  ShouldSkip: false,
});
```

#### Go

```go
err := client.Events().Push(
	context.Background(),
	"simple-event:create",
	EventInput{
		Message: "Hello, World!",
	},
)
if err != nil {
	return err
}
```

#### Ruby

```ruby
HATCHET.event.push("user:create", { "should_skip" => false })
```

> **Info:** Event triggers evaluate tasks to run at the time of the event. If an event is
>   received before the task is registered, the task will not be run.


---

<!-- Source: https://docs.hatchet.run/v1/external-events/run-on-event -->

# Event Trigger

> This example assumes we have a [task](/v1/tasks) registered on a running [worker](/v1/workers).

Run-on-event allows you to trigger one or more tasks when a specific event occurs. This is useful when you need to execute a task in response to an ephemeral event where the result is not important. See [Event-Driven Systems](/guides/event-driven) for a detailed guide. A few common use cases for event-triggered task runs are:

1. Running a task when an ephemeral event is received, such as a webhook or a message from a queue.
2. When you want to run multiple independent tasks in response to a single event. For instance, if you wanted to run a `send_welcome_email` task, and you also wanted to run a `grant_new_user_credits` task, and a `reward_referral` task, all triggered by the signup. In this case, you might declare all three of those tasks with an event trigger for `user:signup`, and then have them all kick off when that event happens.

> **Info:** Event triggers evaluate tasks to run at the time of the event. If an event is
>   received before the task is registered, the task will not be run.

## Declaring Event Triggers

To run a task on an event, you need to declare the event that will trigger the task. This is done by declaring the `on_events` property in the task declaration.

#### Python

```python
EVENT_KEY = "user:create"
SECONDARY_KEY = "foobarbaz"
WILDCARD_KEY = "subscription:*"


class EventWorkflowInput(BaseModel):
    should_skip: bool


event_workflow = hatchet.workflow(
    name="EventWorkflow",
    on_events=[EVENT_KEY, SECONDARY_KEY, WILDCARD_KEY],
    input_validator=EventWorkflowInput,
)
```

#### Typescript

```typescript
export const lower = hatchet.workflow({
  name: 'lower',
  // 👀 Declare the event that will trigger the workflow
  onEvents: ['simple-event:create'],
});
```

#### Go

```go
const SimpleEvent = "simple-event:create"

func Lower(client *hatchet.Client) *hatchet.StandaloneTask {
	return client.NewStandaloneTask(
		"lower", func(ctx hatchet.Context, input EventInput) (*LowerTaskOutput, error) {
			return &LowerTaskOutput{
				TransformedMessage: strings.ToLower(input.Message),
			}, nil
		},
		hatchet.WithWorkflowEvents(SimpleEvent),
	)
}
```

#### Ruby

```ruby
EVENT_KEY = "user:create"
SECONDARY_KEY = "foobarbaz"
WILDCARD_KEY = "subscription:*"

EVENT_WORKFLOW = HATCHET.workflow(
  name: "EventWorkflow",
  on_events: [EVENT_KEY, SECONDARY_KEY, WILDCARD_KEY]
)
```

> **Info:** Note: Multiple tasks can be triggered by the same event.

> **Info:** As of engine version 0.65.0, Hatchet supports wildcard event triggers using
>   the `*` wildcard pattern. For example, you could register `subscription:*` as
>   your event key, which would match incoming events like `subcription:create`,
>   `subscription:renew`, `subscription:cancel`, and so on.


---

<!-- Source: https://docs.hatchet.run/v1/external-events/event-filters -->

# Event Filters

Events can be _filtered_ in Hatchet, which allows you to push events to Hatchet and only trigger task runs from them in certain cases. **If you enable filters on a workflow, your workflow will be triggered once for each matching filter on any incoming event with a matching scope** (more on scopes below).

## Basic Usage

There are two ways to create filters in Hatchet.

### Default filters on the workflow

The simplest way to create a filter is to register it declaratively with your workflow when it's created. For example:

#### Python

```python
event_workflow_with_filter = hatchet.workflow(
    name="EventWorkflow",
    on_events=[EVENT_KEY, SECONDARY_KEY, WILDCARD_KEY],
    input_validator=EventWorkflowInput,
    default_filters=[
        DefaultFilter(
            expression="true",
            scope="example-scope",
            payload={
                "main_character": "Anna",
                "supporting_character": "Stiva",
                "location": "Moscow",
            },
        )
    ],
)
```

#### Typescript

```typescript
export const lowerWithFilter = hatchet.workflow({
  name: 'lower',
  // 👀 Declare the event that will trigger the workflow
  onEvents: ['simple-event:create'],
  defaultFilters: [
    {
      expression: 'true',
      scope: 'example-scope',
      payload: {
        mainCharacter: 'Anna',
        supportingCharacter: 'Stiva',
        location: 'Moscow',
      },
    },
  ],
});
```

#### Go

```go
func LowerWithFilter(client *hatchet.Client) *hatchet.StandaloneTask {
	return client.NewStandaloneTask(
		"lower", accessFilterPayload,
		hatchet.WithWorkflowEvents(SimpleEvent),
		hatchet.WithFilters(types.DefaultFilter{
			Expression: "true",
			Scope:      "example-scope",
			Payload: map[string]interface{}{
				"main_character":       "Anna",
				"supporting_character": "Stiva",
				"location":             "Moscow"},
		}),
	)
}
```

#### Ruby

```ruby
EVENT_WORKFLOW_WITH_FILTER = HATCHET.workflow(
  name: "EventWorkflow",
  on_events: [EVENT_KEY, SECONDARY_KEY, WILDCARD_KEY],
  default_filters: [
    Hatchet::DefaultFilter.new(
      expression: "true",
      scope: "example-scope",
      payload: {
        "main_character" => "Anna",
        "supporting_character" => "Stiva",
        "location" => "Moscow"
      }
    )
  ]
)

EVENT_WORKFLOW.task(:task) do |input, ctx|
  puts "event received"
  ctx.filter_payload
end
```

In each of these cases, we register a filter with the workflow. Note that these "declarative" filters are overwritten each time your workflow is updated, so the ids associated with them will not be stable over time. This allows you to modify a filter in-place or remove a filter, and not need to manually delete it over the API.

### Filters feature client

You also can create event filters by using the `filters` clients on the SDKs:

#### Python

```python
hatchet.filters.create(
    workflow_id=event_workflow.id,
    expression="input.should_skip == false",
    scope="foobarbaz",
    payload={
        "main_character": "Anna",
        "supporting_character": "Stiva",
        "location": "Moscow",
    },
)
```

#### Typescript

```typescript
hatchet.filters.create({
  workflowId: lower.id,
  expression: 'input.ShouldSkip == false',
  scope: 'foobarbaz',
  payload: {
    main_character: 'Anna',
    supporting_character: 'Stiva',
    location: 'Moscow',
  },
});
```

#### Go

```go
_, err = client.Filters().Create(
	context.Background(),
	rest.V1CreateFilterRequest{
		WorkflowId: uuid.MustParse("bb866b59-5a86-451b-8023-10d451db11d3"),
		Expression: "true",
		Scope:      "example-scope",
	},
)
if err != nil {
	return err
}
```

#### Ruby

```ruby
HATCHET_CLIENT.filters.create(
  workflow_id: EVENT_WORKFLOW.id,
  expression: "input.should_skip == false",
  scope: "foobarbaz",
  payload: {
    "main_character" => "Anna",
    "supporting_character" => "Stiva",
    "location" => "Moscow"
  }
)
```

> **Warning:** Note the `scope` argument to the filter. When you create a filter, it must be
>   given a `scope` which will be used by Hatchet internally to look it up. When
>   you push events that you want filtered, you **must provide a `scope` with
>   those events that matches the scope sent with the filter**. If you do not, the
>   filter will not apply.

Then, push an event that uses the filter to determine whether or not to run. For instance, this run will be skipped, since the payload does not match the expression:

#### Python

```python
hatchet.event.push(
    event_key=EVENT_KEY,
    payload={
        "should_skip": True,
    },
    options=PushEventOptions(
        scope="foobarbaz",
    ),
)
```

#### Typescript

```typescript
hatchet.events.push(
  SIMPLE_EVENT,
  {
    Message: 'hello',
    ShouldSkip: true,
  },
  {
    scope: 'foobarbaz',
  }
);
```

#### Go

```go
skipPayload := map[string]interface{}{
	"shouldSkip": true,
}
skipScope := "foobarbaz"
err = client.Events().Push(
	context.Background(),
	"simple-event:create",
	skipPayload,
	v0Client.WithFilterScope(&skipScope),
)
if err != nil {
	return err
}
```

#### Ruby

```ruby
HATCHET_CLIENT.event.push(
  EVENT_KEY,
  { "should_skip" => true },
  scope: "foobarbaz"
)
```

But this one will be triggered since the payload _does_ match the expression:

#### Python

```python
hatchet.event.push(
    event_key=EVENT_KEY,
    payload={
        "should_skip": False,
    },
    options=PushEventOptions(
        scope="foobarbaz",
    ),
)
```

#### Typescript

```typescript
hatchet.events.push(
  SIMPLE_EVENT,
  {
    Message: 'hello',
    ShouldSkip: false,
  },
  {
    scope: 'foobarbaz',
  }
);
```

#### Go

```go
triggerPayload := map[string]interface{}{
	"shouldSkip": false,
}
triggerScope := "foobarbaz"
err = client.Events().Push(
	context.Background(),
	"simple-event:create",
	triggerPayload,
	v0Client.WithFilterScope(&triggerScope),
)
if err != nil {
	return err
}
```

#### Ruby

```ruby
HATCHET_CLIENT.event.push(
  EVENT_KEY,
  { "should_skip" => false },
  scope: "foobarbaz"
)
```

> **Info:** In Hatchet, filters are "positive", meaning that we look for _matches_ to the
>   filter to determine which tasks to trigger.

## Accessing the filter payload

You can access the filter payload by using the `Context` in the task that was triggered by your event:

#### Python

```python
@event_workflow_with_filter.task()
def filtered_task(input: EventWorkflowInput, ctx: Context) -> None:
    print(ctx.filter_payload)
```

#### Typescript

```typescript
lowerWithFilter.task({
  name: 'lowerWithFilter',
  fn: (input, ctx) => {
    console.log(ctx.filterPayload());
  },
});
```

#### Go

```go
func accessFilterPayload(ctx hatchet.Context, input EventInput) (*LowerTaskOutput, error) {
	fmt.Println(ctx.FilterPayload())
	return &LowerTaskOutput{
		TransformedMessage: strings.ToLower(input.Message),
	}, nil
}
```

#### Ruby

```ruby
EVENT_WORKFLOW_WITH_FILTER.task(:filtered_task) do |input, ctx|
  puts ctx.filter_payload.inspect
end
```

## Advanced Usage

In addition to referencing `input` in the expression (which corresponds to the _event_ payload), you can also reference the following fields:

1. `payload` corresponds to the _filter_ payload (which was part of the request when the filter was created).
2. `additional_metadata` allows for filtering based on `additional_metadata` sent with the event.
3. `event_key` allows for filtering based on the key of the event, such as `user:created`.


---

<!-- Source: https://docs.hatchet.run/v1/inter-service-triggering -->

## Invoking Tasks From Other Services

While Hatchet recommends importing your workflows and standalone tasks directly to use for triggering runs, this only works in a monorepo or similar setups where you have access to those objects. However, it's common to have a polyrepo, have code written in multiple languages, or otherwise not be able to import your workflows and standalone tasks directly. Hatchet provides first-class, type-safe support for handling these cases as well, with only minor code duplication, to allow you to trigger your tasks from anywhere in a type-safe way.

### Creating a "Stub" Task on your External Service (Recommended)

The recommended way to trigger a run from a service where you _cannot_ import the workflow or standalone task definition directly is to create a "stub" task or workflow on your external service. This is a Hatchet task or workflow that has the same name and input/output types as the task you want to trigger on your Hatchet worker, but without the function or other configuration.

This allows you to have a polyglot, fully typed interface with full SDK support.

#### Typescript

```typescript
import { hatchet } from '../hatchet-client';

// (optional) Define the input type for the workflow
export type SimpleInput = {
  Message: string;
};

// (optional) Define the output type for the workflow
export type SimpleOutput = {
  'to-lower': {
    TransformedMessage: string;
  };
};

// declare the workflow with the same name as the
// workflow name on the worker
export const simple = hatchet.workflow({
  name: 'simple',
});

// you can use all the same run methods on the stub
// with full type-safety
simple.run({ Message: 'Hello, World!' });
simple.runNoWait({ Message: 'Hello, World!' });
simple.schedule(new Date(), { Message: 'Hello, World!' });
simple.cron('my-cron', '0 0 * * *', { Message: 'Hello, World!' });
```

#### Python

Consider a task with an implementation like this:

```python
from pydantic import BaseModel

from hatchet_sdk import Context, Hatchet


class TaskInput(BaseModel):
    user_id: int


class TaskOutput(BaseModel):
    ok: bool


hatchet = Hatchet()


@hatchet.task(name="externally-triggered-task", input_validator=TaskInput)
async def externally_triggered_task(input: TaskInput, ctx: Context) -> TaskOutput:
    return TaskOutput(ok=True)
```

To trigger this task from a separate service, for instance, in a microservices architecture, where the code is not shared, start by defining models that match the input and output types of the task defined above.

```python
class TaskInput(BaseModel):
    user_id: int


class TaskOutput(BaseModel):
    ok: bool
```

Next, create the stub task.

```python
stub = hatchet.stubs.task(
    # make sure the name and schemas exactly match the implementation
    name="externally-triggered-task",
    input_validator=TaskInput,
    output_validator=TaskOutput,
)
```

Finally, use the stub to trigger the underlying task, and (optionally) retrieve the result.

```python
# input type checks properly
result = await stub.aio_run(input=TaskInput(user_id=1234))

# `result.ok` type checks properly
print("Is successful:", result.ok)
```

#### Go

```go
package main

import (
	"context"
	"fmt"
	"log"

	hatchet "github.com/hatchet-dev/hatchet/sdks/go"
)

type StubInput struct {
	Message string `json:"message"`
}

type StubOutput struct {
	Ok bool `json:"ok"`
}

func StubWorkflow(client *hatchet.Client) *hatchet.StandaloneTask {
	return client.NewStandaloneTask("stub-workflow", func(ctx hatchet.Context, input StubInput) (StubOutput, error) {
		return StubOutput{
			Ok: true,
		}, nil
	})
}

func main() {
	client, err := hatchet.NewClient()
	if err != nil {
		log.Fatalf("failed to create hatchet client: %v", err)
	}

	task := StubWorkflow(client)

	// we are simply running the task here, but it can be implemented in another service / worker
	// and in another language with the same name and input-output types
	result, err := task.Run(context.Background(), StubInput{Message: "Hello, World!"})
	if err != nil {
		log.Fatalf("failed to run task: %v", err)
	}

	fmt.Println(result)
}
```

#### Ruby


  Note that this approach requires code duplication, which can break type
  safety. For instance, if the input type to your workflow changes, you need to
  remember to also change the type passed to the stub. Some ways to mitigate
  risks here are helpful comments reminding developers to keep these types in
  sync, code generation tools, and end-to-end tests.


---

<!-- Source: https://docs.hatchet.run/v1/retry-policies -->

# Simple Task Retries

Hatchet provides a simple and effective way to handle failures in your tasks using a retry policy. This feature allows you to specify the number of times a task should be retried if it fails, helping to improve the reliability and resilience of your tasks.

> **Info:** Task-level retries can be added to both `Standalone Tasks` and `Workflow
>   Tasks`.

## How it works

When a task fails (i.e. throws an error or returns a non-zero exit code), Hatchet can automatically retry the task based on the `retries` configuration defined in the task object. Here's how it works:

1. If a task fails and `retries` is set to a value greater than 0, Hatchet will catch the error and retry the task.
2. The task will be retried up to the specified number of times, with each retry being executed after a short delay to avoid overwhelming the system.
3. If the task succeeds during any of the retries, the task will continue as normal.
4. If the task continues to fail after exhausting all the specified retries, the task will be marked as failed.

This simple retry mechanism can help to mitigate transient failures, such as network issues or temporary unavailability of external services, without requiring complex error handling logic in your task code.

## How to use task-level retries

To enable retries for a task, simply add the `retries` property to the task object in your task definition:

#### Python

```python
@simple_workflow.task(retries=3)
def always_fail(input: EmptyModel, ctx: Context) -> dict[str, str]:
    raise Exception("simple task failed")
```

#### Typescript

```typescript
export const retries = hatchet.task({
  name: 'retries',
  retries: 3,
  fn: async (_, ctx) => {
    throw new Error('intentional failure');
  },
});
```

#### Go

```go
retries := client.NewStandaloneTask("retries-task", func(ctx hatchet.Context, input RetriesInput) (*RetriesResult, error) {
	return nil, errors.New("intentional failure")
}, hatchet.WithRetries(3))
```

#### Ruby

```ruby
SIMPLE_RETRY_WORKFLOW.task(:always_fail, retries: 3) do |input, ctx|
  raise "simple task failed"
end
```

You can add the `retries` property to any task, and Hatchet will handle the retry logic automatically.

It's important to note that task-level retries are not suitable for all types of failures. For example, if a task fails due to a programming error or an invalid configuration, retrying the task will likely not resolve the issue. In these cases, you should fix the underlying problem in your code or configuration rather than relying on retries.

Additionally, if a task interacts with external services or databases, you should ensure that the operation is idempotent (i.e. can be safely repeated without changing the result) before enabling retries. Otherwise, retrying the task could lead to unintended side effects or inconsistencies in your data.

## Accessing the Retry Count in a Running Task

If you need to access the current retry count within a task, you can use the `retryCount` method available in the task context:

#### Python

```python
@simple_workflow.task(retries=3)
def fail_twice(input: EmptyModel, ctx: Context) -> dict[str, str]:
    if ctx.retry_count < 2:
        raise Exception("simple task failed")

    return {"status": "success"}
```

#### Typescript

```typescript
export const retriesWithCount = hatchet.task({
  name: 'retries-with-count',
  retries: 3,
  fn: async (_, ctx) => {
    // > Get the current retry count
    const retryCount = ctx.retryCount();

    console.log(`Retry count: ${retryCount}`);

    if (retryCount < 2) {
      throw new Error('intentional failure');
    }

    return {
      message: 'success',
    };
  },
});
```

#### Go

```go
retriesWithCount := client.NewStandaloneTask("fail-twice-task", func(ctx hatchet.Context, input RetriesWithCountInput) (*RetriesWithCountResult, error) {
	// Get the current retry count
	retryCount := ctx.RetryCount()

	fmt.Printf("Retry count: %d\n", retryCount)

	if retryCount < 2 {
		return nil, errors.New("intentional failure")
	}

	return &RetriesWithCountResult{
		Message: "success",
	}, nil
}, hatchet.WithRetries(3))
```

#### Ruby

```ruby
SIMPLE_RETRY_WORKFLOW.task(:fail_twice, retries: 3) do |input, ctx|
  raise "simple task failed" if ctx.retry_count < 2

  { "status" => "success" }
end
```

## Exponential Backoff

Hatchet also supports exponential backoff for retries, which can be useful for handling failures in a more resilient manner. Exponential backoff increases the delay between retries exponentially, giving the failing service more time to recover before the next retry.

#### Python

```python
@backoff_workflow.task(
    retries=10,
    # 👀 Maximum number of seconds to wait between retries
    backoff_max_seconds=10,
    # 👀 Factor to increase the wait time between retries.
    # This sequence will be 2s, 4s, 8s, 10s, 10s, 10s... due to the maxSeconds limit
    backoff_factor=2.0,
)
def backoff_task(input: EmptyModel, ctx: Context) -> dict[str, str]:
    if ctx.retry_count < 3:
        raise Exception("backoff task failed")

    return {"status": "success"}
```

#### Typescript

```typescript
export const withBackoff = hatchet.task({
  name: 'with-backoff',
  retries: 10,
  backoff: {
    // 👀 Maximum number of seconds to wait between retries
    maxSeconds: 10,
    // 👀 Factor to increase the wait time between retries.
    // This sequence will be 2s, 4s, 8s, 10s, 10s, 10s... due to the maxSeconds limit
    factor: 2,
  },
  fn: async () => {
    throw new Error('intentional failure');
  },
});
```

#### Go

```go
withBackoff := client.NewStandaloneTask("with-backoff-task", func(ctx hatchet.Context, input BackoffInput) (*BackoffResult, error) {
	return nil, errors.New("intentional failure")
}, hatchet.WithRetries(3), hatchet.WithRetryBackoff(2, 10))
```

#### Ruby

```ruby
BACKOFF_WORKFLOW.task(
  :backoff_task,
  retries: 10,
  # Maximum number of seconds to wait between retries
  backoff_max_seconds: 10,
  # Factor to increase the wait time between retries.
  # This sequence will be 2s, 4s, 8s, 10s, 10s, 10s... due to the maxSeconds limit
  backoff_factor: 2.0
) do |input, ctx|
  raise "backoff task failed" if ctx.retry_count < 3

  { "status" => "success" }
end
```

## Bypassing Retry logic

The Hatchet SDKs each expose a `NonRetryable` exception, which allows you to bypass pre-configured retry logic for the task. **If your task raises this exception, it will not be retried.** This allows you to circumvent the default retry behavior in instances where you don't want to or cannot safely retry. Some examples in which this might be useful include:

1. A task that calls an external API which returns a 4XX response code.
2. A task that contains a single non-idempotent operation that can fail but cannot safely be rerun on failure, such as a billing operation.
3. A failure that requires manual intervention to resolve.

#### Python

```python
@non_retryable_workflow.task(retries=1)
def should_not_retry(input: EmptyModel, ctx: Context) -> None:
    raise NonRetryableException("This task should not retry")
```

#### Typescript

```typescript
const shouldNotRetry = nonRetryableWorkflow.task({
  name: 'should-not-retry',
  fn: () => {
    throw new NonRetryableError('This task should not retry');
  },
  retries: 1,
});
```

#### Go

```go
retries := client.NewStandaloneTask("non-retryable-task", func(ctx hatchet.Context, input NonRetryableInput) (*NonRetryableResult, error) {
	return nil, worker.NewNonRetryableError(errors.New("intentional failure"))
}, hatchet.WithRetries(3))
```

#### Ruby

```ruby
NON_RETRYABLE_WORKFLOW.task(:should_not_retry, retries: 1) do |input, ctx|
  raise Hatchet::NonRetryableError, "This task should not retry"
end

NON_RETRYABLE_WORKFLOW.task(:should_retry_wrong_exception_type, retries: 1) do |input, ctx|
  raise TypeError, "This task should retry because it's not a NonRetryableError"
end

NON_RETRYABLE_WORKFLOW.task(:should_not_retry_successful_task, retries: 1) do |input, ctx|
  # no-op
end
```

In these cases, even though `retries` is set to a non-zero number (meaning the task would ordinarily retry), Hatchet will not retry.

## Conclusion

Hatchet's task-level retry feature is a simple and effective way to handle transient failures in your tasks, improving the reliability and resilience of your tasks. By specifying the number of retries for each task, you can ensure that your tasks can recover from temporary issues without requiring complex error handling logic.

Remember to use retries judiciously and only for tasks that are idempotent and can safely be repeated. For more advanced retry strategies, such as exponential backoff or circuit breaking, stay tuned for future updates to Hatchet's retry capabilities.


---

<!-- Source: https://docs.hatchet.run/v1/timeouts -->

# Timeouts in Hatchet

Timeouts are an important concept in Hatchet that allow you to control how long a task is allowed to run before it is considered to have failed. This is useful for ensuring that your tasks don't run indefinitely and consume unnecessary resources. Timeouts in Hatchet are treated as failures and the task will be [retried](./retry-policies.mdx) if specified.

There are two types of timeouts in Hatchet:

1. **Scheduling Timeouts** (Default 5m) - the time a task is allowed to wait in the queue before it is cancelled
2. **Execution Timeouts** (Default 60s) - the time a task is allowed to run before it is considered to have failed

## Timeout Format

In Hatchet, timeouts are specified using a string in the format `<number><unit>`, where `<number>` is an integer and `<unit>` is one of:

- `s` for seconds
- `m` for minutes
- `h` for hours

For example:

- `10s` means 10 seconds
- `4m` means 4 minutes
- `1h` means 1 hour

If no unit is specified, seconds are assumed.

> **Info:** In the Python SDK, timeouts can also be specified as a `datetime.timedelta`
>   object.

### Task-Level Timeouts

You can specify execution and scheduling timeouts for a task using the `execution_timeout` and `schedule_timeout` parameters when creating a task.

#### Ruby

```python
# 👀 Specify an execution timeout on a task
@timeout_wf.task(
    execution_timeout=timedelta(seconds=5), schedule_timeout=timedelta(minutes=10)
)
def timeout_task(input: EmptyModel, ctx: Context) -> dict[str, str]:
    time.sleep(30)
    return {"status": "success"}
```

#### Tab 2

```typescript
export const withTimeouts = hatchet.task({
  name: 'with-timeouts',
  // time the task can wait in the queue before it is cancelled
  scheduleTimeout: '10s',
  // time the task can run before it is cancelled
  executionTimeout: '10s',
  fn: async (input: SimpleInput, ctx) => {
    // wait 15 seconds
    await sleep(15000);

    // get the abort controller
    const { abortController } = ctx;

    // if the abort controller is aborted, throw an error
    if (abortController.signal.aborted) {
      throw new Error('cancelled');
    }

    return {
      TransformedMessage: input.Message.toLowerCase(),
    };
  },
});
```

#### Tab 3

```go
// Task that will timeout - sleeps for 10 seconds but has 3 second timeout
_ = timeoutWorkflow.NewTask("timeout-task",
	func(ctx hatchet.Context, input TimeoutInput) (TimeoutOutput, error) {
		log.Printf("Starting task that will timeout. Message: %s", input.Message)

		// Sleep for 10 seconds (will be interrupted by timeout)
		time.Sleep(10 * time.Second)

		// This should not be reached due to timeout
		log.Println("Task completed successfully (this shouldn't be reached)")
		return TimeoutOutput{
			Status:    "completed",
			Completed: true,
		}, nil
	},
	hatchet.WithExecutionTimeout(3*time.Second), // 3 second timeout
)
```

#### Tab 4

```ruby
# Specify an execution timeout on a task
TIMEOUT_WF.task(:timeout_task, execution_timeout: 5, schedule_timeout: 600) do |input, ctx|
  sleep 30
  { "status" => "success" }
end

REFRESH_TIMEOUT_WF = HATCHET.workflow(name: "RefreshTimeoutWorkflow")
```

In these tasks, both timeouts are specified, meaning:

1. If the task is not scheduled before the `schedule_timeout` is reached, it will be cancelled.
2. If the task does not complete before the `execution_timeout` is reached (after starting), it will be cancelled.

> **Warning:** A timed out step does not guarantee that the step will be stopped immediately.
>   The step will be stopped as soon as the worker is able to stop the step. See
>   [cancellation](./cancellation.mdx) for more information.

## Refreshing Timeouts

In some cases, you may need to extend the timeout for a step while it is running. This can be done using the `refreshTimeout` method provided by the step context (`ctx`).

For example:

#### Ruby

```python
@refresh_timeout_wf.task(execution_timeout=timedelta(seconds=4))
def refresh_task(input: EmptyModel, ctx: Context) -> dict[str, str]:
    ctx.refresh_timeout(timedelta(seconds=10))
    time.sleep(5)

    return {"status": "success"}
```

#### Tab 2

```typescript
export const refreshTimeout = hatchet.task({
  name: 'refresh-timeout',
  executionTimeout: '10s',
  scheduleTimeout: '10s',
  fn: async (input: SimpleInput, ctx) => {
    // adds 15 seconds to the execution timeout
    ctx.refreshTimeout('15s');
    await sleep(15000);

    // get the abort controller
    const { abortController } = ctx;

    // now this condition will not be met
    // if the abort controller is aborted, throw an error
    if (abortController.signal.aborted) {
      throw new Error('cancelled');
    }

    return {
      TransformedMessage: input.Message.toLowerCase(),
    };
  },
});
```

#### Tab 3

```go
// Create workflow with timeout refresh example
refreshTimeoutWorkflow := client.NewWorkflow("refresh-timeout-demo",
	hatchet.WithWorkflowDescription("Demonstrates timeout refresh functionality"),
	hatchet.WithWorkflowVersion("1.0.0"),
)

// Task that refreshes its timeout to avoid timing out
_ = refreshTimeoutWorkflow.NewTask("refresh-timeout-task",
	func(ctx hatchet.Context, input TimeoutInput) (TimeoutOutput, error) {
		log.Printf("Starting task with timeout refresh. Message: %s", input.Message)

		// Refresh timeout by 10 seconds
		log.Println("Refreshing timeout by 10 seconds...")
		err := ctx.RefreshTimeout("10s")
		if err != nil {
			log.Printf("Failed to refresh timeout: %v", err)
			return TimeoutOutput{
				Status:    "failed",
				Completed: false,
			}, err
		}

		// Now sleep for 5 seconds (should complete successfully)
		log.Println("Sleeping for 5 seconds...")
		time.Sleep(5 * time.Second)

		log.Println("Task completed successfully after timeout refresh")
		return TimeoutOutput{
			Status:    "completed",
			Completed: true,
		}, nil
	},
	hatchet.WithExecutionTimeout(3*time.Second), // Initial 3 second timeout
)
```

#### Tab 4

```ruby
REFRESH_TIMEOUT_WF.task(:refresh_task, execution_timeout: 4) do |input, ctx|
  ctx.refresh_timeout(10)
  sleep 5

  { "status" => "success" }
end
```

In this example, the step initially would exceed its execution timeout. But before it does, we call the `refreshTimeout` method, which extends the timeout and allows it to complete. Importantly, refreshing a timeout is an additive operation - the new timeout is added to the existing timeout. So for instance, if the task originally had a timeout of `30s` and we call `refreshTimeout("15s")`, the new timeout will be `45s`.

The `refreshTimeout` function can be called multiple times within a step to further extend the timeout as needed.

## Use Cases

Timeouts are useful in a variety of scenarios:

- Ensuring tasks don't run indefinitely and consume unnecessary resources
- Failing tasks early if a critical step takes too long
- Keeping tasks responsive by ensuring individual steps complete in a timely manner
- Preventing infinite loops or hung processes from blocking the entire system

For example, if you have a task that makes an external API call, you may want to set a timeout to ensure the task fails quickly if the API is unresponsive, rather than waiting indefinitely.

By carefully considering timeouts for your tasks and steps, you can build more resilient and responsive systems with Hatchet.


---

<!-- Source: https://docs.hatchet.run/v1/cancellation -->

# Cancellation in Hatchet Tasks

Hatchet provides a mechanism for canceling task executions gracefully, allowing you to signal to running tasks that they should stop running. Cancellation can be triggered on graceful termination of a worker or automatically through concurrency control strategies like [`CANCEL_IN_PROGRESS`](./concurrency.mdx#cancel_in_progress), which cancels currently running task instances to free up slots for new instances when the concurrency limit is reached.

When a task is canceled, Hatchet sends a cancellation signal to the task. The task can then check for the cancellation signal and take appropriate action, such as cleaning up resources, aborting network requests, or gracefully terminating their execution.

## Cancellation Mechanisms

#### Python

```python
@cancellation_workflow.task()
def check_flag(input: EmptyModel, ctx: Context) -> dict[str, str]:
    for i in range(3):
        time.sleep(1)

        # Note: Checking the status of the exit flag is mostly useful for cancelling
        # sync tasks without needing to forcibly kill the thread they're running on.
        if ctx.exit_flag:
            print("Task has been cancelled")
            raise ValueError("Task has been cancelled")

    return {"error": "Task should have been cancelled"}
```
```python
@cancellation_workflow.task()
async def self_cancel(input: EmptyModel, ctx: Context) -> dict[str, str]:
    await asyncio.sleep(2)

    ## Cancel the task
    await ctx.aio_cancel()

    await asyncio.sleep(10)

    return {"error": "Task should have been cancelled"}
```

#### Typescript

```typescript
export const cancellation = hatchet.task({
  name: 'cancellation',
  fn: async (_, ctx) => {
    await sleep(10 * 1000);

    if (ctx.cancelled) {
      throw new Error('Task was cancelled');
    }

    return {
      Completed: true,
    };
  },
});
```
```typescript
export const abortSignal = hatchet.task({
  name: 'abort-signal',
  fn: async (_, { abortController }) => {
    try {
      const response = await axios.get('https://api.example.com/data', {
        signal: abortController.signal,
      });
      // Handle the response
    } catch (error) {
      if (axios.isCancel(error)) {
        // Request was canceled
        console.log('Request canceled');
      } else {
        // Handle other errors
      }
    }
  },
});
```

#### Go

```go
// Add a long-running task that can be cancelled
_ = workflow.NewTask("long-running-task", func(ctx hatchet.Context, input CancellationInput) (CancellationOutput, error) {
	log.Printf("Starting long-running task with message: %s", input.Message)

	// Simulate long-running work with cancellation checking
	for i := 0; i < 10; i++ {
		select {
		case <-ctx.Done():
			log.Printf("Task cancelled after %d steps", i)
			return CancellationOutput{
				Status:    "cancelled",
				Completed: false,
			}, nil
		default:
			log.Printf("Working... step %d/10", i+1)
			time.Sleep(1 * time.Second)
		}
	}

	log.Println("Task completed successfully")
	return CancellationOutput{
		Status:    "completed",
		Completed: true,
	}, nil
}, hatchet.WithExecutionTimeout(30*time.Second))
```

#### Ruby

```ruby
CANCELLATION_WORKFLOW.task(:check_flag) do |input, ctx|
  3.times do
    sleep 1

    # Note: Checking the status of the exit flag is mostly useful for cancelling
    # sync tasks without needing to forcibly kill the thread they're running on.
    if ctx.cancelled?
      puts "Task has been cancelled"
      raise "Task has been cancelled"
    end
  end

  { "error" => "Task should have been cancelled" }
end
```
```ruby
CANCELLATION_WORKFLOW.task(:self_cancel) do |input, ctx|
  sleep 2

  ## Cancel the task
  ctx.cancel

  sleep 10

  { "error" => "Task should have been cancelled" }
end
```

## Cancellation Best Practices

When working with cancellation in Hatchet tasks, consider the following best practices:

1. **Graceful Termination**: When a task receives a cancellation signal, aim to terminate its execution gracefully. Clean up any resources, abort pending operations, and perform any necessary cleanup tasks before returning from the task function.

2. **Cancellation Checks**: Regularly check for cancellation signals within long-running tasks or loops. This allows the task to respond to cancellation in a timely manner and avoid unnecessary processing.

3. **Asynchronous Operations**: If a task performs asynchronous operations, such as network requests or file I/O, consider passing the cancellation signal to those operations. Many libraries and APIs support cancellation through the `AbortSignal` interface.

4. **Error Handling**: Handle cancellation errors appropriately. Distinguish between cancellation errors and other types of errors to provide meaningful error messages and take appropriate actions.

5. **Cancellation Propagation**: If a task invokes other functions or libraries, consider propagating the cancellation signal to those dependencies. This ensures that cancellation is handled consistently throughout the task.

## Additional Features

In addition to the methods of cancellation listed here, Hatchet also supports [bulk cancellation](./bulk-retries-and-cancellations.mdx), which allows you to cancel many tasks in bulk using either their IDs or a set of filters, which is often the easiest way to cancel many things at once.

## Conclusion

Cancellation is a powerful feature in Hatchet that allows you to gracefully stop task executions when needed. Remember to follow best practices when implementing cancellation in your tasks, such as graceful termination, regular cancellation checks, handling asynchronous operations, proper error handling, and cancellation propagation.

By incorporating cancellation into your Hatchet tasks and workflows, you can build more resilient and responsive systems that can adapt to changing circumstances and user needs.


---

<!-- Source: https://docs.hatchet.run/v1/bulk-retries-and-cancellations -->

# Bulk Cancellations and Replays

V1 adds the ability to cancel or replay task runs in bulk, which you can now do either in the Hatchet Dashboard or programmatically via the SDKs and the REST API.

There are two ways of bulk cancelling or replaying tasks in both cases:

1. You can provide a list of task run ids to cancel or replay, which will cancel or replay all of the tasks in the list.
2. You can provide a list of filters, similar to the list of filters on task runs in the Dashboard, and cancel or replay runs matching those filters. For instance, if you wanted to replay all failed runs of a `SimpleTask` from the past fifteen minutes that had the `foo` field in `additional_metadata` set to `bar`, you could apply those filters and replay all of the matching runs.

### Bulk Operations by Run Ids

The first way to bulk cancel or replay runs is by providing a list of run ids. This is the most straightforward way to cancel or replay runs in bulk.

#### Python

> **Info:** In the Python SDK, the mechanics of bulk replaying and bulk cancelling tasks
>   are exactly the same. The only change would be replacing e.g.
>   `hatchet.runs.bulk_cancel` with `hatchet.runs.bulk_replay`.

First, we'll start by fetching a task via the REST API.

```python
from datetime import datetime, timedelta, timezone

from hatchet_sdk import BulkCancelReplayOpts, Hatchet, RunFilter, V1TaskStatus

hatchet = Hatchet()

workflows = hatchet.workflows.list()

assert workflows.rows

workflow = workflows.rows[0]
```

Now that we have a task, we'll get runs for it, so that we can use them to bulk cancel by run id.

```python
workflow_runs = hatchet.runs.list(workflow_ids=[workflow.metadata.id])
```

And finally, we can cancel the runs in bulk.

```python
workflow_run_ids = [workflow_run.metadata.id for workflow_run in workflow_runs.rows]

bulk_cancel_by_ids = BulkCancelReplayOpts(ids=workflow_run_ids)

hatchet.runs.bulk_cancel(bulk_cancel_by_ids)
```

> **Info:** Note that the Python SDK also exposes async versions of each of these methods:
>
>       - `workflows.list` -> `await workflows.aio_list`
>       - `runs.list` -> `await runs.aio_list`
>       - `runs.bulk_cancel` -> `await runs.aio_bulk_cancel`

#### Go

> **Info:** Just like in the Python SDK, the mechanics of bulk replaying and bulk
>   cancelling tasks are exactly the same.

First, we'll start by fetching a task via the REST API.

```python
from datetime import datetime, timedelta, timezone

from hatchet_sdk import BulkCancelReplayOpts, Hatchet, RunFilter, V1TaskStatus

hatchet = Hatchet()

workflows = hatchet.workflows.list()

assert workflows.rows

workflow = workflows.rows[0]
```

Now that we have a task, we'll get runs for it, so that we can use them to bulk cancel by run id.

```python
workflow_runs = hatchet.runs.list(workflow_ids=[workflow.metadata.id])
```

And finally, we can cancel the runs in bulk.

```python
workflow_run_ids = [workflow_run.metadata.id for workflow_run in workflow_runs.rows]

bulk_cancel_by_ids = BulkCancelReplayOpts(ids=workflow_run_ids)

hatchet.runs.bulk_cancel(bulk_cancel_by_ids)
```

#### Ruby

```ruby
hatchet = Hatchet::Client.new

workflows = hatchet.workflows.list

workflow = workflows.rows.first
```
```ruby
workflow_runs = hatchet.runs.list(workflow_ids: [workflow.metadata.id])
```
```ruby
workflow_run_ids = workflow_runs.rows.map { |run| run.metadata.id }

hatchet.runs.bulk_cancel(ids: workflow_run_ids)
```

### Bulk Operations by Filters

The second way to bulk cancel or replay runs is by providing a list of filters. This is the most powerful way to cancel or replay runs in bulk, as it allows you to cancel or replay all runs matching a set of arbitrary filters without needing to provide IDs for the runs in advance.

#### Python

The example below provides some filters you might use to cancel or replay runs in bulk. Importantly, these filters are very similar to the filters you can use in the Hatchet Dashboard to filter which task runs are displaying.

```python
bulk_cancel_by_filters = BulkCancelReplayOpts(
    filters=RunFilter(
        since=datetime.today() - timedelta(days=1),
        until=datetime.now(tz=timezone.utc),
        statuses=[V1TaskStatus.RUNNING],
        workflow_ids=[workflow.metadata.id],
        additional_metadata={"key": "value"},
    )
)

hatchet.runs.bulk_cancel(bulk_cancel_by_filters)
```

Running this request will cancel all task runs matching the filters provided.

#### Go

The example below provides some filters you might use to cancel or replay runs in bulk. Importantly, these filters are very similar to the filters you can use in the Hatchet Dashboard to filter which task runs are displaying.

```python
bulk_cancel_by_filters = BulkCancelReplayOpts(
    filters=RunFilter(
        since=datetime.today() - timedelta(days=1),
        until=datetime.now(tz=timezone.utc),
        statuses=[V1TaskStatus.RUNNING],
        workflow_ids=[workflow.metadata.id],
        additional_metadata={"key": "value"},
    )
)

hatchet.runs.bulk_cancel(bulk_cancel_by_filters)
```

Running this request will cancel all task runs matching the filters provided.

#### Ruby

```ruby
hatchet.runs.bulk_cancel(
  since: Time.now - 86_400,
  until_time: Time.now,
  statuses: ["RUNNING"],
  workflow_ids: [workflow.metadata.id],
  additional_metadata: { "key" => "value" }
)
```

# Manual Retries

Hatchet provides a manual retry mechanism that allows you to handle failed task instances flexibly from the Hatchet dashboard.

Navigate to the specific task in the Hatchet dashboard and click on the failed run. From there, you can inspect the details of the run, including the input data and the failure reason for each task.

To retry a failed task, simply click on the task in the run details view and then click the "Replay" button. This will create a new instance of the task, starting from the failed task, and using the same input data as the original run.

Manual retries give you full control over when and how to reprocess failed instances. For example, you may choose to wait until an external service is back online before retrying instances that depend on that service, or you may need to deploy a bug fix to your task code before retrying instances that were affected by the bug.

## A Note on Dead Letter Queues

A dead letter queue (DLQ) is a messaging concept used to handle messages that cannot be processed successfully. In the context of task management, a DLQ can be used to store failed task instances that require manual intervention or further analysis.

While Hatchet does not have a built-in dead letter queue feature, the persistence of failed task instances in the dashboard serves a similar purpose. By keeping a record of failed instances, Hatchet allows you to track and manage failures, perform root cause analysis, and take appropriate actions, such as modifying input data or updating your task code before manually retrying the failed instances.

It's important to note that the term "dead letter queue" is more commonly associated with messaging systems like Apache Kafka or Amazon SQS, where unprocessed messages are automatically moved to a separate queue for manual handling. In Hatchet, the failed instances are not automatically moved to a separate queue but are instead persisted in the dashboard for manual management.


---

<!-- Source: https://docs.hatchet.run/v1/concurrency -->

# Concurrency Control in Hatchet Tasks

Hatchet provides powerful concurrency control features to help you manage the execution of your tasks. This is particularly useful when you have tasks that may be triggered frequently or have long-running steps, and you want to limit the number of concurrent executions to prevent overloading your system, ensure fairness, or avoid race conditions.

> **Info:** Concurrency strategies can be added to both `Tasks` and `Workflows`.

### Why use concurrency control?

There are several reasons why you might want to use concurrency control in your Hatchet tasks:

1. **Fairness**: When you have multiple clients or users triggering tasks, concurrency control can help ensure fair access to resources. By limiting the number of concurrent runs per client or user, you can prevent a single client from monopolizing the system and ensure that all clients get a fair share of the available resources.

2. **Resource management**: If your task steps are resource-intensive (e.g., they make external API calls or perform heavy computations), running too many instances concurrently can overload your system. By limiting concurrency, you can ensure your system remains stable and responsive.

3. **Avoiding race conditions**: If your task steps modify shared resources, running multiple instances concurrently can lead to race conditions and inconsistent data. Concurrency control helps you avoid these issues by ensuring only a limited number of instances run at a time.

4. **Compliance with external service limits**: If your task steps interact with external services that have rate limits, concurrency control can help you stay within those limits and avoid being throttled or blocked.

5. **Spike Protection**: When you have tasks that are triggered by external events, such as webhooks or user actions, you may experience spikes in traffic that can overwhelm your system. Concurrency control can help you manage these spikes by limiting the number of concurrent runs and queuing new runs until resources become available.

### Available Strategies:

- [`GROUP_ROUND_ROBIN`](#group-round-robin): Distribute task instances across available slots in a round-robin fashion based on the `key` function.
- [`CANCEL_IN_PROGRESS`](#cancel-in-progress): Cancel the currently running task instances for the same concurrency key to free up slots for the new instance.
- [`CANCEL_NEWEST`](#cancel-newest): Cancel the newest task instance for the same concurrency key to free up slots for the new instance.

> We're always open to adding more strategies to fit your needs. Join our [discord](https://hatchet.run/discord) to let us know.

### Setting concurrency on workers

In addition to setting concurrency limits at the task level, you can also control concurrency at the worker level by passing the `slots` option when creating a new `Worker` instance:

#### Python

```python
class WorkflowInput(BaseModel):
    group: str


concurrency_limit_rr_workflow = hatchet.workflow(
    name="ConcurrencyDemoWorkflowRR",
    concurrency=ConcurrencyExpression(
        expression="input.group",
        max_runs=1,
        limit_strategy=ConcurrencyLimitStrategy.GROUP_ROUND_ROBIN,
    ),
    input_validator=WorkflowInput,
)
```

#### Typescript

```typescript
export const simpleConcurrency = hatchet.workflow({
  name: 'simple-concurrency',
  concurrency: {
    maxRuns: 1,
    limitStrategy: ConcurrencyLimitStrategy.GROUP_ROUND_ROBIN,
    expression: 'input.GroupKey',
  },
});
```

#### Go

```go
var maxRuns int32 = 1
strategy := types.GroupRoundRobin

return client.NewStandaloneTask("simple-concurrency",
	func(ctx worker.HatchetContext, input ConcurrencyInput) (*TransformedOutput, error) {
		// Random sleep between 200ms and 1000ms
		time.Sleep(time.Duration(200+rand.Intn(800)) * time.Millisecond)

		return &TransformedOutput{
			TransformedMessage: input.Message,
		}, nil
	},
	hatchet.WithWorkflowConcurrency(types.Concurrency{
		Expression:    "input.GroupKey",
		MaxRuns:       &maxRuns,
		LimitStrategy: &strategy,
	}),
)
```

#### Ruby

```ruby
CONCURRENCY_LIMIT_RR_WORKFLOW = HATCHET.workflow(
  name: "ConcurrencyDemoWorkflowRR",
  concurrency: Hatchet::ConcurrencyExpression.new(
    expression: "input.group",
    max_runs: 1,
    limit_strategy: :group_round_robin
  )
)

CONCURRENCY_LIMIT_RR_WORKFLOW.task(:step1) do |input, ctx|
  puts "starting step1"
  sleep 2
  puts "finished step1"
end
```

This example will only let 1 run in each group run at a given time to fairly distribute the load across the workers.

## Group Round Robin

### How it works

When a new task instance is triggered, the `GROUP_ROUND_ROBIN` strategy will:

1. Determine the group that the instance belongs to based on the `key` function defined in the task's concurrency configuration.
2. Check if there are any available slots for the instance's group based on the `slots` limit of available workers.
3. If a slot is available, the new task instance starts executing immediately.
4. If no slots are available, the new task instance is added to a queue for its group.
5. When a running task instance completes and a slot becomes available for a group, the next queued instance for that group (in round-robin order) is dequeued and starts executing.

This strategy ensures that task instances are processed fairly across different groups, preventing any one group from monopolizing the available resources. It also helps to reduce latency for instances within each group, as they are processed in a round-robin fashion rather than strictly in the order they were triggered.

### When to use `GROUP_ROUND_ROBIN`

The `GROUP_ROUND_ROBIN` strategy is particularly useful in scenarios where:

- You have multiple clients or users triggering task instances, and you want to ensure fair resource allocation among them.
- You want to process instances within each group in a round-robin fashion to minimize latency and ensure that no single instance within a group is starved for resources.
- You have long-running task instances and want to avoid one group's instances monopolizing the available slots.

Keep in mind that the `GROUP_ROUND_ROBIN` strategy may not be suitable for all use cases, especially those that require strict ordering or prioritization of the most recent events.

## Cancel In Progress

### How it works

When a new task instance is triggered, the `CANCEL_IN_PROGRESS` strategy will:

1. Determine the group that the instance belongs to based on the `key` function defined in the task's concurrency configuration.
2. Check if there are any available slots for the instance's group based on the `maxRuns` limit of available workers.
3. If a slot is available, the new task instance starts executing immediately.
4. If there are no available slots, currently running task instances for the same concurrency key are cancelled to free up slots for the new instance.
5. The new task instance starts executing immediately.

### When to use Cancel In Progress

The `CANCEL_IN_PROGRESS` strategy is particularly useful in scenarios where:

- You have long-running task instances that may become stale or irrelevant if newer instances are triggered.
- You want to prioritize processing the most recent data or events, even if it means canceling older task instances.
- You have resource-intensive tasks where it's more efficient to cancel an in-progress instance and start a new one than to wait for the old instance to complete.
- Your user UI allows for multiple inputs, but only the most recent is relevant (i.e. chat messages, form submissions, etc.).

## Cancel Newest

### How it works

The `CANCEL_NEWEST` strategy is similar to `CANCEL_IN_PROGRESS`, but it cancels the newly enqueued run instead of the oldest.

### When to use `CANCEL_NEWEST`

The `CANCEL_NEWEST` strategy is particularly useful in scenarios where:

- You want to allow in progress runs to complete before starting new work.
- You have long-running task instances and want to avoid one group's instances monopolizing the available slots.

## Multiple concurrency strategies

You can also combine multiple concurrency strategies to create a more complex concurrency control system. For example, you can use one group key to represent a specific team, and another group to represent a specific resource in that team, giving you more control over the rate at which tasks are executed.

#### Python

```python
class WorkflowInput(BaseModel):
    name: str
    digit: str


concurrency_workflow_level_workflow = hatchet.workflow(
    name="ConcurrencyWorkflowLevel",
    input_validator=WorkflowInput,
    concurrency=[
        ConcurrencyExpression(
            expression="input.digit",
            max_runs=DIGIT_MAX_RUNS,
            limit_strategy=ConcurrencyLimitStrategy.GROUP_ROUND_ROBIN,
        ),
        ConcurrencyExpression(
            expression="input.name",
            max_runs=NAME_MAX_RUNS,
            limit_strategy=ConcurrencyLimitStrategy.GROUP_ROUND_ROBIN,
        ),
    ],
)
```

#### Typescript

```typescript
export const multipleConcurrencyKeys = hatchet.workflow({
  name: 'simple-concurrency',
  concurrency: [
    {
      maxRuns: 1,
      limitStrategy: ConcurrencyLimitStrategy.GROUP_ROUND_ROBIN,
      expression: 'input.Tier',
    },
    {
      maxRuns: 1,
      limitStrategy: ConcurrencyLimitStrategy.GROUP_ROUND_ROBIN,
      expression: 'input.Account',
    },
  ],
});
```

#### Go

```go
strategy := types.GroupRoundRobin
var maxRuns int32 = 20

return client.NewStandaloneTask("multi-concurrency",
	func(ctx worker.HatchetContext, input ConcurrencyInput) (*TransformedOutput, error) {
		// Random sleep between 200ms and 1000ms
		time.Sleep(time.Duration(200+rand.Intn(800)) * time.Millisecond)

		return &TransformedOutput{
			TransformedMessage: input.Message,
		}, nil
	},
	hatchet.WithWorkflowConcurrency(
		types.Concurrency{
			Expression:    "input.Tier",
			MaxRuns:       &maxRuns,
			LimitStrategy: &strategy,
		}, types.Concurrency{
			Expression:    "input.Account",
			MaxRuns:       &maxRuns,
			LimitStrategy: &strategy,
		},
	),
)
```

#### Ruby

```ruby
CONCURRENCY_WORKFLOW_LEVEL_WORKFLOW = HATCHET.workflow(
  name: "ConcurrencyWorkflowLevel",
  concurrency: [
    Hatchet::ConcurrencyExpression.new(
      expression: "input.digit",
      max_runs: DIGIT_MAX_RUNS_WL,
      limit_strategy: :group_round_robin
    ),
    Hatchet::ConcurrencyExpression.new(
      expression: "input.name",
      max_runs: NAME_MAX_RUNS_WL,
      limit_strategy: :group_round_robin
    )
  ]
)

CONCURRENCY_WORKFLOW_LEVEL_WORKFLOW.task(:task_1) do |input, ctx|
  sleep SLEEP_TIME_WL
end

CONCURRENCY_WORKFLOW_LEVEL_WORKFLOW.task(:task_2) do |input, ctx|
  sleep SLEEP_TIME_WL
end
```


---

<!-- Source: https://docs.hatchet.run/v1/rate-limits -->

# Rate Limiting Step Runs in Hatchet

Hatchet allows you to enforce rate limits on task runs, enabling you to control the rate at which your service runs consume resources, such as external API calls, database queries, or other services. By defining rate limits, you can prevent task runs from exceeding a certain number of requests per time window (e.g., per second, minute, or hour), ensuring efficient resource utilization and avoiding overloading external services.

The state of active rate limits can be viewed in the dashboard in the `Rate Limit` resource tab.

## Dynamic vs Static Rate Limits

Hatchet offers two patterns for Rate Limiting task runs:

1. [Dynamic Rate Limits](#dynamic-rate-limits): Allows for complex rate limiting scenarios, such as per-user limits, by using `input` or `additional_metadata` keys to upsert a limit at runtime.
2. [Static Rate Limits](#static-rate-limits): Allows for simple rate limiting for resources known prior to runtime (e.g., external APIs).

## Dynamic Rate Limits

Dynamic rate limits are ideal for complex scenarios where rate limits need to be partitioned by resources that are only known at runtime.

This pattern is especially useful for:

1. Rate limiting individual users or tenants
2. Implementing variable rate limits based on subscription tiers or user roles
3. Dynamically adjusting limits based on real-time system load or other factors

### How It Works

1. Define the dynamic rate limit key with a CEL (Common Expression Language) Expression on the key, referencing either `input` or `additional_metadata`.
2. Provide this key as part of the workflow trigger or event `input` or `additional_metadata` at runtime.
3. Hatchet will create or update the rate limit based on the provided key and enforce it for the step run.

> **Info:** Note: Dynamic keys are a shared resource, this means the same rendered cel on
>   multiple steps will be treated as one global rate limit.

### Declaring and Consuming Dynamic Rate Limits

#### Ruby

> Note: `dynamic_key` must be a CEL expression. `units` and `limits` can be either an integer or a CEL expression.

We can add one or more rate limits to a task by adding the `rate_limits` configuration to the task definition.

```python
@rate_limit_workflow.task(
    rate_limits=[
        RateLimit(
            dynamic_key="input.user_id",
            units=1,
            limit=10,
            duration=RateLimitDuration.MINUTE,
        )
    ]
)
def step_2(input: RateLimitInput, ctx: Context) -> None:
    print("executed step_2")
```

#### Tab 2

> Note: `dynamicKey` must be a CEL expression. `units` and `limit` can be either an integer or a CEL expression.

We can add one or more rate limits to a task by adding the `rate_limits` configuration to the task definition.

```typescript
const task2 = hatchet.task({
  name: 'task2',
  fn: (input: { userId: string }) => {
    console.log('executed task2 for user: ', input.userId);
  },
  rateLimits: [
    {
      dynamicKey: 'input.userId',
      units: 1,
      limit: 10,
      duration: RateLimitDuration.MINUTE,
    },
  ],
});
```

#### Tab 3

> Note: Go requires both a key and KeyExpr be set and the LimitValueExpr must be a CEL.

```go
userUnits := 1
userLimit := "10"
duration := types.Minute
dynamicTask := client.NewStandaloneTask("task2",
	func(ctx hatchet.Context, input APIRequest) (string, error) {
		log.Printf("executed task2 for user: %s", input.UserID)

		return "completed", nil
	},
	hatchet.WithRateLimits(&types.RateLimit{
		Key:            "input.userId",
		Units:          &userUnits,
		LimitValueExpr: &userLimit,
		Duration:       &duration,
	}),
)
```

#### Tab 4

```ruby
RATE_LIMIT_WORKFLOW.task(
  :step_2,
  rate_limits: [
    Hatchet::RateLimit.new(
      dynamic_key: "input.user_id",
      units: 1,
      limit: 10,
      duration: :minute
    )
  ]
) do |input, ctx|
  puts "executed step_2"
end
```

## Static Rate Limits

Static Rate Limits (formerly known as Global Rate Limits) are defined as part of your worker startup lifecycle prior to runtime. This model provides a single "source of truth" for pre-defined resources such as:

1. External API resources that have a rate limit across all users or tenants
2. Database connection pools with a maximum number of concurrent connections
3. Shared computing resources with limited capacity

### How It Works

1. Declare static rate limits using the `put_rate_limit` method in the `Admin` client before starting your worker.
2. Specify the units of consumption for a specific rate limit key in each step definition using the `rate_limits` configuration.
3. Hatchet enforces the defined rate limits by tracking the number of units consumed by each step run across all workflow runs.

If a step run exceeds the rate limit, Hatchet re-queues the step run until the rate limit is no longer exceeded.

### Declaring Static Limits

Define the static rate limits that can be consumed by any step run across all workflow runs using the `put_rate_limit` method in the `Admin` client within your code.

#### Ruby

```python
RATE_LIMIT_KEY = "test-limit"

hatchet.rate_limits.put(RATE_LIMIT_KEY, 2, RateLimitDuration.SECOND)
```

#### Tab 2

{" "}

```typescript
hatchet.ratelimits.upsert({
  key: 'api-service-rate-limit',
  limit: 10,
  duration: RateLimitDuration.SECOND,
});
```

#### Tab 3

```go
err = client.RateLimits().Upsert(features.CreateRatelimitOpts{
	Key:      RATE_LIMIT_KEY,
	Limit:    10,
	Duration: types.Second,
})
if err != nil {
	log.Fatalf("failed to create rate limit: %v", err)
}
```

#### Tab 4

```ruby
def main
  HATCHET.rate_limits.put(RATE_LIMIT_KEY, 2, :second)

  worker = HATCHET.worker(
    "rate-limit-worker", slots: 10, workflows: [RATE_LIMIT_WORKFLOW]
  )
  worker.start
end
```

### Consuming Static Rate Limits

With your rate limit key defined, specify the units of consumption for a specific key in each step definition by adding the `rate_limits` configuration to your step definition in your workflow.

#### Ruby

```python
RATE_LIMIT_KEY = "test-limit"


@rate_limit_workflow.task(rate_limits=[RateLimit(static_key=RATE_LIMIT_KEY, units=1)])
def step_1(input: RateLimitInput, ctx: Context) -> None:
    print("executed step_1")
```

#### Tab 2

```typescript
const RATE_LIMIT_KEY = 'api-service-rate-limit';

const task1 = hatchet.task({
  name: 'task1',
  rateLimits: [
    {
      staticKey: RATE_LIMIT_KEY,
      units: 1,
    },
  ],
  fn: (input) => {
    console.log('executed task1');
  },
});
```

#### Tab 3

```go
units := 1
staticTask := client.NewStandaloneTask("task1",
	func(ctx hatchet.Context, input APIRequest) (string, error) {
		log.Println("executed task1")

		return "completed", nil
	},
	hatchet.WithRateLimits(&types.RateLimit{
		Key:   RATE_LIMIT_KEY,
		Units: &units,
	}),
)
```

#### Tab 4

```ruby
RATE_LIMIT_KEY = "test-limit"

RATE_LIMIT_WORKFLOW.task(
  :step_1,
  rate_limits: [Hatchet::RateLimit.new(static_key: RATE_LIMIT_KEY, units: 1)]
) do |input, ctx|
  puts "executed step_1"
end
```

### Limiting Workflow Runs

To rate limit an entire workflow run, it's recommended to specify the rate limit configuration on the entry step (i.e., the first step in the workflow). This will gate the execution of all downstream steps in the workflow.


---

<!-- Source: https://docs.hatchet.run/v1/priority -->

# Assigning priority to tasks in Hatchet

Hatchet allows you to assign different `priority` values to your tasks depending on how soon you want them to run. `priority` can be set to either `1`, `2`, or `3`, (`low`, `medium`, and `high`, respectively) with relatively higher values resulting in that task being picked up before others of the same type. **By default, runs in Hatchet have a priority of 1 (low) unless otherwise specified.**


Priority only affects multiple runs of a _single_ workflow. If you have two different workflows (A and B) and set A to globally have a priority of 3, and B to globally have a priority of 1, this does _not_ guarantee that if there is one task from A and one from B in the queue, that A's task will be run first.

However, _within_ A, if you enqueue one task with priority 3 and one with priority 1, the priority 3 task will be run first.


A couple of common use cases for assigning priorities are things like:

1. Having high-priority (e.g. paying, new, etc.) customers be prioritized over lower-priority ones, allowing them to get faster turnaround times on their tasks.
2. Having tasks triggered via your API run with higher priority than the same tasks triggered by a cron.

## Setting priority for a task or workflow

There are a few different ways to set priorities for tasks or workflows in Hatchet.

### Workflow-level default priority

First, you can set a default priority at the workflow level:

#### Ruby

```python
DEFAULT_PRIORITY = 1
SLEEP_TIME = 0.25

priority_workflow = hatchet.workflow(
    name="PriorityWorkflow",
    default_priority=DEFAULT_PRIORITY,
)
```

#### Tab 2

```typescript
export const priorityWf = hatchet.workflow({
  name: 'priority-wf',
  defaultPriority: Priority.LOW,
});
```

#### Tab 3

```go
workflow := client.NewWorkflow(
	"priority",
	hatchet.WithWorkflowDefaultPriority(features.RunPriorityLow),
)
```

#### Tab 4

```ruby
DEFAULT_PRIORITY = 1
SLEEP_TIME = 0.25

PRIORITY_WORKFLOW = HATCHET.workflow(
  name: "PriorityWorkflow",
  default_priority: DEFAULT_PRIORITY
)

PRIORITY_WORKFLOW.task(:priority_task) do |input, ctx|
  puts "Priority: #{ctx.priority}"
  sleep SLEEP_TIME
end
```

This will assign the same default priority to all runs of this workflow (and all of the workflow's corresponding tasks), but will have no effect without also setting run-level priorities, since every run will use the same default.

### Priority-on-trigger

When you trigger a run, you can set the priority of the triggered run to override its default priority.

#### Ruby

```python
low_prio = priority_workflow.run_no_wait(
    options=TriggerWorkflowOptions(
        ## 👀 Adding priority and key to metadata to show them in the dashboard
        priority=1,
        additional_metadata={"priority": "low", "key": 1},
    )
)

high_prio = priority_workflow.run_no_wait(
    options=TriggerWorkflowOptions(
        ## 👀 Adding priority and key to metadata to show them in the dashboard
        priority=3,
        additional_metadata={"priority": "high", "key": 1},
    )
)
```

#### Tab 2

```typescript
const run = priority.run(new Date(Date.now() + 60 * 60 * 1000), { priority: Priority.HIGH });
```

#### Tab 3

```go
ref, err := client.RunNoWait(
	context.Background(),
	workflow.GetName(),
	PriorityInput{},
	hatchet.WithRunPriority(features.RunPriorityLow),
)
if err != nil {
	return err
}
```

#### Tab 4

```ruby
low_prio = PRIORITY_WORKFLOW.run_no_wait(
  {},
  options: Hatchet::TriggerWorkflowOptions.new(
    priority: 1,
    additional_metadata: { "priority" => "low", "key" => 1 }
  )
)

high_prio = PRIORITY_WORKFLOW.run_no_wait(
  {},
  options: Hatchet::TriggerWorkflowOptions.new(
    priority: 3,
    additional_metadata: { "priority" => "high", "key" => 1 }
  )
)
```

Similarly, you can also assign a priority to scheduled and cron workflows.

#### Ruby

```python
schedule = priority_workflow.schedule(
    run_at=datetime.now(tz=timezone.utc) + timedelta(minutes=1),
    options=ScheduleTriggerWorkflowOptions(priority=3),
)

cron = priority_workflow.create_cron(
    cron_name="my-scheduled-cron",
    expression="0 * * * *",
    priority=3,
)
```

#### Tab 2

```typescript
const scheduled = priority.schedule(
  new Date(Date.now() + 60 * 60 * 1000),
  {},
  { priority: Priority.HIGH }
);
const delayed = priority.delay(60 * 60 * 1000, {}, { priority: Priority.HIGH });
const cron = priority.cron(
  `daily-cron-${Math.random()}`,
  '0 0 * * *',
  {},
  { priority: Priority.HIGH }
);
```

#### Tab 3

```go
priority := features.RunPriorityHigh

schedule, err := client.Schedules().Create(
	context.Background(),
	workflow.GetName(),
	features.CreateScheduledRunTrigger{
		Priority: &priority,
	},
)
if err != nil {
	return err
}

cron, err := client.Crons().Create(
	context.Background(),
	workflow.GetName(),
	features.CreateCronTrigger{
		Priority: &priority,
	},
)
if err != nil {
	return err
}
```

#### Tab 4

```ruby
schedule = PRIORITY_WORKFLOW.schedule(
  Time.now + 60,
  options: Hatchet::TriggerWorkflowOptions.new(priority: 3)
)

cron = PRIORITY_WORKFLOW.create_cron(
  "my-scheduled-cron",
  "0 * * * *",
  input: {},
)
```

In these cases, the priority set on the trigger will override the default priority, so these runs will be processed ahead of lower-priority ones.


---

<!-- Source: https://docs.hatchet.run/v1/patterns/durable-task-execution -->

# Durable Tasks

Use durable tasks when **you don't know the shape of work ahead of time**. For example, an AI agent that picks its next action based on a model response, a fan-out where N is determined by the input data, or a pipeline that branches and spawns sub-workflows based on intermediate results. In all of these cases, the "graph" of work doesn't exist when the task starts; it emerges at runtime as the task makes decisions and [spawns children](/v1/child-spawning).

A durable task is a single long-running function that acts as an **orchestrator**: it spawns child tasks, waits for their results, makes decisions, and spawns more. Hatchet checkpoints its progress so it can recover from crashes, survive long waits, and resume on any worker without re-executing completed work.

> **Info:** If you know the full graph of work upfront (every task and dependency is fixed
>   before execution begins), use a [DAG](/v1/patterns/directed-acyclic-graphs)
>   instead. You can always [mix both patterns](/v1/patterns/mixing-patterns) in
>   the same application.

## When to Use Durable Tasks

| Scenario                          | Why Durable?                                                                                                                                                                            |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Dynamic fan-out** (N unknown)   | Spawn children based on runtime data; wait for results without holding a slot. See [Batch Processing](/guides/batch-processing) and [Document Processing](/guides/document-processing). |
| **Agentic workflows**             | An agent decides what to do next, spawns subtasks, loops, or stops at runtime. See [AI Agents](/guides/ai-agents/reasoning-loop).                                                       |
| **Long waits** (hours/days)       | Worker slots are freed during waits; no wasted compute.                                                                                                                                 |
| **Human-in-the-loop**             | Wait for approval events without holding resources. See [Human-in-the-Loop](/guides/human-in-the-loop).                                                                                 |
| **Multi-step with inline pauses** | `SleepFor` and `WaitForEvent` let you express complex procedural flows.                                                                                                                 |
| **Crash-resilient pipelines**     | Automatically resume from checkpoints after failures.                                                                                                                                   |

## How It Works

A durable task builds the workflow at runtime through **child spawning**. The task function runs, inspects data, and decides what to do next by spawning child tasks. The parent is [evicted](/v1/task-eviction) while children execute, freeing its worker slot. When children complete, the parent resumes from its checkpoint and continues.

```mermaid
sequenceDiagram
    participant P as Durable Task
    participant H as Hatchet
    participant W as Workers

    P->>H: Spawn Child A, Child B, Child C...N
    H-->>P: Evicted (slot freed)
    H->>W: Schedule children across fleet
    W->>H: Child results
    H->>P: Resume from checkpoint
    P->>P: Inspect results, decide next step
    P->>H: Spawn more children, sleep, or finish
```

This is fundamentally different from a DAG, where every task and dependency is declared before execution begins. With durable tasks, the number of children, which branches to take, and whether to loop or stop are all determined by your code at runtime.


### Checkpoints

Each call to `SleepFor`, `WaitForEvent`, `WaitFor`, `Memo`, or `RunChild` creates a checkpoint in the durable event log. These checkpoints record the task's progress.

### Worker slot is freed during waits

When a durable task enters a wait (sleep, event, or child result), Hatchet [evicts](/v1/task-eviction) it from the worker. The slot is immediately available for other tasks.

### Task resumes from checkpoint

When the wait completes, Hatchet re-queues the task on any available worker. It replays the event log up to the last checkpoint and resumes execution from there. Completed operations are not re-executed.


## The Durable Context

Declare a task as durable (using `durable_task` instead of `task`) and it receives a `DurableContext` instead of a normal `Context`. The `DurableContext` extends `Context` with methods for checkpointing and waiting:

| Method                        | Purpose                                                                                                                                                                        |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`SleepFor(duration)`**      | Pause for a fixed duration. Respects the original sleep time on restart; if interrupted after 23 of 24 hours, only sleeps 1 more hour.                                         |
| **`WaitForEvent(key, expr)`** | Wait for an external event by key, with optional [CEL filter](https://github.com/google/cel-spec) expression on the payload.                                                   |
| **`WaitFor(conditions)`**     | General-purpose wait accepting any combination of sleep conditions, event conditions, or or-groups. `SleepFor` and `WaitForEvent` are convenience wrappers around this method. |
| **`Memo(function)`**          | Run functions whose outputs are memoized based on the input arguments.                                                                                                         |
| **`RunChild(task, input)`**   | Spawn a child task and wait for its result. The parent is evicted during the wait.                                                                                             |

## Example Task

```python
durable_workflow = hatchet.workflow(name="DurableWorkflow")
```

Now add tasks to the workflow. The first is a regular task; the second is a durable task that sleeps and waits for an event:

```python
EVENT_KEY = "durable-example:event"
SLEEP_TIME = 5


@durable_workflow.task()
async def ephemeral_task(input: EmptyModel, ctx: Context) -> None:
    print("Running non-durable task")


@durable_workflow.durable_task()
async def durable_task(input: EmptyModel, ctx: DurableContext) -> dict[str, str]:
    print("Waiting for sleep")
    await ctx.aio_sleep_for(duration=timedelta(seconds=SLEEP_TIME))
    print("Sleep finished")

    print("Waiting for event")
    await ctx.aio_wait_for(
        "event",
        UserEventCondition(event_key=EVENT_KEY, expression="true"),
    )
    print("Event received")

    return {
        "status": "success",
    }
```

> **Info:** The `durable_task` decorator gives the function a `DurableContext` instead of
>   a regular `Context`. This is the only difference in declaration; the task
>   registers and runs on the same worker as regular tasks.

If this task is interrupted at any time, it will continue from where it left off. If the task calls `ctx.aio_sleep_for` for 24 hours and is interrupted after 23 hours, it will only sleep for 1 more hour on restart.

### Or Groups

Durable tasks can combine multiple wait conditions using [or groups](/v1/conditions#or-groups). For example, you could wait for either an event or a sleep (whichever comes first):

```python
@durable_workflow.durable_task()
async def wait_for_or_group_1(
    _i: EmptyModel, ctx: DurableContext
) -> dict[str, str | int]:
    start = time.time()
    wait_result = await ctx.aio_wait_for(
        uuid4().hex,
        or_(
            SleepCondition(timedelta(seconds=SLEEP_TIME)),
            UserEventCondition(event_key=EVENT_KEY),
        ),
    )

    key = list(wait_result.keys())[0]
    event_id = list(wait_result[key].keys())[0]

    return {
        "runtime": int(time.time() - start),
        "key": key,
        "event_id": event_id,
    }
```

## Spawning Child Tasks

Child spawning is the primary way durable tasks build workflows at runtime. A durable task can spawn any runnable (regular tasks, other durable tasks, or entire DAG workflows), wait for results, and decide what to do next.

| Child type       | Example                                                                           |
| ---------------- | --------------------------------------------------------------------------------- |
| **Regular task** | Spawn a stateless task for a quick computation or API call.                       |
| **Durable task** | Spawn another durable task that has its own checkpoints, sleeps, and event waits. |
| **DAG workflow** | Spawn an entire multi-task workflow and wait for its final output.                |

The parent is evicted while children execute, so it consumes no resources. The number and type of children can be determined dynamically based on input, intermediate results, or model outputs.

See [Child Spawning](/v1/child-spawning) for patterns and full examples.

> **Info:** For an in-depth look at how durable execution works internally, see [this blog
>   post](https://hatchet.run/blog/durable-execution).


---

<!-- Source: https://docs.hatchet.run/v1/patterns/directed-acyclic-graphs -->

# Declarative Workflow Design (DAGs)

Hatchet workflows are designed in a **Directed Acyclic Graph (DAG)** format, where each task is a node in the graph, and the dependencies between tasks are the edges. This structure ensures that workflows are organized, predictable, and free from circular dependencies.


## How DAG Workflows Work


### You declare the graph

Define tasks and their dependencies upfront. Hatchet knows the full shape of work before execution begins.

### Hatchet executes in order

Tasks run as soon as their parents complete. Independent tasks run in parallel automatically. A worker slot is only assigned when a task is ready to execute, so tasks waiting on parents consume no resources. Each task has configurable [retry policies](/v1/retry-policies) and [timeouts](/v1/timeouts).

### Results flow downstream

Task outputs are cached and passed to child tasks. If a failure occurs mid-workflow, completed tasks don't re-run.

### Everything is observable

Every task execution is tracked in the dashboard — inputs, outputs, durations, and errors. You can see exactly where a workflow succeeded or failed.


## Defining a Workflow

Start by declaring a workflow with a name. The workflow object can declare additional workflow-level configuration options which we'll cover later.

The returned object is an instance of the `Workflow` class, which is the primary interface for interacting with the workflow (i.e. [running](/v1/running-your-task#run-and-wait), [enqueuing](/v1/running-your-task#fire-and-forget), [scheduling](/v1/scheduled-runs), etc).

#### Python

```python
dag_workflow = hatchet.workflow(name="DAGWorkflow")
```

#### Typescript

```typescript
// First, we declare the workflow
export const dag = hatchet.workflow({
  name: 'simple',
});
```

#### Go

```go
workflow := client.NewWorkflow("dag-workflow")
```

#### Ruby

```ruby
DAG_WORKFLOW = HATCHET.workflow(name: "DAGWorkflow")
```


  The Workflow return object can be interacted with in the same way as a
  [task](/v1/tasks), however, it can only take a subset of options which are
  applied at the task level.


## Defining a Task

Now that we have a workflow, we can define a task to be executed as part of the workflow. Tasks are defined by calling the `task` method on the workflow object.

The `task` method takes a name and a function that defines the task's behavior. The function will receive the workflow's input and return the task's output. Tasks also accept a number of other configuration options, which are covered elsewhere in our documentation.

#### Python

In Python, the `task` method is a decorator, which is used like this to wrap a function:

```python
@dag_workflow.task(execution_timeout=timedelta(seconds=5))
def step1(input: EmptyModel, ctx: Context) -> StepOutput:
    return StepOutput(random_number=random.randint(1, 100))
```

The function takes two arguments: `input`, which is a Pydantic model, and `ctx`, which is the Hatchet `Context` object. We'll discuss both of these more later.

> **Info:** In the internals of Hatchet, the task is called using _positional arguments_, meaning that you can name `input` and `ctx` whatever you like.
>
> For instance, `def task_1(foo: EmptyModel, bar: Context) -> None:` is perfectly valid.

#### Typescript

```typescript
// Next, we declare the tasks bound to the workflow
const toLower = dag.task({
  name: 'to-lower',
  fn: (input) => {
    return {
      TransformedMessage: input.Message.toLowerCase(),
    };
  },
});
```

The `fn` argument is a function that takes the workflow's input and a
context object. The context object contains information about the workflow
run (e.g. the run ID, the workflow's input, etc). It can be synchronous or
asynchronous.

#### Go

```go
step1 := workflow.NewTask("step-1", func(ctx hatchet.Context, input Input) (StepOutput, error) {
	return StepOutput{
		Step:   1,
		Result: input.Value * 2,
	}, nil
})
```

#### Ruby

```ruby
STEP1 = DAG_WORKFLOW.task(:step1, execution_timeout: 5) do |input, ctx|
  { "random_number" => rand(1..100) }
end

STEP2 = DAG_WORKFLOW.task(:step2, execution_timeout: 5) do |input, ctx|
  { "random_number" => rand(1..100) }
end
```

## Building a DAG with Task Dependencies

The power of Hatchet's workflow design comes from connecting tasks into a DAG structure. Tasks can specify dependencies (parents) which must complete successfully before the task can start.

#### Python

```python
@dag_workflow.task(execution_timeout=timedelta(seconds=5))
async def step2(input: EmptyModel, ctx: Context) -> StepOutput:
    return StepOutput(random_number=random.randint(1, 100))


@dag_workflow.task(parents=[step1, step2])
async def step3(input: EmptyModel, ctx: Context) -> RandomSum:
    one = ctx.task_output(step1).random_number
    two = ctx.task_output(step2).random_number

    return RandomSum(sum=one + two)
```

#### Typescript

```typescript
dag.task({
  name: 'reverse',
  parents: [toLower],
  fn: async (input, ctx) => {
    const lower = await ctx.parentOutput(toLower);
    return {
      Original: input.Message,
      Transformed: lower.TransformedMessage.split('').reverse().join(''),
    };
  },
});
```

#### Go

```go
step2 := workflow.NewTask("step-2", func(ctx hatchet.Context, input Input) (StepOutput, error) {
	// Get output from step 1
	var step1Output StepOutput
	if err := ctx.ParentOutput(step1, &step1Output); err != nil {
		return StepOutput{}, err
	}

	return StepOutput{
		Step:   2,
		Result: step1Output.Result + 10,
	}, nil
}, hatchet.WithParents(step1))
```

#### Ruby

```ruby
DAG_WORKFLOW.task(:step3, parents: [STEP1, STEP2]) do |input, ctx|
  one = ctx.task_output(STEP1)["random_number"]
  two = ctx.task_output(STEP2)["random_number"]

  { "sum" => one + two }
end

DAG_WORKFLOW.task(:step4, parents: [STEP1, :step3]) do |input, ctx|
  puts(
    "executed step4",
    Time.now.strftime("%H:%M:%S"),
    input.inspect,
    ctx.task_output(STEP1).inspect,
    ctx.task_output(:step3).inspect
  )

  { "step4" => "step4" }
end
```

## Accessing Parent Task Outputs

As shown in the examples above, tasks can access outputs from their parent tasks using the context object:

#### Python

```python
@dag_workflow.task(execution_timeout=timedelta(seconds=5))
async def step2(input: EmptyModel, ctx: Context) -> StepOutput:
    return StepOutput(random_number=random.randint(1, 100))


@dag_workflow.task(parents=[step1, step2])
async def step3(input: EmptyModel, ctx: Context) -> RandomSum:
    one = ctx.task_output(step1).random_number
    two = ctx.task_output(step2).random_number

    return RandomSum(sum=one + two)
```

#### Typescript

```typescript
dag.task({
  name: 'task-with-parent-output',
  parents: [toLower],
  fn: async (input, ctx) => {
    const lower = await ctx.parentOutput(toLower);
    return {
      Original: input.Message,
      Transformed: lower.TransformedMessage.split('').reverse().join(''),
    };
  },
});
```

#### Go

```go
// Inside a task with parent dependencies
var parentOutput ParentOutputType
err := ctx.ParentOutput(parentTask, &parentOutput)
if err != nil {
    return nil, err
}
```

#### Ruby

```ruby
DAG_WORKFLOW.task(:step3, parents: [STEP1, STEP2]) do |input, ctx|
  one = ctx.task_output(STEP1)["random_number"]
  two = ctx.task_output(STEP2)["random_number"]

  { "sum" => one + two }
end

DAG_WORKFLOW.task(:step4, parents: [STEP1, :step3]) do |input, ctx|
  puts(
    "executed step4",
    Time.now.strftime("%H:%M:%S"),
    input.inspect,
    ctx.task_output(STEP1).inspect,
    ctx.task_output(:step3).inspect
  )

  { "step4" => "step4" }
end
```

## Running a Workflow

You can run workflows directly or enqueue them for asynchronous execution. All the same methods for running a task are available for workflows!

#### Python

```python
dag_workflow.run()
```

#### Typescript

```typescript
const input = { Message: 'Hello, World!' };

// Run workflow and wait for the result
const result = await simple.run(input);

// Enqueue workflow to be executed asynchronously
const runReference = await simple.runNoWait(input);
```

#### Go

```go
// Run workflow and wait for the result
result, err := simple.Run(ctx, input)

// Enqueue workflow to be executed asynchronously
runID, err := simple.RunNoWait(ctx, input)
```

#### Ruby

```ruby
result = DAG_WORKFLOW.run
puts result
```

## Pre-Determined Pipelines

DAGs naturally model fixed multi-stage pipelines where the sequence of tasks and their dependencies are known before execution. ETL workflows, [document processing](/guides/document-processing) pipelines, and CI/CD workflows all follow this pattern: each stage depends on the previous, and the overall structure is visible and predictable in the dashboard.


---

<!-- Source: https://docs.hatchet.run/v1/patterns/mixing-patterns -->

# Best Practices

## Choosing a Pattern

Use a **DAG** for any portion of work whose shape you know upfront, and use a **durable task** to orchestrate the parts whose shape is dynamic. You can mix them freely within the same application and even within the same workflow.

| Scenario                                       | Pattern                                      |
| ---------------------------------------------- | -------------------------------------------- |
| Fixed pipeline, every step is known            | DAG                                          |
| Fixed pipeline, but one step needs a long wait | DAG with a durable task node                 |
| Dynamic orchestration of known pipelines       | Durable task spawning DAGs                   |
| Fully dynamic, shape decided at runtime        | Durable task spawning tasks/durable tasks    |
| Agent that reasons and acts in a loop          | Durable task spawning children per iteration |

[DAGs](/v1/patterns/directed-acyclic-graphs) are inherently deterministic, since their shape is predefined and intermediate results are cached. If your workflow can be represented as a DAG, prefer that. Reach for a durable task only when you need capabilities a static graph can't express.

> **Info:** You don't have to choose one pattern for your entire application. Different
>   workflows can use different patterns, and a single workflow can mix them.
>   Start with the simplest pattern that fits and add complexity only when needed.

## Mixing Patterns

### A durable task inside a DAG

A DAG workflow can include a durable task as one of its nodes. The durable task checkpoints and waits like any other, while the rest of the DAG proceeds according to its declared dependencies.

This is useful when most of your pipeline is a fixed graph but one step needs dynamic behavior, for example a pipeline where one stage runs an agentic loop that decides what to do at runtime.

```mermaid
graph LR
    A[Prepare Data] --> B[Durable: Agentic Loop]
    B --> C[Publish Results]
    style B stroke:#3392FF,stroke-dasharray: 5 5
```

The durable task (`Agentic Loop`) can spawn children, sleep, wait for events, or loop until a condition is met. When it completes, the downstream `Publish Results` task runs automatically.

### Spawning a DAG from a durable task

A durable task can spawn an entire DAG workflow as a child, wait for its result, and then continue. This lets you use procedural control flow to decide _which_ pipeline to run and _how many times_ to run it, while the pipeline itself is a well-defined graph.

```mermaid
graph TD
    DT[Durable Task] -->|spawns| DAG1[DAG: Process Batch 1]
    DT -->|spawns| DAG2[DAG: Process Batch 2]
    DT -->|spawns| DAG3[DAG: Process Batch N]
    DAG1 -->|result| DT
    DAG2 -->|result| DT
    DAG3 -->|result| DT
    style DT stroke:#3392FF
    style DAG1 stroke:#22C55E
    style DAG2 stroke:#22C55E
    style DAG3 stroke:#22C55E
```

The durable task decides at runtime how many batches to process, spawns a DAG workflow for each one, and collects the results. The DAG workflows run in parallel across your worker fleet while the durable task's slot is freed.

### Durable tasks spawning durable tasks

A durable task can spawn other durable tasks as children, each with their own checkpoints and event waits. This creates a tree of durable work that's entirely driven by runtime logic.

```mermaid
graph TD
    Root[Durable: Orchestrator] -->|spawns| A[Durable: Agent A]
    Root -->|spawns| B[Durable: Agent B]
    A -->|spawns| A1[Task: Subtask]
    A -->|spawns| A2[Task: Subtask]
    B -->|spawns| B1[Durable: Sub-Agent]
    B1 -->|spawns| B1a[Task: Subtask]
    style Root stroke:#3392FF,stroke-dasharray: 5 5
    style A stroke:#3392FF,stroke-dasharray: 5 5
    style B stroke:#3392FF,stroke-dasharray: 5 5
    style B1 stroke:#3392FF,stroke-dasharray: 5 5
```

This pattern is ideal for agent-based systems where each level of the tree decides what to do next. Each durable task in the tree can sleep, wait for events, or spawn more children, and none of them hold a worker slot while waiting.

## Determinism in Durable Tasks

Durable tasks must be **deterministic** between checkpoints. The task should always perform the same sequence of operations in between retries. This is what allows Hatchet to replay the task from the last checkpoint. If a task is not deterministic, it may produce different results on each retry, which can lead to unexpected behavior.

### Rules for determinism

1. **Only call methods available on the `DurableContext`**: a common way to introduce non-determinism is to call methods that produce side effects. If you need to fetch data from a database, call an API, or otherwise interact with external systems, spawn those operations as a **child task** using `RunChild`. Durable tasks are [evicted](/v1/task-eviction) at every wait point and replayed from checkpoint on resume. Any side effect not behind a checkpoint will re-execute.

2. **When updating durable tasks, always guarantee backwards compatibility**: if you change the order of checkpoint operations in a durable task, you may break determinism. For example, if you call `SleepFor` followed by `WaitFor`, and then change the order of those calls, Hatchet will not be able to replay the task correctly. The task may have already been checkpointed at the first call to `SleepFor`, and changing the order makes that checkpoint meaningless.


---

<!-- Source: https://docs.hatchet.run/v1/child-spawning -->

# Child Spawning

A task can spawn child tasks at runtime, including other durable tasks or entire DAG workflows. Children run independently on any available worker, and the parent can wait for their results.

Both durable tasks and DAG tasks support child spawning with the same core API. The key difference is that durable tasks free the parent's worker slot while waiting (via [eviction](/v1/task-eviction)), while DAG tasks hold their slot for the duration of execution.

#### Durable Tasks

## Spawning from Durable Tasks

A durable task can spawn child tasks at runtime. This is one of the core reasons to choose durable tasks over DAGs: the shape of work is decided as the task runs, not declared upfront.

> **Info:** Waiting for child results puts the parent task into an [evictable
>   state](/v1/task-eviction), the worker slot is freed and the parent is
>   re-queued when results are available.

Because the parent is evicted while children execute:

- **No slot waste** — the parent doesn't hold a worker slot while N children run across your fleet.
- **No deadlocks** — because the parent is evicted, it can't starve its own children for slots.
- **Dynamic N** — you decide how many children to spawn based on runtime data (input size, API responses, agent reasoning).

### Spawning child tasks

Use the context object to spawn a child task from within a durable task. The child runs independently on any available worker.

#### Python

```python
from examples.fanout.worker import ChildInput, child_wf

# 👀 example: run this inside of a parent task to spawn a child
child_wf.run(
    ChildInput(a="b"),
)
```

#### Typescript

```typescript
export const parentSingleChild = hatchet.task({
  name: 'parent-single-child',
  fn: async () => {
    const childRes = await child.run({ N: 1 });

    return {
      Result: childRes.Value,
    };
  },
});
```

#### Go

```go
// Inside a parent task
childResult, err := childWorkflow.Run(hCtx, ChildInput{
	Value: 1,
})
if err != nil {
	return err
}
```

#### Ruby

```ruby
FANOUT_CHILD_WF.run({ "a" => "b" })
```

### Parallel fan-out

Spawn many children at once and wait for all results. The parent is evicted during the wait, so it consumes no resources while children run.

#### Python

```python
async def run_child_workflows(n: int) -> list[dict[str, Any]]:
    return await child_wf.aio_run_many(
        [
            child_wf.create_bulk_run_item(
                input=ChildInput(a=str(i)),
            )
            for i in range(n)
        ]
    )
```

#### Typescript

```typescript
type ParentInput = {
  N: number;
};

export const parent = hatchet.task({
  name: 'parent',
  fn: async (input: ParentInput, ctx) => {
    const n = input.N;
    const promises = [];

    for (let i = 0; i < n; i++) {
      promises.push(child.run({ N: i }));
    }

    const childRes = await Promise.all(promises);
    const sum = childRes.reduce((acc, curr) => acc + curr.Value, 0);

    return {
      Result: sum,
    };
  },
});
```

#### Go

```go
// Run multiple child tasks in parallel using goroutines
var wg sync.WaitGroup
var mu sync.Mutex
results := make([]*ChildOutput, 0, n)

wg.Add(n)
for i := 0; i < n; i++ {
	go func(index int) {
		defer wg.Done()
		result, err := childWorkflow.Run(hCtx, ChildInput{Value: index})
		if err != nil {
			return
		}

		var childOutput ChildOutput
		err = result.Into(&childOutput)
		if err != nil {
			return
		}

		mu.Lock()
		results = append(results, &childOutput)
		mu.Unlock()
	}(i)
}
wg.Wait()
```

#### Ruby

```ruby
def run_child_workflows(n)
  FANOUT_CHILD_WF.run_many(
    n.times.map do |i|
      FANOUT_CHILD_WF.create_bulk_run_item(
        input: { "a" => i.to_s }
      )
    end
  )
end
```

### What children can be

A durable task can spawn any runnable:

| Child type       | Example                                                                           |
| ---------------- | --------------------------------------------------------------------------------- |
| **Regular task** | Spawn a stateless task for a quick computation or API call.                       |
| **Durable task** | Spawn another durable task that has its own checkpoints, sleeps, and event waits. |
| **DAG workflow** | Spawn an entire multi-task workflow and wait for its final output.                |

### Error handling

#### Python

```python
try:
    child_wf.run(
        ChildInput(a="b"),
    )
except Exception as e:
    print(f"Child workflow failed: {e}")
```

#### Typescript

```typescript
export const withErrorHandling = hatchet.task({
  name: 'parent-error-handling',
  fn: async () => {
    try {
      const childRes = await child.run({ N: 1 });

      return {
        Result: childRes.Value,
      };
    } catch (error) {
      // decide how to proceed here
      return {
        Result: -1,
      };
    }
  },
});
```

#### Go

```go
result, err := childWorkflow.Run(hCtx, ChildInput{Value: 1})
if err != nil {
	// Handle error from child workflow
	fmt.Printf("Child workflow failed: %v\n", err)
	// Decide how to proceed - retry, skip, or fail the parent
}
```

#### Ruby

```ruby
begin
  FANOUT_CHILD_WF.run({ "a" => "b" })
rescue StandardError => e
  puts "Child workflow failed: #{e.message}"
end
```

#### DAGs

## Spawning from DAG Tasks

DAG tasks can also spawn child tasks procedurally during execution. This lets you combine a fixed pipeline structure with dynamic child work inside individual tasks.

### Creating parent and child tasks

To implement child task spawning, you first need to create both parent and child task definitions.

#### Python

First, we'll declare a couple of tasks for the parent and child:

```python
class ParentInput(BaseModel):
    n: int = 100


class ChildInput(BaseModel):
    a: str


parent_wf = hatchet.workflow(name="FanoutParent", input_validator=ParentInput)
child_wf = hatchet.workflow(name="FanoutChild", input_validator=ChildInput)


@parent_wf.task(execution_timeout=timedelta(minutes=5))
async def spawn(input: ParentInput, ctx: Context) -> dict[str, Any]:
    print("spawning child")

    result = await child_wf.aio_run_many(
        [
            child_wf.create_bulk_run_item(
                input=ChildInput(a=str(i)),
                options=TriggerWorkflowOptions(
                    additional_metadata={"hello": "earth"}, key=f"child{i}"
                ),
            )
            for i in range(input.n)
        ],
    )

    print(f"results {result}")

    return {"results": result}
```

We also created a step on the parent task that spawns the child tasks. Now, we'll add a couple of steps to the child task:

```python
@child_wf.task()
async def process(input: ChildInput, ctx: Context) -> dict[str, str]:
    print(f"child process {input.a}")
    return {"status": input.a}


@child_wf.task(parents=[process])
async def process2(input: ChildInput, ctx: Context) -> dict[str, str]:
    process_output = ctx.task_output(process)
    a = process_output["status"]

    return {"status2": a + "2"}
```

And that's it! The fanout parent will run and spawn the child, and then will collect the results from its steps.

#### Typescript

```typescript
import sleep from '@hatchet-dev/typescript-sdk/util/sleep';
import { hatchet } from '../hatchet-client';

// (optional) Define the input type for the workflow
export type ChildInput = {
  Message: string;
};

export type ParentInput = {
  Message: string;
};

export const child = hatchet.workflow({
  name: 'child',
});

export const child1 = child.task({
  name: 'child1',
  fn: async (input: ChildInput, ctx) => {
    await sleep(30 * 1000);

    ctx.logger.info('hello from the child1', { hello: 'moon' });
    return {
      TransformedMessage: input.Message.toLowerCase(),
    };
  },
});

export const child2 = child.task({
  name: 'child2',
  fn: (input: ChildInput, ctx) => {
    ctx.logger.info('hello from the child2');
    return {
      TransformedMessage: input.Message.toLowerCase(),
    };
  },
});

export const child3 = child.task({
  name: 'child3',
  parents: [child1, child2],
  fn: async (input: ChildInput, ctx) => {
    ctx.logger.info('hello from the child3');
    return {
      TransformedMessage: input.Message.toLowerCase(),
    };
  },
});

export const parent = hatchet.task({
  name: 'parent',
  executionTimeout: '5m',
  fn: async (input: ParentInput, ctx) => {
    const c = await ctx.runChild(child, {
      Message: input.Message,
    });

    return {
      TransformedMessage: 'not implemented',
    };
  },
});
```

#### Go

```go
type ParentInput struct {
	Count int `json:"count"`
}

type ParentOutput struct {
	Sum int `json:"sum"`
}

func Parent(client *hatchet.Client) *hatchet.StandaloneTask {
	return client.NewStandaloneTask("parent-task",
		func(ctx hatchet.Context, input ParentInput) (ParentOutput, error) {
			log.Printf("Parent workflow spawning %d child workflows", input.Count)

			// Spawn multiple child workflows and collect results
			sum := 0
			for i := 0; i < input.Count; i++ {
				log.Printf("Spawning child workflow %d/%d", i+1, input.Count)

				// Spawn child workflow and wait for result
				childResult, err := Child(client).Run(ctx, ChildInput{
					Value: i + 1,
				})
				if err != nil {
					return ParentOutput{}, fmt.Errorf("failed to spawn child workflow %d: %w", i, err)
				}

				var childOutput ChildOutput
				err = childResult.Into(&childOutput)
				if err != nil {
					return ParentOutput{}, fmt.Errorf("failed to get child workflow result: %w", err)
				}

				sum += childOutput.Result

				log.Printf("Child workflow %d completed with result: %d", i+1, childOutput.Result)
			}

			log.Printf("All child workflows completed. Total sum: %d", sum)
			return ParentOutput{
				Sum: sum,
			}, nil
		},
	)
}

type ChildInput struct {
	Value int `json:"value"`
}

type ChildOutput struct {
	Result int `json:"result"`
}

func Child(client *hatchet.Client) *hatchet.StandaloneTask {
	return client.NewStandaloneTask("child-task",
		func(ctx hatchet.Context, input ChildInput) (ChildOutput, error) {
			return ChildOutput{
				Result: input.Value * 2,
			}, nil
		},
	)
}
```

#### Ruby

```ruby
FANOUT_PARENT_WF = HATCHET.workflow(name: "FanoutParent")
FANOUT_CHILD_WF = HATCHET.workflow(name: "FanoutChild")

FANOUT_PARENT_WF.task(:spawn, execution_timeout: 300) do |input, ctx|
  puts "spawning child"
  n = input["n"] || 100

  result = FANOUT_CHILD_WF.run_many(
    n.times.map do |i|
      FANOUT_CHILD_WF.create_bulk_run_item(
        input: { "a" => i.to_s },
        options: Hatchet::TriggerWorkflowOptions.new(
          additional_metadata: { "hello" => "earth" },
          key: "child#{i}"
        )
      )
    end
  )

  puts "results #{result}"
  { "results" => result }
end
```
```ruby
FANOUT_CHILD_PROCESS = FANOUT_CHILD_WF.task(:process) do |input, ctx|
  puts "child process #{input['a']}"
  { "status" => input["a"] }
end

FANOUT_CHILD_WF.task(:process2, parents: [FANOUT_CHILD_PROCESS]) do |input, ctx|
  process_output = ctx.task_output(FANOUT_CHILD_PROCESS)
  a = process_output["status"]
  { "status2" => "#{a}2" }
end
```

### Running child tasks

To spawn and run a child task from a parent task, use the appropriate method for your language:

#### Python

```python
from examples.fanout.worker import ChildInput, child_wf

# 👀 example: run this inside of a parent task to spawn a child
child_wf.run(
    ChildInput(a="b"),
)
```

#### Typescript

```typescript
export const parentSingleChild = hatchet.task({
  name: 'parent-single-child',
  fn: async () => {
    const childRes = await child.run({ N: 1 });

    return {
      Result: childRes.Value,
    };
  },
});
```

#### Go

```go
// Inside a parent task
childResult, err := childWorkflow.Run(hCtx, ChildInput{
	Value: 1,
})
if err != nil {
	return err
}
```

#### Ruby

```ruby
FANOUT_CHILD_WF.run({ "a" => "b" })
```

### Parallel child task execution

Spawn multiple child tasks in parallel:

#### Python

```python
async def run_child_workflows(n: int) -> list[dict[str, Any]]:
    return await child_wf.aio_run_many(
        [
            child_wf.create_bulk_run_item(
                input=ChildInput(a=str(i)),
            )
            for i in range(n)
        ]
    )
```

#### Typescript

```typescript
type ParentInput = {
  N: number;
};

export const parent = hatchet.task({
  name: 'parent',
  fn: async (input: ParentInput, ctx) => {
    const n = input.N;
    const promises = [];

    for (let i = 0; i < n; i++) {
      promises.push(child.run({ N: i }));
    }

    const childRes = await Promise.all(promises);
    const sum = childRes.reduce((acc, curr) => acc + curr.Value, 0);

    return {
      Result: sum,
    };
  },
});
```

#### Go

```go
// Run multiple child tasks in parallel using goroutines
var wg sync.WaitGroup
var mu sync.Mutex
results := make([]*ChildOutput, 0, n)

wg.Add(n)
for i := 0; i < n; i++ {
	go func(index int) {
		defer wg.Done()
		result, err := childWorkflow.Run(hCtx, ChildInput{Value: index})
		if err != nil {
			return
		}

		var childOutput ChildOutput
		err = result.Into(&childOutput)
		if err != nil {
			return
		}

		mu.Lock()
		results = append(results, &childOutput)
		mu.Unlock()
	}(i)
}
wg.Wait()
```

#### Ruby

```ruby
def run_child_workflows(n)
  FANOUT_CHILD_WF.run_many(
    n.times.map do |i|
      FANOUT_CHILD_WF.create_bulk_run_item(
        input: { "a" => i.to_s }
      )
    end
  )
end
```

### Error handling

#### Python

```python
try:
    child_wf.run(
        ChildInput(a="b"),
    )
except Exception as e:
    print(f"Child workflow failed: {e}")
```

#### Typescript

```typescript
export const withErrorHandling = hatchet.task({
  name: 'parent-error-handling',
  fn: async () => {
    try {
      const childRes = await child.run({ N: 1 });

      return {
        Result: childRes.Value,
      };
    } catch (error) {
      // decide how to proceed here
      return {
        Result: -1,
      };
    }
  },
});
```

#### Go

```go
result, err := childWorkflow.Run(hCtx, ChildInput{Value: 1})
if err != nil {
	// Handle error from child workflow
	fmt.Printf("Child workflow failed: %v\n", err)
	// Decide how to proceed - retry, skip, or fail the parent
}
```

#### Ruby

```ruby
begin
  FANOUT_CHILD_WF.run({ "a" => "b" })
rescue StandardError => e
  puts "Child workflow failed: #{e.message}"
end
```

## Common Patterns

### Dynamic fan-out / fan-in

Process a list of items whose length is only known at runtime. Spawn one child per item, collect all results, then continue. [Document processing](/guides/document-processing) and [batch processing](/guides/batch-processing) are canonical examples: when a batch of files arrives, a parent fans out to one child per document; each child parses, extracts, and validates its document in parallel across your worker fleet.


[Concurrency](/v1/concurrency) controls how many children run simultaneously. Hatchet distributes child tasks across available workers, so adding workers increases throughput without code changes. For rate-limited external services (OCR, LLM APIs), combine with [Rate Limits](/v1/rate-limits) to throttle child execution across all workers.

### Agent loops

An **agent loop** is implemented by having a durable task spawn a new child run of itself with updated input until a termination condition is met. Each iteration is a separate child task, giving full observability in the dashboard. AI agents use this pattern when they reason about what to do, spawn a subtask (or a sub-workflow), inspect the result, and decide whether to continue, branch, or stop. See [AI Agents](/guides/ai-agents/reasoning-loop) for a detailed guide.


### Recursive workflows

A durable task spawns child durable tasks, each of which may spawn their own children. This creates a tree of work that's entirely driven by runtime logic, useful for crawlers, recursive search, and tree-structured computations.

## Use cases

1. **Dynamic fan-out processing** — When the number of parallel tasks is determined at runtime. See [Batch Processing](/guides/batch-processing) and [Document Processing](/guides/document-processing).
2. **Reusable workflow components** — Create modular workflows that can be reused across different parent workflows.
3. **Resource-intensive operations** — Spread computation across multiple workers.
4. **Agent-based systems** — Allow AI agents to spawn new workflows based on their reasoning. See [AI Agents](/guides/ai-agents/reasoning-loop).
5. **Long-running operations** — Break down long operations into smaller, trackable units of work.


---

<!-- Source: https://docs.hatchet.run/v1/sleep -->

# Sleep & Delays

Sleep pauses a task for a specified duration while freeing the worker slot. No resources are consumed during the wait, whether the pause lasts seconds or weeks.


Both durable tasks and DAGs support sleeping, but the API differs: durable tasks call `SleepFor` dynamically at runtime, while DAGs declare a sleep condition upfront on the task definition.

#### Durable Tasks

## Durable Sleep

Durable sleep pauses execution for a specified amount of time and frees the worker slot until the sleep expires.

> **Info:** Sleeping puts the task into an [evictable state](/v1/task-eviction), the
>   worker slot is freed and the task is re-queued when the sleep expires.

Unlike a language-level sleep (e.g. `time.sleep` in Python or `setTimeout` in Node), durable sleep is guaranteed to respect the original duration across interruptions. A language-level sleep ties the wait to the local process, so if the process restarts, the sleep starts over from zero.

For example, say you'd like to send a notification to a user after 24 hours. With `time.sleep`, if the task is interrupted after 23 hours, it will restart and sleep for 24 hours again (47 hours total). With durable sleep, Hatchet tracks the original deadline server-side, so the task will only sleep for 1 more hour on restart.

### Using durable sleep

Durable sleep can be used by calling the `SleepFor` method on the `DurableContext` object. This method takes a duration as an argument and will sleep for that duration.

#### Python

```python
@hatchet.durable_task(name="DurableSleepTask")
async def durable_sleep_task(input: EmptyModel, ctx: DurableContext) -> None:
    res = await ctx.aio_sleep_for(timedelta(seconds=5))

    print("got result", res)
```

#### Typescript

```typescript
durableSleep.durableTask({
  name: 'durable-sleep',
  executionTimeout: '10m',
  fn: async (_, ctx) => {
    console.log('sleeping for 5s');
    const sleepRes = await ctx.sleepFor('5s');
    console.log('done sleeping for 5s', sleepRes);

    return {
      Value: 'done',
    };
  },
});
```

#### Go

```go
task := client.NewStandaloneDurableTask("long-running-task", func(ctx hatchet.DurableContext, input DurableInput) (DurableOutput, error) {
	log.Printf("Starting task, will sleep for %d seconds", input.Delay)

	if _, err := ctx.SleepFor(time.Duration(input.Delay) * time.Second); err != nil {
		return DurableOutput{}, err
	}

	log.Printf("Finished sleeping, processing message: %s", input.Message)

	return DurableOutput{
		ProcessedAt: time.Now().Format(time.RFC3339),
		Message:     "Processed: " + input.Message,
	}, nil
})
```

#### Ruby

```ruby
DURABLE_SLEEP_TASK = HATCHET.durable_task(name: "DurableSleepTask") do |input, ctx|
  res = ctx.sleep_for(duration: 5)

  puts "got result #{res}"
end
```

#### DAGs

## Sleep Conditions

Sleep conditions pause a DAG task for a specified duration before it runs. Use them when a task should wait for a fixed amount of time after its parent tasks complete.

Unlike durable sleep (which is called dynamically at runtime), DAG sleep conditions are declared upfront on the task definition. Both free the worker slot during the wait.

### Using sleep conditions

Declare a task with a `wait_for` sleep condition. The task will wait for its parent tasks to complete, then sleep for the specified duration before executing.

#### Python

```python
@task_condition_workflow.task(
    parents=[start], wait_for=[SleepCondition(timedelta(seconds=10))]
)
def wait_for_sleep(input: EmptyModel, ctx: Context) -> StepOutput:
    return StepOutput(random_number=random.randint(1, 100))
```

#### Typescript

```typescript
const waitForSleep = taskConditionWorkflow.task({
  name: 'waitForSleep',
  parents: [start],
  waitFor: [new SleepCondition('10s')],
  fn: () => {
    return {
      randomNumber: Math.floor(Math.random() * 100) + 1,
    };
  },
});
```

#### Go

```go
waitForSleep := workflow.NewTask("wait-for-sleep", func(ctx hatchet.Context, _ any) (StepOutput, error) {
	return StepOutput{RandomNumber: rand.Intn(100) + 1}, nil //nolint:gosec
},
	hatchet.WithParents(start),
	hatchet.WithWaitFor(hatchet.SleepCondition(10*time.Second)),
)
```

#### Ruby

```ruby
WAIT_FOR_SLEEP = TASK_CONDITION_WORKFLOW.task(
  :wait_for_sleep,
  parents: [COND_START],
  wait_for: [Hatchet::SleepCondition.new(10)]
) do |input, ctx|
  { "random_number" => rand(1..100) }
end
```

This task will first wait for its parent to complete, then sleep for the specified duration before executing.

### Combining with other conditions

Sleep conditions can be combined with other conditions using or groups. For example, you can wait for _either_ a sleep duration or an event (whichever comes first). See [Combining Conditions](/v1/conditions#or-groups) for details.


---

<!-- Source: https://docs.hatchet.run/v1/events -->

# Events

Tasks can pause until an external event arrives before continuing. This is the foundation for [human-in-the-loop](/guides/human-in-the-loop) workflows, webhook-driven pipelines, and any flow that depends on signals from outside the task.


Both durable tasks and DAGs support waiting for events. Durable tasks call `WaitForEvent` dynamically at runtime, while DAGs declare event conditions upfront on the task definition.

Events are delivered by [pushing events](/v1/external-events/pushing-events) into Hatchet using the event client. The event key you push must match the key your task is waiting for.

#### Durable Tasks

## Wait For Events

Wait For Events lets a durable task pause until an external event arrives. Even if the task is interrupted and requeued while waiting, the event will still be processed. When it resumes, it reads the event from the durable event log and continues.

> **Info:** Waiting for an event puts the task into an [evictable
>   state](/v1/task-eviction), the worker slot is freed and the task is re-queued
>   when the event arrives.

### Declaring a wait for event

Wait For Event is declared using the context method `WaitFor` (or utility method `WaitForEvent`) on the `DurableContext` object.

#### Python

```python
@hatchet.durable_task(name="DurableEventTask")
async def durable_event_task(input: EmptyModel, ctx: DurableContext) -> None:
    res = await ctx.aio_wait_for(
        "event",
        UserEventCondition(event_key="user:update"),
    )

    print("got event", res)
```

#### Typescript

```typescript
export const durableEvent = hatchet.durableTask({
  name: 'durable-event',
  executionTimeout: '10m',
  fn: async (_, ctx) => {
    const res = ctx.waitFor({
      eventKey: 'user:update',
    });

    console.log('res', res);

    return {
      Value: 'done',
    };
  },
});
```

#### Go

```go
task := client.NewStandaloneDurableTask("long-running-task", func(ctx hatchet.DurableContext, input DurableInput) (DurableOutput, error) {
	log.Printf("Starting task, will sleep for %d seconds", input.Delay)

	if _, err := ctx.WaitForEvent("user:updated", ""); err != nil {
		return DurableOutput{}, err
	}

	log.Printf("Finished waiting for event, processing message: %s", input.Message)

	return DurableOutput{
		ProcessedAt: time.Now().Format(time.RFC3339),
		Message:     "Processed: " + input.Message,
	}, nil
})
```

#### Ruby

```ruby
DURABLE_EVENT_TASK = HATCHET.durable_task(name: "DurableEventTask") do |input, ctx|
  res = ctx.wait_for(
    "event",
    Hatchet::UserEventCondition.new(event_key: "user:update")
  )

  puts "got event #{res}"
end

DURABLE_EVENT_TASK_WITH_FILTER = HATCHET.durable_task(name: "DurableEventWithFilterTask") do |input, ctx|
```

### Event filters

Events can be filtered using [CEL](https://github.com/google/cel-spec) expressions. For example, to only receive `user:update` events for a specific user:

#### Python

```python
res = await ctx.aio_wait_for(
    "event",
    UserEventCondition(
        event_key="user:update", expression="input.user_id == '1234'"
    ),
)
```

#### Typescript

```typescript
const res = ctx.waitFor({
  eventKey: 'user:update',
  expression: "input.userId == '1234'",
});
```

#### Go

```go
if _, err := ctx.WaitForEvent("user:updated", "input.status_code == 200"); err != nil {
	return DurableOutput{}, err
}
```

#### Ruby

```ruby
res = ctx.wait_for(
    "event",
    Hatchet::UserEventCondition.new(
      event_key: "user:update",
      expression: "input.user_id == '1234'"
    )
  )

  puts "got event #{res}"
end
```

### Pushing events

For a waiting task to resume, something must [push an event](/v1/external-events/pushing-events) into Hatchet with a matching key. You can do this from any service that has access to the Hatchet client.

#### Python

```python
hatchet.event.push("user:create", {"should_skip": False})
```

#### Typescript

```typescript
const res = await hatchet.events.push('simple-event:create', {
  Message: 'hello',
  ShouldSkip: false,
});
```

#### Go

```go
err := client.Events().Push(
	context.Background(),
	"simple-event:create",
	EventInput{
		Message: "Hello, World!",
	},
)
if err != nil {
	return err
}
```

#### Ruby

```ruby
HATCHET.event.push("user:create", { "should_skip" => false })
```

When the pushed event's key matches what a durable task is waiting for (and passes any CEL filter), the task is re-queued and resumes from its checkpoint.

#### DAGs

## Event Conditions

Event conditions let a DAG task react to external events. A task can wait for an event before running, be skipped when an event arrives, or be cancelled by an event.

Unlike durable tasks (where `WaitForEvent` is called dynamically at runtime), DAG event conditions are declared upfront on the task definition.

### Usage modes

Event conditions can be used with three operators:

- **`wait_for`** — the task waits for the event before starting.
- **`skip_if`** — the task is skipped if the event arrives.
- **`cancel_if`** — the task is cancelled if the event arrives.

> **Warning:** A task cancelled by `cancel_if` behaves like any other cancellation in Hatchet
>   — downstream tasks will be cancelled as well.

### Waiting for an event

Declare a task with a `wait_for` event condition. The task will not start until the specified event is pushed into Hatchet.

#### Python

```python
@task_condition_workflow.task(
    parents=[start],
    wait_for=[
        or_(
            SleepCondition(duration=timedelta(minutes=1)),
            UserEventCondition(event_key="wait_for_event:start"),
        )
    ],
)
def wait_for_event(input: EmptyModel, ctx: Context) -> StepOutput:
    return StepOutput(random_number=random.randint(1, 100))
```

#### Typescript

```typescript
const waitForEvent = taskConditionWorkflow.task({
  name: 'waitForEvent',
  parents: [start],
  waitFor: [Or(new SleepCondition('1m'), new UserEventCondition('wait_for_event:start', 'true'))],
  fn: () => {
    return {
      randomNumber: Math.floor(Math.random() * 100) + 1,
    };
  },
});
```

#### Go

```go
waitForEvent := workflow.NewTask("wait-for-event", func(ctx hatchet.Context, _ any) (StepOutput, error) {
	return StepOutput{RandomNumber: rand.Intn(100) + 1}, nil //nolint:gosec
},
	hatchet.WithParents(start),
	hatchet.WithWaitFor(hatchet.OrCondition(
		hatchet.SleepCondition(1*time.Minute),
		hatchet.UserEventCondition("wait_for_event:start", ""),
	)),
)
```

#### Ruby

```ruby
WAIT_FOR_EVENT = TASK_CONDITION_WORKFLOW.task(
  :wait_for_event,
  parents: [COND_START],
  wait_for: [
    Hatchet.or_(
      Hatchet::SleepCondition.new(60),
      Hatchet::UserEventCondition.new(event_key: "wait_for_event:start")
    )
  ]
) do |input, ctx|
  { "random_number" => rand(1..100) }
end
```

### Skipping on an event

Declare a task with a `skip_if` event condition. The task will be skipped if the event arrives before the task starts.

#### Python

```python
@task_condition_workflow.task(
    parents=[start],
    wait_for=[SleepCondition(timedelta(seconds=30))],
    skip_if=[UserEventCondition(event_key="skip_on_event:skip")],
)
def skip_on_event(input: EmptyModel, ctx: Context) -> StepOutput:
    return StepOutput(random_number=random.randint(1, 100))
```

#### Typescript

```typescript
const skipOnEvent = taskConditionWorkflow.task({
  name: 'skipOnEvent',
  parents: [start],
  waitFor: [new SleepCondition('10s')],
  skipIf: [new UserEventCondition('skip_on_event:skip', 'true')],
  fn: () => {
    return {
      randomNumber: Math.floor(Math.random() * 100) + 1,
    };
  },
});
```

#### Go

```go
skipOnEvent := workflow.NewTask("skip-on-event", func(ctx hatchet.Context, _ any) (StepOutput, error) {
	return StepOutput{RandomNumber: rand.Intn(100) + 1}, nil //nolint:gosec
},
	hatchet.WithParents(start),
	hatchet.WithWaitFor(hatchet.SleepCondition(30*time.Second)),
	hatchet.WithSkipIf(hatchet.UserEventCondition("skip_on_event:skip", "")),
)
```

#### Ruby

```ruby
SKIP_ON_EVENT = TASK_CONDITION_WORKFLOW.task(
  :skip_on_event,
  parents: [COND_START],
  wait_for: [Hatchet::SleepCondition.new(30)],
  skip_if: [Hatchet::UserEventCondition.new(event_key: "skip_on_event:skip")]
) do |input, ctx|
  { "random_number" => rand(1..100) }
end
```

### Event filters

Events can be filtered using [CEL](https://github.com/google/cel-spec) expressions. The CEL expression is evaluated against the event payload, and the condition only matches if the expression returns `true`. This works identically to event filters in durable tasks.

### Pushing events

For a waiting task to proceed, something must [push an event](/v1/external-events/pushing-events) into Hatchet with a matching key. You can do this from any service that has access to the Hatchet client.

#### Python

```python
hatchet.event.push("user:create", {"should_skip": False})
```

#### Typescript

```typescript
const res = await hatchet.events.push('simple-event:create', {
  Message: 'hello',
  ShouldSkip: false,
});
```

#### Go

```go
err := client.Events().Push(
	context.Background(),
	"simple-event:create",
	EventInput{
		Message: "Hello, World!",
	},
)
if err != nil {
	return err
}
```

#### Ruby

```ruby
HATCHET.event.push("user:create", { "should_skip" => false })
```

### Combining with other conditions

Event conditions can be combined with parent and sleep conditions using or groups. For example, you can wait for _either_ an event or a timeout (whichever comes first). See [Conditions & Branching](/v1/conditions) for details.


---

<!-- Source: https://docs.hatchet.run/v1/conditions -->

# Conditions & Branching

Workflows often need to branch: run different paths depending on data, skip steps when conditions aren't met, or wait for a combination of signals before proceeding. Both durable tasks and DAGs support conditional logic, but the approach differs.


#### Durable Tasks

## Procedural Branching

Durable tasks use standard language control flow (`if`/`else`, `match`, loops) to branch at runtime. Because the task is a single long-running function, you can make decisions based on any data available during execution: inputs, intermediate results, API responses, or child task outputs.

```python
@workflow.durable_task()
async def process(input: ProcessInput, ctx: DurableContext):
    result = await ctx.run_child(analyze_task, input)

    if result["score"] > 0.8:
        await ctx.run_child(fast_path_task, result)
    else:
        await ctx.run_child(slow_path_task, result)
        await ctx.run_child(review_task, result)
```

This is one of the key advantages of durable tasks: branching logic is expressed directly in code, making it easy to handle complex, dynamic flows. Each branch can spawn different children, sleep for different durations, or wait for different events.

> **Warning:** Branching logic must be **deterministic** between checkpoints. If the task is
>   evicted and replayed, the same branches must execute in the same order. Base
>   decisions on checkpoint outputs (child results, event payloads) rather than
>   wall-clock time or external state that may change between replays. See [Best
>   Practices](/v1/patterns/mixing-patterns#determinism-in-durable-tasks) for
>   details.

## Or Groups

Durable tasks can combine multiple wait conditions using or groups. An or group evaluates to `True` if **at least one** of its conditions is satisfied, letting you express "proceed on timeout or event, whichever comes first."

#### Python

```python
@durable_workflow.durable_task()
async def wait_for_or_group_1(
    _i: EmptyModel, ctx: DurableContext
) -> dict[str, str | int]:
    start = time.time()
    wait_result = await ctx.aio_wait_for(
        uuid4().hex,
        or_(
            SleepCondition(timedelta(seconds=SLEEP_TIME)),
            UserEventCondition(event_key=EVENT_KEY),
        ),
    )

    key = list(wait_result.keys())[0]
    event_id = list(wait_result[key].keys())[0]

    return {
        "runtime": int(time.time() - start),
        "key": key,
        "event_id": event_id,
    }
```

`or_()` wraps a `SleepCondition` and a `UserEventCondition` into a single or group. The task will resume as soon as either the sleep expires or the event arrives.

#### Typescript

```typescript
export const durableEvent = hatchet.durableTask({
  name: 'durable-event',
  executionTimeout: '10m',
  fn: async (_, ctx) => {
    const res = ctx.waitFor({
      eventKey: 'user:update',
    });

    console.log('res', res);

    return {
      Value: 'done',
    };
  },
});
```

#### Go

```go
task := client.NewStandaloneDurableTask("long-running-task", func(ctx hatchet.DurableContext, input DurableInput) (DurableOutput, error) {
	log.Printf("Starting task, will sleep for %d seconds", input.Delay)

	if _, err := ctx.WaitForEvent("user:updated", ""); err != nil {
		return DurableOutput{}, err
	}

	log.Printf("Finished waiting for event, processing message: %s", input.Message)

	return DurableOutput{
		ProcessedAt: time.Now().Format(time.RFC3339),
		Message:     "Processed: " + input.Message,
	}, nil
})
```

#### Ruby

```ruby
DURABLE_EVENT_TASK = HATCHET.durable_task(name: "DurableEventTask") do |input, ctx|
  res = ctx.wait_for(
    "event",
    Hatchet::UserEventCondition.new(event_key: "user:update")
  )

  puts "got event #{res}"
end

DURABLE_EVENT_TASK_WITH_FILTER = HATCHET.durable_task(name: "DurableEventWithFilterTask") do |input, ctx|
```

#### DAGs

## Parent Conditions

Parent conditions let a DAG task decide whether to run based on the output of a parent task. This enables branching logic within a DAG: different paths can execute depending on runtime data, while the overall graph structure remains fixed and visible in the dashboard.

Parent conditions can be used with two operators:

- **`skip_if`** — skip the task if the parent output matches the condition.
- **`cancel_if`** — cancel the task (and its downstream dependents) if the parent output matches the condition.

> **Warning:** A task cancelled by `cancel_if` behaves like any other cancellation in Hatchet
>   — downstream tasks will be cancelled as well.

### Branching example

A common pattern is to create two sibling tasks with complementary parent conditions. For example, one task runs when a value is greater than 50 and the other runs when it is less than or equal to 50. Only one branch executes per run.

First, declare a base task that returns a value:

#### Python

```python
@task_condition_workflow.task()
def start(input: EmptyModel, ctx: Context) -> StepOutput:
    return StepOutput(random_number=random.randint(1, 100))
```

#### Typescript

```typescript
const start = taskConditionWorkflow.task({
  name: 'start',
  fn: () => {
    return {
      randomNumber: Math.floor(Math.random() * 100) + 1,
    };
  },
});
```

#### Go

```go
start := workflow.NewTask("start", func(ctx hatchet.Context, _ any) (StepOutput, error) {
	return StepOutput{RandomNumber: rand.Intn(100) + 1}, nil //nolint:gosec
})
```

#### Ruby

```ruby
COND_START = TASK_CONDITION_WORKFLOW.task(:start) do |input, ctx|
  { "random_number" => rand(1..100) }
end
```

Then add two branches that use `ParentCondition` with `skip_if`:

#### Python

```python
@task_condition_workflow.task(
    parents=[wait_for_sleep],
    skip_if=[
        ParentCondition(
            parent=wait_for_sleep,
            expression="output.random_number > 50",
        )
    ],
)
def left_branch(input: EmptyModel, ctx: Context) -> StepOutput:
    return StepOutput(random_number=random.randint(1, 100))


@task_condition_workflow.task(
    parents=[wait_for_sleep],
    skip_if=[
        ParentCondition(
            parent=wait_for_sleep,
            expression="output.random_number <= 50",
        )
    ],
)
def right_branch(input: EmptyModel, ctx: Context) -> StepOutput:
    return StepOutput(random_number=random.randint(1, 100))
```

#### Typescript

```typescript
const leftBranch = taskConditionWorkflow.task({
  name: 'leftBranch',
  parents: [waitForSleep],
  skipIf: [new ParentCondition(waitForSleep, 'output.randomNumber > 50')],
  fn: () => {
    return {
      randomNumber: Math.floor(Math.random() * 100) + 1,
    };
  },
});

const rightBranch = taskConditionWorkflow.task({
  name: 'rightBranch',
  parents: [waitForSleep],
  skipIf: [new ParentCondition(waitForSleep, 'output.randomNumber <= 50')],
  fn: () => {
    return {
      randomNumber: Math.floor(Math.random() * 100) + 1,
    };
  },
});
```

#### Go

```go
leftBranch := workflow.NewTask("left-branch", func(ctx hatchet.Context, _ any) (StepOutput, error) {
	return StepOutput{RandomNumber: rand.Intn(100) + 1}, nil //nolint:gosec
},
	hatchet.WithParents(waitForSleep),
	hatchet.WithSkipIf(hatchet.ParentCondition(waitForSleep, "output.random_number > 50")),
)

rightBranch := workflow.NewTask("right-branch", func(ctx hatchet.Context, _ any) (StepOutput, error) {
	return StepOutput{RandomNumber: rand.Intn(100) + 1}, nil //nolint:gosec
},
	hatchet.WithParents(waitForSleep),
	hatchet.WithSkipIf(hatchet.ParentCondition(waitForSleep, "output.random_number <= 50")),
)
```

#### Ruby

```ruby
LEFT_BRANCH = TASK_CONDITION_WORKFLOW.task(
  :left_branch,
  parents: [WAIT_FOR_SLEEP],
  skip_if: [
    Hatchet::ParentCondition.new(
      parent: WAIT_FOR_SLEEP,
      expression: "output.random_number > 50"
    )
  ]
) do |input, ctx|
  { "random_number" => rand(1..100) }
end

RIGHT_BRANCH = TASK_CONDITION_WORKFLOW.task(
  :right_branch,
  parents: [WAIT_FOR_SLEEP],
  skip_if: [
    Hatchet::ParentCondition.new(
      parent: WAIT_FOR_SLEEP,
      expression: "output.random_number <= 50"
    )
  ]
) do |input, ctx|
  { "random_number" => rand(1..100) }
end
```

These two tasks check whether the output of the base task was greater or less than `50`, respectively. Only one of the two will run per workflow execution.

### Checking if a task was skipped

Downstream tasks can check whether a parent was skipped using `ctx.was_skipped`:

#### Python

```python
@task_condition_workflow.task(
    parents=[
        start,
        wait_for_sleep,
        wait_for_event,
        skip_on_event,
        left_branch,
        right_branch,
    ],
)
def sum(input: EmptyModel, ctx: Context) -> RandomSum:
    one = ctx.task_output(start).random_number
    two = ctx.task_output(wait_for_event).random_number
    three = ctx.task_output(wait_for_sleep).random_number
    four = (
        ctx.task_output(skip_on_event).random_number
        if not ctx.was_skipped(skip_on_event)
        else 0
    )

    five = (
        ctx.task_output(left_branch).random_number
        if not ctx.was_skipped(left_branch)
        else 0
    )
    six = (
        ctx.task_output(right_branch).random_number
        if not ctx.was_skipped(right_branch)
        else 0
    )

    return RandomSum(sum=one + two + three + four + five + six)
```

#### Typescript

```typescript
taskConditionWorkflow.task({
  name: 'sum',
  parents: [start, waitForSleep, waitForEvent, skipOnEvent, leftBranch, rightBranch],
  fn: async (_, ctx: Context<any, any>) => {
    const one = (await ctx.parentOutput(start)).randomNumber;
    const two = (await ctx.parentOutput(waitForEvent)).randomNumber;
    const three = (await ctx.parentOutput(waitForSleep)).randomNumber;
    const four = (await ctx.parentOutput(skipOnEvent))?.randomNumber || 0;
    const five = (await ctx.parentOutput(leftBranch))?.randomNumber || 0;
    const six = (await ctx.parentOutput(rightBranch))?.randomNumber || 0;

    return {
      sum: one + two + three + four + five + six,
    };
  },
});
```

#### Go

```go
_ = workflow.NewTask("sum", func(ctx hatchet.Context, _ any) (RandomSum, error) {
	var startOut StepOutput
	err := ctx.ParentOutput(start, &startOut)
	if err != nil {
		return RandomSum{}, err
	}

	var waitForEventOut StepOutput
	err = ctx.ParentOutput(waitForEvent, &waitForEventOut)
	if err != nil {
		return RandomSum{}, err
	}

	var waitForSleepOut StepOutput
	err = ctx.ParentOutput(waitForSleep, &waitForSleepOut)
	if err != nil {
		return RandomSum{}, err
	}

	total := startOut.RandomNumber + waitForEventOut.RandomNumber + waitForSleepOut.RandomNumber

	if !ctx.WasSkipped(skipOnEvent) {
		var out StepOutput
		err = ctx.ParentOutput(skipOnEvent, &out)
		if err == nil {
			total += out.RandomNumber
		}
	}

	if !ctx.WasSkipped(leftBranch) {
		var out StepOutput
		err = ctx.ParentOutput(leftBranch, &out)
		if err == nil {
			total += out.RandomNumber
		}
	}

	if !ctx.WasSkipped(rightBranch) {
		var out StepOutput
		err = ctx.ParentOutput(rightBranch, &out)
		if err == nil {
			total += out.RandomNumber
		}
	}

	return RandomSum{Sum: total}, nil
}, hatchet.WithParents(
	start,
	waitForSleep,
	waitForEvent,
	skipOnEvent,
	leftBranch,
	rightBranch,
))
```

#### Ruby

```ruby
TASK_CONDITION_WORKFLOW.task(
  :sum,
  parents: [COND_START, WAIT_FOR_SLEEP, WAIT_FOR_EVENT, SKIP_ON_EVENT, LEFT_BRANCH, RIGHT_BRANCH]
) do |input, ctx|
  one = ctx.task_output(COND_START)["random_number"]
  two = ctx.task_output(WAIT_FOR_EVENT)["random_number"]
  three = ctx.task_output(WAIT_FOR_SLEEP)["random_number"]
  four = ctx.was_skipped?(SKIP_ON_EVENT) ? 0 : ctx.task_output(SKIP_ON_EVENT)["random_number"]
  five = ctx.was_skipped?(LEFT_BRANCH) ? 0 : ctx.task_output(LEFT_BRANCH)["random_number"]
  six = ctx.was_skipped?(RIGHT_BRANCH) ? 0 : ctx.task_output(RIGHT_BRANCH)["random_number"]

  { "sum" => one + two + three + four + five + six }
end
```

## Or Groups

DAG tasks can declare multiple conditions that work together to control when and whether a task runs. Conditions of different types (parent conditions, [event conditions](/v1/events), and [sleep conditions](/v1/sleep)) can be mixed on a single task using **or groups**.

An **or group** is a set of conditions combined with an `Or` operator. The group evaluates to `True` if **at least one** of its conditions is satisfied. Multiple or groups on the same task are combined with `AND`, so every group must have at least one satisfied condition for the task to proceed.

This lets you express arbitrarily complex sets of conditions in [conjunctive normal form](https://en.wikipedia.org/wiki/Conjunctive_normal_form) (CNF).

### Sleep + Event example

The most common combination is a sleep condition with an event condition: proceed when an external signal arrives _or_ after a timeout (whichever comes first). This is ideal for [human-in-the-loop](/guides/human-in-the-loop) workflows where you want a deadline.

#### Python

```python
@task_condition_workflow.task(
    parents=[start],
    wait_for=[
        or_(
            SleepCondition(duration=timedelta(minutes=1)),
            UserEventCondition(event_key="wait_for_event:start"),
        )
    ],
)
def wait_for_event(input: EmptyModel, ctx: Context) -> StepOutput:
    return StepOutput(random_number=random.randint(1, 100))
```

`or_()` wraps a `SleepCondition` and a `UserEventCondition` into a single or group. The task will start as soon as either the sleep expires or the event arrives.

#### Typescript

```typescript
const waitForEvent = taskConditionWorkflow.task({
  name: 'waitForEvent',
  parents: [start],
  waitFor: [Or(new SleepCondition('1m'), new UserEventCondition('wait_for_event:start', 'true'))],
  fn: () => {
    return {
      randomNumber: Math.floor(Math.random() * 100) + 1,
    };
  },
});
```

`Or()` wraps a `SleepCondition` and a `UserEventCondition` into a single or group. The task will start as soon as either the sleep expires or the event arrives.

#### Go

```go
waitForEvent := workflow.NewTask("wait-for-event", func(ctx hatchet.Context, _ any) (StepOutput, error) {
	return StepOutput{RandomNumber: rand.Intn(100) + 1}, nil //nolint:gosec
},
	hatchet.WithParents(start),
	hatchet.WithWaitFor(hatchet.OrCondition(
		hatchet.SleepCondition(1*time.Minute),
		hatchet.UserEventCondition("wait_for_event:start", ""),
	)),
)
```

`hatchet.WithWaitFor` and `hatchet.WithSkipIf` attach conditions to the task. The task will wait for the sleep to expire before starting, and will be skipped if the event arrives.

#### Ruby

```ruby
WAIT_FOR_EVENT = TASK_CONDITION_WORKFLOW.task(
  :wait_for_event,
  parents: [COND_START],
  wait_for: [
    Hatchet.or_(
      Hatchet::SleepCondition.new(60),
      Hatchet::UserEventCondition.new(event_key: "wait_for_event:start")
    )
  ]
) do |input, ctx|
  { "random_number" => rand(1..100) }
end
```

`Hatchet.or_()` wraps a `SleepCondition` and a `UserEventCondition` into a single or group. The task will start as soon as either the sleep expires or the event arrives.

### Multiple or groups

For more complex logic, you can declare multiple or groups on a single task. Consider three conditions:

- **Condition A**: Parent output is greater than 50
- **Condition B**: Sleep for 30 seconds
- **Condition C**: Receive the `payment:processed` event

To proceed if (A _or_ B) **and** (A _or_ C), declare two or groups:

1. Group 1: `A or B`
2. Group 2: `A or C`

The task will run once both groups are satisfied. If A is true, both groups pass immediately. If A is false, the task needs both B (sleep expires) and C (event arrives).

### Common combinations

| Combination    | Use case                                                                             |
| -------------- | ------------------------------------------------------------------------------------ |
| Sleep + Event  | Proceed after a timeout _or_ when an external signal arrives (whichever comes first) |
| Parent + Event | Proceed if a parent output meets a threshold _or_ a manual override event arrives    |
| Parent + Sleep | Proceed if a parent indicates readiness _or_ after a maximum wait time               |
| All three      | Complex gates combining data-driven, time-based, and event-driven conditions         |


---

<!-- Source: https://docs.hatchet.run/v1/on-failure -->

# Error Handling

When a task fails, you need a way to run cleanup logic, send notifications, or trigger compensating actions. Both durable tasks and DAGs support error handling, but the mechanism differs: durable tasks use standard try/catch blocks, while DAGs declare a special on-failure task.

#### Durable Tasks

## Try/Catch in Durable Tasks

Durable tasks are regular functions, so you handle errors with your language's native error handling (`try`/`except` in Python, `try`/`catch` in TypeScript/Go). This gives you full control over what happens when a child task or operation fails.

### Handling child task errors

When spawning child tasks, wrap the call in a try/catch block to handle failures gracefully:

#### Python

```python
try:
    child_wf.run(
        ChildInput(a="b"),
    )
except Exception as e:
    print(f"Child workflow failed: {e}")
```

#### Typescript

```typescript
export const withErrorHandling = hatchet.task({
  name: 'parent-error-handling',
  fn: async () => {
    try {
      const childRes = await child.run({ N: 1 });

      return {
        Result: childRes.Value,
      };
    } catch (error) {
      // decide how to proceed here
      return {
        Result: -1,
      };
    }
  },
});
```

#### Go

```go
result, err := childWorkflow.Run(hCtx, ChildInput{Value: 1})
if err != nil {
	// Handle error from child workflow
	fmt.Printf("Child workflow failed: %v\n", err)
	// Decide how to proceed - retry, skip, or fail the parent
}
```

#### Ruby

```ruby
begin
  FANOUT_CHILD_WF.run({ "a" => "b" })
rescue StandardError => e
  puts "Child workflow failed: #{e.message}"
end
```

### Common patterns

- **Retry with backoff** — Catch the error, sleep, and retry the child task.
- **Fallback logic** — If a primary path fails, spawn a different child task as a fallback.
- **Partial failure handling** — In a fan-out, collect results from successful children and handle failures individually rather than failing the entire workflow.
- **Cleanup** — Release resources, cancel in-progress work, or notify external systems.

#### DAGs

## On-Failure Tasks

The on-failure task is a special task that runs when any task in the workflow fails. It lets you handle errors, perform cleanup, or trigger notifications declaratively as part of the workflow definition.

### Defining an on-failure task

You can define an on-failure task on your workflow the same as you'd define any other task:

#### Python

```python
# This workflow will fail because the step will throw an error
# we define an onFailure step to handle this case

on_failure_wf = hatchet.workflow(name="OnFailureWorkflow")


@on_failure_wf.task(execution_timeout=timedelta(seconds=1))
def step1(input: EmptyModel, ctx: Context) -> None:
    # 👀 this step will always raise an exception
    raise Exception(ERROR_TEXT)


# 👀 After the workflow fails, this special step will run
@on_failure_wf.on_failure_task()
def on_failure(input: EmptyModel, ctx: Context) -> dict[str, str]:
    # 👀 we can do things like perform cleanup logic
    # or notify a user here

    # 👀 Fetch the errors from upstream step runs from the context
    print(ctx.task_run_errors)

    return {"status": "success"}
```

Note: Only one on-failure task can be defined per workflow.


#### Typescript

```typescript
// This workflow will fail because `step1` throws. We define an `onFailure` handler to run cleanup.
export const failureWorkflow = hatchet.workflow({
  name: 'on-failure-workflow',
});

failureWorkflow.task({
  name: 'step1',
  executionTimeout: '1s',
  fn: async () => {
    throw new Error(ERROR_TEXT);
  },
});

// 👀 After the workflow fails, this special step will run
failureWorkflow.onFailure({
  name: 'on_failure',
  fn: async (_input, ctx) => {
    console.log('onFailure for run:', ctx.workflowRunId());
    console.log('upstream errors:', ctx.errors());

    return {
      status: 'success',
    };
  },
});
```

#### Go

```go
multiStepWorkflow.OnFailure(func(ctx hatchet.Context, input FailureInput) (FailureHandlerOutput, error) {
	log.Printf("Multi-step failure handler called for input: %s", input.Message)

	stepErrors := ctx.StepRunErrors()
	var errorDetails string
	for stepName, errorMsg := range stepErrors {
		log.Printf("Multi-step: Step '%s' failed with error: %s", stepName, errorMsg)
		errorDetails += stepName + ": " + errorMsg + "; "
	}

	// Access successful step outputs for cleanup
	var step1Output TaskOutput
	if err := ctx.StepOutput("first-step", &step1Output); err == nil {
		log.Printf("First step completed successfully with: %s", step1Output.Message)
	}

	return FailureHandlerOutput{
		FailureHandled: true,
		ErrorDetails:   "Multi-step workflow failed: " + errorDetails,
		OriginalInput:  input.Message,
	}, nil
})
```

#### Ruby

```ruby
# This workflow will fail because the step will throw an error
# we define an onFailure step to handle this case

ON_FAILURE_WF = HATCHET.workflow(name: "OnFailureWorkflow")

ON_FAILURE_WF.task(:step1, execution_timeout: 1) do |input, ctx|
  # This step will always raise an exception
  raise ERROR_TEXT
end

# After the workflow fails, this special step will run
ON_FAILURE_WF.on_failure_task do |input, ctx|
  # We can do things like perform cleanup logic
  # or notify a user here

  # Fetch the errors from upstream step runs from the context
  puts ctx.task_run_errors.inspect

  { "status" => "success" }
end
```

The on-failure task will be executed only if any of the main tasks in the workflow fail.

### Use cases

- Performing cleanup tasks after a task failure in a workflow
- Sending notifications or alerts about the failure
- Logging additional information for debugging purposes
- Triggering a compensating action or a fallback task


---

<!-- Source: https://docs.hatchet.run/v1/task-eviction -->

# Resource Management During Waits

When a task needs to wait (for time, an event, or child results), how does Hatchet handle the worker slot? The answer depends on which pattern you're using.

#### Durable Tasks

## Task Eviction

When a durable task enters a wait, whether from `SleepFor`, `WaitForEvent`, or `WaitFor`, Hatchet **evicts** the task from the worker. The worker slot is released, the task's progress is persisted in the durable event log, and the task does not consume slots or hold resources while it is idle.

This is what makes durable tasks fundamentally different from regular tasks: a regular task consumes a slot for the entire duration of execution, even if it's just sleeping. A durable task gives the slot back the moment it starts waiting.

### How eviction works

```mermaid
graph LR
    QUEUED -->|Assigned to worker| RUNNING
    RUNNING -->|Hits SleepFor / WaitForEvent| EVICTED
    EVICTED -->|Wait completes or event arrives| QUEUED
```

1. **Task reaches a wait.** The durable task calls `SleepFor`, `WaitForEvent`, or `WaitFor`.
2. **Checkpoint is written.** Hatchet records the current progress in the durable event log.
3. **Worker slot is freed.** The task is evicted from the worker. The slot is immediately available for other tasks.
4. **Wait completes.** When the sleep expires or the expected event arrives, Hatchet re-queues the task.
5. **Task resumes on any available worker.** A worker picks up the task, replays the event log to the last checkpoint, and continues execution from where it left off.

The resumed task does not need to run on the same worker that originally started it. Any worker that has registered the task can pick it up.

### Why eviction matters

Without eviction, a task that sleeps for 24 hours would consume a slot for the entire duration, wasting capacity that could be running other work. With eviction, the slot is freed immediately.

This is especially important for:

- **Long waits** — Tasks that sleep for hours or days should not hold slots.
- **Human-in-the-loop** — Waiting for a human to approve or respond could take minutes or weeks. Eviction ensures no resources are held in the meantime.
- **Large fan-outs** — A parent task that spawns thousands of children and waits for results can release its slot while the children run, preventing deadlocks where the parent holds resources that the children need.

### Separate slot pools

Durable tasks consume slots from a **separate slot pool** than regular tasks. This prevents a common deadlock: if durable and regular tasks shared the same pool, a durable task waiting on child tasks could hold the very slot those children need to execute.

By isolating slot pools, Hatchet ensures that durable tasks waiting on children never starve the workers that need to run those children.

### Eviction and determinism

Because a task may be evicted and resumed on a different worker at any time, the code between checkpoints must be [deterministic](/v1/patterns/mixing-patterns#determinism-in-durable-tasks). On resume, Hatchet replays the event log; it does not re-execute completed operations. If the code has changed between the original run and the replay, the checkpoint sequence may not match, leading to unexpected behavior.

#### DAGs

## No Eviction Needed

DAG tasks do not require eviction because they are **never assigned to a worker until they can actually run**. A worker slot is only allocated when all of the task's conditions are met: parent tasks have completed, sleep durations have elapsed, and expected events have arrived.

This means resources are only consumed during active execution, never during waits.

### How DAG scheduling works

```mermaid
graph LR
    PENDING -->|"All conditions met (parents, sleep, events)"| QUEUED
    QUEUED -->|Assigned to worker| RUNNING
    RUNNING -->|Completes| COMPLETED
```

1. **Task is pending.** The task exists in the workflow but is not queued. No worker slot is allocated. No resources are consumed.
2. **Conditions are met.** All parent tasks have completed, any sleep duration has elapsed, and any required events have arrived.
3. **Task is queued.** Only now does Hatchet place the task in the queue for worker assignment.
4. **Task runs to completion.** A worker picks up the task, executes it, and the slot is freed.

### Why this matters

Because DAG tasks are only scheduled when ready, there is no wasted capacity:

- **Sleep conditions** — A task that waits 24 hours after its parent completes does not hold a slot. It sits in a pending state until the timer expires, then gets queued.
- **Event conditions** — A task waiting for an external event consumes no resources. When the event arrives, the task is queued and assigned a slot.
- **Parent dependencies** — Tasks waiting on upstream results are not queued until those results are available.

This is one of the advantages of DAGs: the scheduling model is simpler. You declare the conditions upfront, and Hatchet handles the timing. There is no eviction, no checkpointing, and no replay, because the task never starts until it's ready to run straight through.

> **Info:** If you need a task to start running and then pause partway through (for
>   example, to wait for an event based on intermediate results), use a [durable
>   task](/v1/patterns/durable-task-execution) instead. DAG tasks run from start
>   to finish once scheduled.


---

<!-- Source: https://docs.hatchet.run/v1/docker -->

# Dockerizing Hatchet Applications

This guide explains how to create Dockerfiles for Hatchet applications. There are examples for Python, TypeScript, Go, and Ruby applications here.

## Entrypoint Configuration for Hatchet

Before creating your Dockerfile, understand that Hatchet workers require specific entry point configuration:

1. The entry point must run code that runs the Hatchet worker. This can be done by calling the `worker.start()` method in your respective SDK.
2. Proper environment variables must be set for Hatchet SDK
3. The worker should be configured to handle your workflows using the `worker.register` method or by passing workflows into the worker constructor or factory.

## Example Dockerfiles

#### Python - Poetry

```dockerfile
FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
 POETRY_VERSION=1.4.2 \
 HATCHET_ENV=production

# Install system dependencies and Poetry
RUN apt-get update && \
 apt-get install -y curl && \
 curl -sSL https://install.python-poetry.org | python3 - && \
 ln -s /root/.local/bin/poetry /usr/local/bin/poetry && \
 apt-get clean && \
 rm -rf /var/lib/apt/lists/\*

WORKDIR /app

COPY pyproject.toml poetry.lock\* /app/

RUN poetry config virtualenvs.create false && \
 poetry install --no-interaction --no-ansi

COPY . /app

CMD ["poetry", "run", "python", "worker.py"]
```

> **Info:** If you're using a poetry script to run your worker, you can replace `poetry run python worker.py` with `poetry run <script-name>` in the CMD.

#### Python - pip

```dockerfile
FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
 HATCHET_ENV=production

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "worker.py"]
```

#### JavaScript - npm

```dockerfile
# Stage 1: Build
FROM node:18 AS builder

WORKDIR /app

COPY package\*.json ./

RUN npm ci

COPY . .

RUN npm run build

# Stage 2: Production
FROM node:22-alpine

WORKDIR /app

COPY package\*.json ./

RUN npm ci --omit=dev

COPY --from=builder /app/dist ./dist

ENV NODE_ENV=production

CMD ["node", "dist/worker.js"]
```

> **Info:** Use `npm ci` instead of `npm install` for more reliable builds. It's faster and ensures consistent installs across environments.

#### JavaScript - pnpm

```dockerfile
# Stage 1: Build
FROM node:18 AS builder

WORKDIR /app

# Install pnpm
RUN npm install -g pnpm

COPY pnpm-lock.yaml package.json ./

RUN pnpm install --frozen-lockfile

COPY . .

RUN pnpm build

# Stage 2: Production
FROM node:22-alpine

WORKDIR /app

RUN npm install -g pnpm

COPY pnpm-lock.yaml package.json ./

RUN pnpm install --frozen-lockfile --prod

COPY --from=builder /app/dist ./dist

ENV NODE_ENV=production

CMD ["node", "dist/worker.js"]
```

> **Info:** PNPM's `--frozen-lockfile` flag ensures consistent installs and fails if an update is needed.

#### JavaScript - yarn

```dockerfile
# Stage 1: Build
FROM node:18 AS builder

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install --frozen-lockfile

COPY . .

RUN yarn build

# Stage 2: Production
FROM node:22-alpine

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install --frozen-lockfile --production

COPY --from=builder /app/dist ./dist

ENV NODE_ENV=production

CMD ["node", "dist/worker.js"]

```

> **Info:** Yarn's `--frozen-lockfile` ensures your dependencies match the lock file exactly.

#### Go

```dockerfile
# Stage 1: Build
FROM golang:1.25-alpine3.21 AS builder

WORKDIR /app

COPY . .

RUN go mod download

RUN go build -o hatchet-worker .

# Stage 2: Production

FROM golang:1.25-alpine3.21

WORKDIR /app

COPY --from=builder hatchet-worker .

CMD ["/app/hatchet-worker"]

```

#### Ruby

```dockerfile
FROM ruby:3.3-slim

ENV HATCHET_ENV=production

# Install system dependencies for native gems

RUN apt-get update && \
 apt-get install -y build-essential && \
 apt-get clean && \
 rm -rf /var/lib/apt/lists/\*

WORKDIR /app

COPY Gemfile Gemfile.lock ./

RUN bundle config set --local without 'development test' && \
 bundle install

COPY . /app

CMD ["bundle", "exec", "ruby", "worker.rb"]

```

> **Info:** If you're using a Rake task or binstub to start your worker, replace the CMD with the appropriate command, e.g. `CMD ["bundle", "exec", "rake", "hatchet:worker"]`.
```


---

<!-- Source: https://docs.hatchet.run/v1/autoscaling-workers -->

# Autoscaling Workers

Hatchet provides a Task Stats API that enables you to implement autoscaling for your worker pools. By querying real-time queue depths and task distribution, you can dynamically scale workers based on actual workload demand.

## Task Stats API

The Task Stats endpoint returns current statistics for queued and running tasks across your tenant, broken down by task name, queue, and concurrency group.

### Endpoint

```
GET /api/v1/tenants/{tenantId}/task-stats
```

### Authentication

The endpoint requires Bearer token authentication using a valid API token:

```
Authorization: Bearer 
```

### Response Format

The response is a JSON object keyed by task name, with each task containing statistics for queued and running states:

```json
{
  "my-task": {
    "queued": {
      "total": 150,
      "queues": {
        "my-task:default": 100,
        "my-task:priority": 50
      },
      "concurrency": [
        {
          "expression": "input.user_id",
          "type": "GROUP_ROUND_ROBIN",
          "keys": {
            "user-123": 10,
            "user-456": 15
          }
        }
      ],
      "oldest": "2024-01-15T10:30:00Z"
    },
    "running": {
      "total": 25,
      "oldest": "2024-01-15T10:25:00Z",
      "concurrency": []
    }
  }
}
```

Each task stat includes:

- **total**: The total count of tasks in this state
- **concurrency**: Distribution across concurrency groups (if concurrency limits are configured)
- **oldest**: Timestamp of the oldest task in the specified state

These are available only for `queued` tasks:

- **queues**: A breakdown of task counts by queue name

### Example Usage

```bash
curl -H "Authorization: Bearer your-api-token-here" \
  https://cloud.onhatchet.run/api/v1/tenants/707d0855-80ab-4e1f-a156-f1c4546cbf52/task-stats
```

## Autoscaling with KEDA

[KEDA](https://keda.sh) (Kubernetes Event-driven Autoscaling) can use the Task Stats API to automatically scale your worker deployments based on queue depth.

### Setting Up a KEDA ScaledObject

Create a `ScaledObject` that queries the Hatchet Task Stats API and scales your worker deployment based on the number of queued tasks:

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: hatchet-worker-scaler
spec:
  scaleTargetRef:
    name: hatchet-worker
  minReplicaCount: 1
  maxReplicaCount: 10
  triggers:
    - type: metrics-api
      metadata:
        targetValue: "100"
        url: "https://cloud.onhatchet.run/api/v1/tenants/YOUR_TENANT_ID/task-stats"
        valueLocation: "my-task.queued.total"
        authMode: "bearer"
      authenticationRef:
        name: hatchet-api-token
---
apiVersion: v1
kind: Secret
metadata:
  name: hatchet-api-token
type: Opaque
stringData:
  token: "your-api-token-here"
---
apiVersion: keda.sh/v1alpha1
kind: TriggerAuthentication
metadata:
  name: hatchet-api-token
spec:
  secretTargetRef:
    - parameter: token
      name: hatchet-api-token
      key: token
```

> **Info:** The `valueLocation` field uses JSONPath-style notation to extract a specific
>   value from the response. Adjust `my-task` to match your actual task name.

### Scaling Based on Multiple Tasks

If you have multiple task types handled by the same worker, you can create multiple triggers or use a custom metrics endpoint that aggregates the totals:

```yaml
triggers:
  - type: metrics-api
    metadata:
      targetValue: "50"
      url: "https://cloud.onhatchet.run/api/v1/tenants/YOUR_TENANT_ID/task-stats"
      valueLocation: "task-a.queued.total"
      authMode: "bearer"
    authenticationRef:
      name: hatchet-api-token
  - type: metrics-api
    metadata:
      targetValue: "50"
      url: "https://cloud.onhatchet.run/api/v1/tenants/YOUR_TENANT_ID/task-stats"
      valueLocation: "task-b.queued.total"
      authMode: "bearer"
    authenticationRef:
      name: hatchet-api-token
```


---

<!-- Source: https://docs.hatchet.run/v1/advanced-assignment/sticky-assignment -->

# Sticky Worker Assignment (Beta)

> **Info:** This feature is currently in beta and may be subject to change.

Sticky assignment is a task property that allows you to specify that all child tasks should be assigned to the same worker for the duration of its execution. This can be useful in situations like when you need to maintain expensive local memory state across multiple tasks in a workflow or ensure that certain tasks are processed by the same worker for consistency.

> **Warning:** This feature is only compatible with long lived workers, and not webhook
>   workers.

## Setting Sticky Assignment

Sticky assignment is set on the task level by adding the `sticky` property to the task definition. When a task is marked as sticky, all steps within that task will be assigned to the same worker for the duration of the task execution.

> **Warning:** While sticky assignment can be useful in certain scenarios, it can also
>   introduce potential bottlenecks if the assigned worker becomes unavailable, or
>   if local state is not maintained when the job is picked up. Be sure to
>   consider the implications of sticky assignment when designing your tasks and
>   have a plan in place to handle local state issues.

There are two strategies for setting sticky assignment for [DAG](./dags.mdx) workflows:

- `SOFT`: All tasks in the workflow will attempt to be assigned to the same worker, but if that worker is unavailable, it will be assigned to another worker.
- `HARD`: All taks in the workflow will only be assigned to the same worker. If that worker is unavailable, the workflow run will not be assigned to another worker and will remain in a pending state until the original worker becomes available or timeout is reached. (See [Scheduling Timeouts](./timeouts.mdx#task-level-timeouts))

#### Ruby

```python
sticky_workflow = hatchet.workflow(
    name="StickyWorkflow",
    # 👀 Specify a sticky strategy when declaring the workflow
    sticky=StickyStrategy.SOFT,
)


@sticky_workflow.task()
def step1a(input: EmptyModel, ctx: Context) -> dict[str, str | None]:
    return {"worker": ctx.worker.id()}


@sticky_workflow.task()
def step1b(input: EmptyModel, ctx: Context) -> dict[str, str | None]:
    return {"worker": ctx.worker.id()}
```

#### Tab 2

```typescript
export const sticky = hatchet.task({
  name: 'sticky',
  retries: 3,
  sticky: StickyStrategy.SOFT,
  fn: async (_, ctx) => {
    // specify a child workflow to run on the same worker
    const result = await child.run(
      {
        N: 1,
      },
      { sticky: true }
    );

    return {
      result,
    };
  },
});
```

#### Tab 3

```go
func StickyDag(client *hatchet.Client) *hatchet.Workflow {
	stickyDag := client.NewWorkflow("sticky-dag",
		hatchet.WithWorkflowStickyStrategy(types.StickyStrategy_SOFT),
	)

	_ = stickyDag.NewTask("sticky-task",
		func(ctx worker.HatchetContext, input StickyInput) (interface{}, error) {
			workerId := ctx.Worker().ID()

			return &StickyResult{
				Result: workerId,
			}, nil
		},
	)

	_ = stickyDag.NewTask("sticky-task-2",
		func(ctx worker.HatchetContext, input StickyInput) (interface{}, error) {
			workerId := ctx.Worker().ID()

			return &StickyResult{
				Result: workerId,
			}, nil
		},
	)

	return stickyDag
}
```

#### Tab 4

```ruby
STICKY_WORKFLOW = HATCHET.workflow(
  name: "StickyWorkflow",
  # Specify a sticky strategy when declaring the workflow
  sticky: :soft
)

STEP1A = STICKY_WORKFLOW.task(:step1a) do |input, ctx|
  { "worker" => ctx.worker.id }
end

STEP1B = STICKY_WORKFLOW.task(:step1b) do |input, ctx|
  { "worker" => ctx.worker.id }
end
```

In this example, the `sticky` property is set to `SOFT`, which means that the task will attempt to be assigned to the same worker for the duration of its execution. If the original worker is unavailable, the task will be assigned to another worker.

## Sticky Child Tasks

It is possible to spawn child tasks on the same worker as the parent task by setting the `sticky` property to `true` in the `run` method options. This can be useful when you need to maintain local state across multiple tasks or ensure that child tasks are processed by the same worker for consistency.

However, the child task must:

1. Specify a `sticky` strategy in the child task's definition
2. Be registered with the same worker as the parent task

If either condition is not met, an error will be thrown when the child task is spawned.

#### Ruby

```python
sticky_child_workflow = hatchet.workflow(
    name="StickyChildWorkflow", sticky=StickyStrategy.SOFT
)


@sticky_workflow.task(parents=[step1a, step1b])
async def step2(input: EmptyModel, ctx: Context) -> dict[str, str | None]:
    ref = await sticky_child_workflow.aio_run_no_wait(
        options=TriggerWorkflowOptions(sticky=True)
    )

    await ref.aio_result()

    return {"worker": ctx.worker.id()}


@sticky_child_workflow.task()
def child(input: EmptyModel, ctx: Context) -> dict[str, str | None]:
    return {"worker": ctx.worker.id()}
```

#### Tab 2

```typescript
export const sticky = hatchet.task({
  name: 'sticky',
  retries: 3,
  sticky: StickyStrategy.SOFT,
  fn: async (_, ctx) => {
    // specify a child workflow to run on the same worker
    const result = await child.run(
      {
        N: 1,
      },
      { sticky: true }
    );

    return {
      result,
    };
  },
});
```

#### Tab 3

```go
func Sticky(client *hatchet.Client) *hatchet.StandaloneTask {
	sticky := client.NewStandaloneTask("sticky-task",
		func(ctx worker.HatchetContext, input StickyInput) (*StickyResult, error) {
			// Run a child workflow on the same worker
			childWorkflow := Child(client)
			childResult, err := childWorkflow.Run(ctx, ChildInput{N: 1}, hatchet.WithRunSticky(true))

			if err != nil {
				return nil, err
			}

			var childOutput ChildResult
			err = childResult.Into(&childOutput)
			if err != nil {
				return nil, err
			}

			return &StickyResult{
				Result: fmt.Sprintf("child-result-%s", childOutput.Result),
			}, nil
		},
	)

	return sticky
}
```

#### Tab 4

```ruby
STICKY_CHILD_WORKFLOW = HATCHET.workflow(
  name: "StickyChildWorkflow",
  sticky: :soft
)

STICKY_WORKFLOW.task(:step2, parents: [STEP1A, STEP1B]) do |input, ctx|
  ref = STICKY_CHILD_WORKFLOW.run_no_wait(
    options: Hatchet::TriggerWorkflowOptions.new(sticky: true)
  )

  ref.result

  { "worker" => ctx.worker.id }
end

STICKY_CHILD_WORKFLOW.task(:child) do |input, ctx|
  { "worker" => ctx.worker.id }
end
```


---

<!-- Source: https://docs.hatchet.run/v1/advanced-assignment/worker-affinity -->

# Worker Affinity Assignment (Beta)

> **Info:** This feature is currently in beta and may be subject to change.

It is often desirable to assign workflows to specific workers based on certain criteria, such as worker capabilities, resource availability, or location. Worker affinity allows you to specify that a workflow should be assigned to a specific worker based on worker label state. Labels can be set dynamically on workers to reflect their current state, such as a specific model loaded into memory or specific disk requirements.

Specific tasks can then specify desired label state to ensure that workflows are assigned to workers that meet specific criteria. If no worker meets the specified criteria, the task run will remain in a pending state until a suitable worker becomes available or the task is cancelled. (See [Scheduling Timeouts](./timeouts.mdx#task-level-timeouts))

## Specifying Worker Labels

Labels can be set on workers when they are registered with Hatchet. Labels are key-value pairs that can be used to specify worker capabilities, resource availability, or other criteria that can be used to match workflows to workers. Values can be strings or numbers, and multiple labels can be set on a worker.

#### Python

```python
worker = hatchet.worker(
    "affinity-worker",
    slots=10,
    labels={
        "model": "fancy-ai-model-v2",
        "memory": 512,
    },
    workflows=[affinity_worker_workflow],
)
worker.start()
```

#### Typescript

```typescript
const workflow = hatchet.workflow({
  name: 'affinity-workflow',
  description: 'test',
});

workflow.task({
  name: 'step1',
  fn: async (_, ctx) => {
    const results = [];

    for (let i = 0; i < 50; i++) {
      const result = await childWorkflow.run({});
      results.push(result);
    }
    console.log('Spawned 50 child workflows');
    console.log('Results:', await Promise.all(results));

    return { step1: 'step1 results!' };
  },
});
```

#### Go

```go
worker, err := client.NewWorker("affinity-worker",
	hatchet.WithWorkflows(affinityWorkflow),
	hatchet.WithSlots(10),
	hatchet.WithLabels(map[string]any{
		"model":  "fancy-ai-model-v2",
		"memory": 512,
	}),
)
```

#### Ruby

```ruby
def main
  worker = HATCHET.worker(
    "affinity-worker",
    slots: 10,
    labels: {
      "model" => "fancy-ai-model-v2",
      "memory" => 512
    },
    workflows: [AFFINITY_WORKER_WORKFLOW]
  )
  worker.start
end
```

## Specifying Step Desired Labels

You can specify desired worker label state for specific tasks in a workflow by setting the `desired_worker_labels` property on the task definition. This property is an object where the keys are the label keys and the values are objects with the following properties:

- `value`: The desired value of the label
- `comparator` (default: `EQUAL`): The comparison operator to use when matching the label value.
  - `EQUAL`: The label value must be equal to the desired value
  - `NOT_EQUAL`: The label value must not be equal to the desired value
  - `GREATER_THAN`: The label value must be greater than the desired value
  - `GREATER_THAN_OR_EQUAL`: The label value must be greater than or equal to the desired value
  - `LESS_THAN`: The label value must be less than the desired value
  - `LESS_THAN_OR_EQUAL`: The label value must be less than or equal to the desired value
- `required` (default: `true`): Whether the label is required for the task to run. If `true`, the task will remain in a pending state until a worker with the desired label state becomes available. If `false`, the worker will be prioritized based on the sum of the highest matching weights.
- `weight` (optional, default: `100`): The weight of the label. Higher weights are prioritized over lower weights when selecting a worker for the task. If multiple workers have the same highest weight, the worker with the highest sum of weights will be selected. Ignored if `required` is `true`.

#### Ruby

```python
affinity_worker_workflow = hatchet.workflow(name="AffinityWorkflow")


@affinity_worker_workflow.task(
    desired_worker_labels={
        "model": DesiredWorkerLabel(value="fancy-ai-model-v2", weight=10),
        "memory": DesiredWorkerLabel(
            value=256,
            required=True,
            comparator=WorkerLabelComparator.LESS_THAN,
        ),
    },
)
```

#### Tab 2

```typescript
const workflow = hatchet.workflow({
  name: 'affinity-workflow',
  description: 'test',
});

workflow.task({
  name: 'step1',
  fn: async (_, ctx) => {
    const results = [];

    for (let i = 0; i < 50; i++) {
      const result = await childWorkflow.run({});
      results.push(result);
    }
    console.log('Spawned 50 child workflows');
    console.log('Results:', await Promise.all(results));

    return { step1: 'step1 results!' };
  },
});
```

#### Tab 3

```go
	err = w.RegisterWorkflow(
		&worker.WorkflowJob{
			On:          worker.Events("user:create:affinity"),
			Name:        "affinity",
			Description: "affinity",
			Steps: []*worker.WorkflowStep{
				worker.Fn(func(ctx worker.HatchetContext) (result *taskOneOutput, err error) {
					return &taskOneOutput{
						Message: ctx.Worker().ID(),
					}, nil
				}).
					SetName("task-one").
					SetDesiredLabels(map[string]*types.DesiredWorkerLabel{
						"model": {
							Value:  "fancy-ai-model-v2",
							Weight: 10,
						},
						"memory": {
							Value:      512,
							Required:   true,
							Comparator: types.ComparatorPtr(types.WorkerLabelComparator_GREATER_THAN),
						},
					}),
			},
		},
	)
```

#### Tab 4

```ruby
AFFINITY_WORKER_WORKFLOW = HATCHET.workflow(name: "AffinityWorkflow")
```

> **Warning:** Use extra care when using worker affinity with [sticky assignment `HARD`
>   strategy](./sticky-assignment.mdx). In this case, it is recommended to set
>   desired labels on the first task of the workflow to ensure that the workflow
>   is assigned to a worker that meets the desired criteria and remains on that
>   worker for the duration of the workflow.

### Dynamic Worker Labels

Labels can also be set dynamically on workers using the `upsertLabels` method. This can be useful when worker state changes over time, such as when a new model is loaded into memory or when a worker's resource availability changes.

#### Ruby

```python
async def step(input: EmptyModel, ctx: Context) -> dict[str, str | None]:
    if ctx.worker.labels().get("model") != "fancy-ai-model-v2":
        ctx.worker.upsert_labels({"model": "unset"})
        # DO WORK TO EVICT OLD MODEL / LOAD NEW MODEL
        ctx.worker.upsert_labels({"model": "fancy-ai-model-v2"})

    return {"worker": ctx.worker.id()}
```

#### Tab 2

```typescript
const childWorkflow = hatchet.workflow({
  name: 'child-affinity-workflow',
  description: 'test',
});

childWorkflow.task({
  name: 'child-step1',
  desiredWorkerLabels: {
    model: {
      value: 'xyz',
      required: true,
    },
  },
  fn: async (ctx) => {
    return { childStep1: 'childStep1 results!' };
  },
});
```

#### Tab 3

```go
	err = w.RegisterWorkflow(
		&worker.WorkflowJob{
			On:          worker.Events("user:create:affinity"),
			Name:        "affinity",
			Description: "affinity",
			Steps: []*worker.WorkflowStep{
				worker.Fn(func(ctx worker.HatchetContext) (result *taskOneOutput, err error) {

    				model := ctx.Worker().GetLabels()["model"]

    				if model != "fancy-vision-model" {
    					ctx.Worker().UpsertLabels(map[string]interface{}{
    						"model": nil,
    					})
    					// Do something to load the model
            evictModel();
            loadNewModel("fancy-vision-model");
    					ctx.Worker().UpsertLabels(map[string]interface{}{
    						"model": "fancy-vision-model",
    					})
    				}

    				return &taskOneOutput{
    					Message: ctx.Worker().ID(),
    				}, nil
    			}).
    				SetName("task-one").
    				SetDesiredLabels(map[string]*types.DesiredWorkerLabel{
    					"model": {
    						Value:  "fancy-vision-model",
    						Weight: 10,
    					},
    					"memory": {
    						Value:      512,
    						Required:   true,
    						Comparator: types.WorkerLabelComparator_GREATER_THAN,
    					},
    				}),
    		},
    	},
    )

```

#### Tab 4

```ruby
AFFINITY_WORKER_WORKFLOW.task(
  :step,
  desired_worker_labels: {
    "model" => Hatchet::DesiredWorkerLabel.new(value: "fancy-ai-model-v2", weight: 10),
    "memory" => Hatchet::DesiredWorkerLabel.new(
      value: 256,
      required: true,
      comparator: :less_than
    )
  }
) do |input, ctx|
  if ctx.worker.labels["model"] != "fancy-ai-model-v2"
    ctx.worker.upsert_labels("model" => "unset")
    # DO WORK TO EVICT OLD MODEL / LOAD NEW MODEL
    ctx.worker.upsert_labels("model" => "fancy-ai-model-v2")
  end

  { "worker" => ctx.worker.id }
end
```


---

<!-- Source: https://docs.hatchet.run/v1/advanced-assignment/manual-slot-release -->

# Manual Slot Release

The Hatchet execution model sets a number of available slots for running tasks in a workflow. When a task is running, it occupies a slot, and if a worker has no available slots, it will not be able to run any more tasks concurrently.

In some cases, you may have a task in your workflow that is resource-intensive and requires exclusive access to a shared resource, such as a database connection or a GPU compute instance. To ensure that other tasks in the workflow can run concurrently, you can manually release the slot after the resource-intensive task has completed, but the task still has non-resource-intensive work to do (i.e. upload or cleanup).

> **Warning:** This is an advanced feature and should be used with caution. Manually
>   releasing the slot can have unintended side effects on system performance and
>   concurrency. For example, if the worker running the task dies, the task will
>   not be reassigned and will remain in a running state until manually
>   terminated.

## Using Manual Slot Release

You can manually release a slot in from within a running task in your workflow using the Hatchet context method `release_slot`:

#### Go

```python
slot_release_workflow = hatchet.workflow(name="SlotReleaseWorkflow")


@slot_release_workflow.task()
def step1(input: EmptyModel, ctx: Context) -> dict[str, str]:
    print("RESOURCE INTENSIVE PROCESS")
    time.sleep(10)

    # 👀 Release the slot after the resource-intensive process, so that other steps can run
    ctx.release_slot()

    print("NON RESOURCE INTENSIVE PROCESS")
    return {"status": "success"}
```

#### Ruby

```go
_ = workflow.NewTask("step1", func(ctx hatchet.Context, _ any) (*StepOutput, error) {
	fmt.Println("RESOURCE INTENSIVE PROCESS")
	time.Sleep(10 * time.Second)

	// Release the slot after the resource-intensive process,
	// so that other steps can run on this worker.
	if releaseErr := ctx.ReleaseSlot(); releaseErr != nil {
		return nil, fmt.Errorf("failed to release slot: %w", releaseErr)
	}

	fmt.Println("NON RESOURCE INTENSIVE PROCESS")

	return &StepOutput{Status: "success"}, nil
})
```

#### Tab 3

```ruby
SLOT_RELEASE_WORKFLOW = HATCHET.workflow(name: "SlotReleaseWorkflow")

SLOT_RELEASE_WORKFLOW.task(:step1) do |input, ctx|
  puts "RESOURCE INTENSIVE PROCESS"
  sleep 10

  # Release the slot after the resource-intensive process, so that other steps can run
  ctx.release_slot

  puts "NON RESOURCE INTENSIVE PROCESS"
  { "status" => "success" }
end
```

In the above examples, the `release_slot()` method is called after the resource-intensive process has completed. This allows other tasks in the workflow to start executing while the current task continues with non-resource-intensive tasks.

> **Info:** Manually releasing the slot does not terminate the current task. The task will
>   continue executing until it completes or encounters an error.

## Use Cases

Some common use cases for Manual Slot Release include:

- Performing data processing or analysis that requires significant CPU, GPU, or memory resources
- Acquiring locks or semaphores to access shared resources
- Executing long-running tasks that don't need to block other tasks after some initial work is done

By utilizing Manual Slot Release, you can optimize the concurrency and resource utilization of your workflows, allowing multiple tasks to run in parallel when possible.


---

<!-- Source: https://docs.hatchet.run/v1/logging -->

# Logging

Hatchet comes with a built-in logging view where you can push logs from your workflows. This is useful for debugging and monitoring your workflows.

#### Ruby

You can use either Python's built-in `logging` package, or the `context.log` method for more control over the logs that are sent.

## Using the built-in `logging` package

You can pass a custom logger to the `Hatchet` class when initializing it. For example:

```python
import logging

from hatchet_sdk import ClientConfig, Hatchet

logging.basicConfig(level=logging.INFO)

root_logger = logging.getLogger()

hatchet = Hatchet(
    debug=True,
    config=ClientConfig(
        logger=root_logger,
    ),
)
```

It's recommended that you pass the root logger to the `Hatchet` class, as this will ensure that all logs are captured by the Hatchet logger. If you have workflows defined in multiple files, they should be children of the root logger. For example, with the following file structure:

```
workflows/
  workflow.py
client.py
worker.py
workflow.py
```

You should pass the root logger to the `Hatchet` class in `client.py`:

```python
import logging

from hatchet_sdk import ClientConfig, Hatchet

logging.basicConfig(level=logging.INFO)

root_logger = logging.getLogger()

hatchet = Hatchet(
    debug=True,
    config=ClientConfig(
        logger=root_logger,
    ),
)
```

And then in `workflows/workflow.py`, you should create a child logger:

```python
import logging
import time

from examples.logger.client import hatchet
from hatchet_sdk import Context, EmptyModel

logger = logging.getLogger(__name__)

logging_workflow = hatchet.workflow(
    name="LoggingWorkflow",
)


@logging_workflow.task()
def root_logger(input: EmptyModel, ctx: Context) -> dict[str, str]:
    for i in range(12):
        logger.info(f"executed step1 - {i}")
        logger.info({"step1": "step1"})

        time.sleep(0.1)

    return {"status": "success"}
```

## Using the `context.log` method

You can also use the `context.log` method to log messages from your workflows. This method is available on the `Context` object that is passed to each task in your workflow. For example:

```python
@logging_workflow.task()
def context_logger(input: EmptyModel, ctx: Context) -> dict[str, str]:
    for i in range(12):
        ctx.log(f"executed step1 - {i}")
        ctx.log({"step1": "step1"})

        time.sleep(0.1)

    return {"status": "success"}
```

Each task is currently limited to 1000 log lines.

#### Tab 2

In TypeScript, there are two options for logging from your tasks. The first is to use the `ctx.log()` method (from the `Context`) to send logs:

```typescript
const workflow = hatchet.workflow({
  name: 'logger-example',
  description: 'test',
  on: {
    event: 'user:create',
  },
});

workflow.task({
  name: 'logger-step1',
  fn: async (_, ctx) => {
    // log in a for loop

    for (let i = 0; i < 10; i++) {
      ctx.logger.info(`log message ${i}`);
      await sleep(200);
    }

    return { step1: 'completed step run' };
  },
});
```

This has the benefit of being easy to use out of the box (no setup required!), but it's limited in its flexibiliy and how pluggable it is with your existing logging setup.

Hatchet also allows you to "bring your own" logger when you define a workflow:

```typescript
const logger = pino();

class PinoLogger implements Logger {
  logLevel: LogLevel;
  context: string;

  constructor(context: string, logLevel: LogLevel = 'DEBUG') {
    this.logLevel = logLevel;
    this.context = context;
  }

  debug(message: string, extra?: JsonObject): void {
    logger.debug(extra, message);
  }

  info(message: string, extra?: JsonObject): void {
    logger.info(extra, message);
  }

  green(message: string, extra?: JsonObject): void {
    logger.info(extra, `%c${message}`);
  }

  warn(message: string, error?: Error, extra?: JsonObject): void {
    logger.warn(extra, `${message} ${error}`);
  }

  error(message: string, error?: Error, extra?: JsonObject): void {
    logger.error(extra, `${message} ${error}`);
  }

  // optional util method
  util(key: string, message: string, extra?: JsonObject): void {
    // for example you may want to expose a trace method
    if (key === 'trace') {
      logger.info(extra, 'trace');
    }
  }
}

const hatchet = Hatchet.init({
  log_level: 'DEBUG',
  logger: (ctx, level) => new PinoLogger(ctx, level),
});
```

In this example, we create Pino logger that implement's Hatchet's `Logger` interface and pass it to the Hatchet client constructor. We can then use that logger in our steps:

```typescript
const workflow = hatchet.workflow({
  name: 'logger-example',
  description: 'test',
  on: {
    event: 'user:create',
  },
});

workflow.task({
  name: 'logger-step1',
  fn: async (_, ctx) => {
    // log in a for loop

    for (let i = 0; i < 10; i++) {
      ctx.logger.info(`log message ${i}`);
      await sleep(200);
    }

    return { step1: 'completed step run' };
  },
});
```

#### Tab 3

```ruby
require "hatchet-sdk"
require "logger"

logger = Logger.new($stdout)
logger.level = Logger::INFO

HATCHET = Hatchet::Client.new(debug: true) unless defined?(HATCHET)

LOGGING_WORKFLOW = HATCHET.workflow(name: "LoggingWorkflow")

LOGGING_WORKFLOW.task(:root_logger) do |input, ctx|
  12.times do |i|
    logger.info("executed step1 - #{i}")
    logger.info({ "step1" => "step1" }.inspect)

    sleep 0.1
  end

  { "status" => "success" }
end
```
```ruby
LOGGING_WORKFLOW.task(:context_logger) do |input, ctx|
  12.times do |i|
    ctx.log("executed step1 - #{i}")
    ctx.log({ "step1" => "step1" }.inspect)

    sleep 0.1
  end

  { "status" => "success" }
end
```


---

<!-- Source: https://docs.hatchet.run/v1/opentelemetry -->

# OpenTelemetry


  OpenTelemetry support is currently only available for the Python SDK.


Hatchet supports exporting traces from your tasks to an [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) to improve visibility into your Hatchet tasks.

## Usage

### Setup

Hatchet's SDK provides an instrumentor that auto-instruments Hatchet code if you opt in. Setup is straightforward:

First, install the `otel` extra with (e.g.) `pip install hatchet-sdk[otel]`. Then, import the instrumentor:

```python
from hatchet_sdk.opentelemetry.instrumentor import HatchetInstrumentor

HatchetInstrumentor(
    tracer_provider=trace_provider,
).instrument()
```

You bring your own trace provider and plug it into the `HatchetInstrumentor`, call `instrument`, and that's it!


  Check out the [OpenTelemetry
  documentation](https://opentelemetry.io/docs/languages/python/instrumentation/)
  for more information on how to set up a trace provider.


### Spans

By default, Hatchet creates spans at the following points in the lifecycle of a task run:

1. When a trigger is run on the client side, e.g. `run()` or `push()` is called.
2. When a worker handles a task event, such as starting to run the task or cancelling the task

In addition, you'll get a handful of attributes set (prefixed by `hatchet.`) on the task run events, such as the task name and the worker ID, as well as success/failure states, and so on.

Some other important notes:

1. The instrumentor will automatically propagate the trace context between task runs, so if you spawn a task from another task, the child will correctly show up as a child of its parent in the trace waterfall.
2. You can exclude specific attributes from being attached to spans by providing the `otel` configuration option on the `ClientConfig` and passing a list of `excluded_attributes`, which come from [this list](https://github.com/hatchet-dev/hatchet/blob/main/sdks/python/hatchet_sdk/utils/opentelemetry.py).

## Integrations

Hatchet's instrumentor is easy to integrate with a number of third-party tracing tools.

### Langfuse

For example, you might be interested in using [Langfuse](https://langfuse.com/) for tracing an LLM-intensive application.


  Note that this example uses Langfuse's [V3 (OTel-based)
  SDK](https://langfuse.com/docs/sdk/python/sdk-v3). See their docs for more
  information.


First, configure the Langfuse client [as described by their documentation](https://langfuse.com/docs/opentelemetry/example-python-sdk):

```python
LANGFUSE_AUTH = base64.b64encode(
    f"{os.getenv('LANGFUSE_PUBLIC_KEY')}:{os.getenv('LANGFUSE_SECRET_KEY')}".encode()
).decode()

os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = (
    os.getenv("LANGFUSE_HOST", "https://us.cloud.langfuse.com") + "/api/public/otel"
)
os.environ["OTEL_EXPORTER_OTLP_HEADERS"] = f"Authorization=Basic {LANGFUSE_AUTH}"

## Note: Langfuse sets the global tracer provider, so you don't need to worry about it
lf = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST", "https://app.langfuse.com"),
)
```

Langfuse will set the global tracer provider, so you don't have to do it manually.

Next, create an OpenAI client [using Langfuse's OpenAI wrapper `langfuse.openai` as a drop-in replacement for the default OpenAI](https://langfuse.com/docs/integrations/openai/python/get-started) client:

```python
openai = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)
```

And that's it! Now you're ready to instrument your Hatchet workers with Langfuse. For example, create a task like this:

```python
HatchetInstrumentor(
    ## Langfuse sets the global tracer provider
    tracer_provider=get_tracer_provider(),
).instrument()

hatchet = Hatchet()


@hatchet.task()
async def langfuse_task(input: EmptyModel, ctx: Context) -> dict[str, str | None]:
    ## Usage, cost, etc. of this call will be send to Langfuse
    generation = await openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Where does Anna Karenina take place?"},
        ],
    )

    location = generation.choices[0].message.content

    return {
        "location": location,
    }
```

And finally, run the task to view the Langfuse traces (cost, usage, etc.) interspersed with Hatchet's traces, in addition to any other traces you may have:

```python
tracer = get_client()


async def main() -> None:
    # Traces will send to Langfuse
    # Use `_otel_tracer` to access the OpenTelemetry tracer if you need
    # to e.g. log statuses or attributes manually.
    with tracer._otel_tracer.start_as_current_span(name="trigger") as span:
        result = await langfuse_task.aio_run()
        location = result.get("location")

        if not location:
            span.set_status(StatusCode.ERROR)
            return

        span.set_attribute("location", location)
```

When you run this task, you'll see a trace like this in Langfuse!

<img
  src="/langfuse-trace.png"
  alt="example-langfuse-trace"
  className="max-w-full mx-auto my-8"
/>


---

<!-- Source: https://docs.hatchet.run/v1/worker-healthchecks -->

# Worker Health Checks

The Python SDK allows you to enable and ping a healthcheck to check on the status of your worker.

### Usage

First, set the `HATCHET_CLIENT_WORKER_HEALTHCHECK_ENABLED` environment variable to `True`. Once that flag is set, two health check endpoints will be available (on port `8001` by default):

1. `/health` - Returns **200** when the worker listener is healthy, otherwise **503** with body `{"status":"HEALTHY"}` or `{"status":"UNHEALTHY"}`.
2. `/metrics` - A metrics endpoint intended to be used by a monitoring system like Prometheus.

### Custom Port

You can set a custom port with the `HATCHET_CLIENT_WORKER_HEALTHCHECK_PORT` environment variable, e.g. `HATCHET_CLIENT_WORKER_HEALTHCHECK_PORT=8002`.

### Event loop blocked threshold

If the worker listener process event loop becomes blocked for longer than a threshold, `/health` will return **503**.

You can configure this threshold (in seconds) with:

- `HATCHET_CLIENT_WORKER_HEALTHCHECK_EVENT_LOOP_BLOCK_THRESHOLD_SECONDS` (default: `5.0`)

#### Example request to `/health`:

```bash
curl localhost:8001/health

{"status":"HEALTHY"}
```

#### Example request to `/metrics`:

```bash
curl localhost:8001/metrics

# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 18782.0
python_gc_objects_collected_total{generation="1"} 4907.0
python_gc_objects_collected_total{generation="2"} 244.0
# HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 308.0
python_gc_collections_total{generation="1"} 27.0
python_gc_collections_total{generation="2"} 2.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="10",patchlevel="15",version="3.10.15"} 1.0
# HELP hatchet_worker_listener_health_my_worker Listener health (1 healthy, 0 unhealthy)
# TYPE hatchet_worker_listener_health_my_worker gauge
hatchet_worker_listener_health_my_worker 1.0
# HELP hatchet_worker_event_loop_lag_seconds_my_worker Event loop lag in seconds (listener process)
# TYPE hatchet_worker_event_loop_lag_seconds_my_worker gauge
hatchet_worker_event_loop_lag_seconds_my_worker 0.0
```

#### Example Prometheus Configuration for `/metrics`:

```yaml
scrape_configs:
  - job_name: "hatchet"
    scrape_interval: 5s
    static_configs:
      - targets: ["localhost:8001"]
```

#### Example Prometheus Query

An example query to check if the worker is healthy might look something like:

```
(hatchet_worker_listener_health_my_worker{instance="localhost:8001", job="hatchet"}) or vector(0)
```


---

<!-- Source: https://docs.hatchet.run/v1/prometheus-metrics -->

# Prometheus Metrics

> **Info:** Only available in the Dedicated tier and above on Hatchet Cloud, [reach
>   out](https://hatchet.run/office-hours) to upgrade.

Hatchet exports Prometheus Metrics for your tenant which can be scraped with services like Grafana and DataDog.

## Tenant Metrics

> **Warning:** Only works with v1 tenants

Metrics for individual tenants are available in Prometheus Text Format via a REST API endpoint.

### Endpoint

```
GET /api/v1/tenants/{tenantId}/prometheus-metrics
```

### Authentication

The endpoint requires Bearer token authentication using a valid API token:

```
Authorization: Bearer 
```

### Response Format

The response is returned in standard Prometheus Text Format, including:

- HELP comments describing each metric
- TYPE declarations (counter, gauge, etc.)
- Metric samples with labels and values

### Example Usage

```bash
curl -H "Authorization: Bearer your-api-token-here" \
  https://cloud.onhatchet.run/api/v1/tenants/707d0855-80ab-4e1f-a156-f1c4546cbf52/prometheus-metrics
```


---

<!-- Source: https://docs.hatchet.run/v1/additional-metadata -->

# Additional Metadata

Hatchet allows you to attach arbitrary key-value string pairs to events and task runs, which can be used for filtering, searching, or any other lookup purposes. This additional metadata is not part of the event payload or task input data but provides supplementary information for better organization and discoverability.

> **Info:** Additional metadata can be added to `Runs`, `Scheduled Runs`, `Cron Runs`, and
>   `Events`. The data is propagated from parents to children or from events to
>   runs.

You can attach additional metadata when pushing events or triggering task runs using the Hatchet client libraries:

#### Event Push

#### Ruby

```python
hatchet.event.push(
    "user:create",
    {"userId": "1234", "should_skip": False},
    options=PushEventOptions(
        additional_metadata={"source": "api"}  # Arbitrary key-value pair
    ),
)
```

#### Tab 2

```typescript
const withMetadata = await hatchet.events.push(
  'user:create',
  {
    test: 'test',
  },
  {
    additionalMetadata: {
      source: 'api', // Arbitrary key-value pair
    },
  }
);
```

#### Tab 3

```go
err = client.Events().Push(
	context.Background(),
	"user:create",
	Input{Message: "hello"},
	v0Client.WithEventMetadata(
		map[string]string{"version": "1.0.0"},
	),
)
if err != nil {
	log.Fatalf("failed to push event: %v", err)
}
```

#### Tab 4

```ruby
HATCHET.event.push(
  "user:create",
  { "userId" => "1234", "should_skip" => false },
  additional_metadata: { "source" => "api" }
)
```

#### Task Run Trigger

#### Ruby

```python
simple.run(
    options=TriggerWorkflowOptions(
        additional_metadata={"source": "api"}  # Arbitrary key-value pair
    )
)
```

#### Tab 2

```typescript
const withMetadata = simple.run(
  {
    Message: 'HeLlO WoRlD',
  },
  {
    additionalMetadata: {
      source: 'api', // Arbitrary key-value pair
    },
  }
);
```

#### Tab 3

```go
_, err = client.Run(
	context.Background(),
	"my-workflow",
	Input{Message: "hello"},
	hatchet.WithRunMetadata(
		map[string]string{"version": "1.0.0"},
	),
)
if err != nil {
	log.Fatalf("failed to run workflow: %v", err)
}
```

#### Tab 4

```ruby
SIMPLE.run(
  {},
  options: Hatchet::TriggerWorkflowOptions.new(
    additional_metadata: { "source" => "api" }
  )
)
```

## Filtering in the Dashboard

Once you've attached additional metadata to events or task runs, this data will be available in the Event and Task Run list views in the Hatchet dashboard. You can use the filter input field to search for events or task runs based on the additional metadata key-value pairs you've attached.

For example, you can filter events by the `source` metadata keys to quickly find events originating from a specific source or environment.

![Blocks](/addl-meta.gif)

## Use Cases

Some common use cases for additional metadata include:

- Tagging events or task runs with environment information (e.g., `production`, `staging`, `development`)
- Specifying the source or origin of events (e.g., `api`, `webhook`, `manual`)
- Categorizing events or task runs based on business-specific criteria (e.g., `priority`, `region`, `product`)

By leveraging additional metadata, you can enhance the organization, searchability, and discoverability of your events and task runs within Hatchet.


---

<!-- Source: https://docs.hatchet.run/v1/middleware -->

# Middleware & Dependency Injection

Middleware lets you run logic **before** and **after** every task on a client, without touching individual task definitions. Common uses include injecting request IDs, enriching inputs with shared data, encrypting/decrypting payloads, and normalizing or augmenting outputs.


  This feature is experimental, and middleware hook signatures may change in
  future releases.


#### Python

Hatchet's Python SDK uses FastAPI-style dependency injection to run logic
before tasks and inject the results as parameters. Dependencies are declared
as functions and wired into tasks with `Depends`.

#### Typescript

Middleware hooks are registered on the client with `withMiddleware` and are
fully type-safe — TypeScript sees the union of fields from the task input
type and any values returned by `before` hooks, and similarly for task
outputs and `after` hooks.

#### Go

> **Info:** Middleware support for the Go SDK is coming soon. Join our
>       [Discord](https://hatchet.run/discord) to stay up to date.

#### Ruby

In Ruby, this pattern uses callable objects (lambdas/procs) passed as `deps`
when defining tasks. Dependencies are evaluated before each task run and
made available via `ctx.deps`.

## Defining Middleware

#### Python

Define your dependency functions — they receive the workflow input and context, and their return values are injected into the task as parameters.

```python
async def async_dep(input: EmptyModel, ctx: Context) -> str:
    return ASYNC_DEPENDENCY_VALUE


def sync_dep(input: EmptyModel, ctx: Context) -> str:
    return SYNC_DEPENDENCY_VALUE


@asynccontextmanager
async def async_cm_dep(
    input: EmptyModel, ctx: Context, async_dep: Annotated[str, Depends(async_dep)]
) -> AsyncGenerator[str, None]:
    try:
        yield ASYNC_CM_DEPENDENCY_VALUE + "_" + async_dep
    finally:
        pass


@contextmanager
def sync_cm_dep(
    input: EmptyModel, ctx: Context, sync_dep: Annotated[str, Depends(sync_dep)]
) -> Generator[str, None, None]:
    try:
        yield SYNC_CM_DEPENDENCY_VALUE + "_" + sync_dep
    finally:
        pass


@contextmanager
def base_cm_dep(input: EmptyModel, ctx: Context) -> Generator[str, None, None]:
    try:
        yield CHAINED_CM_VALUE
    finally:
        pass


def chained_dep(
    input: EmptyModel, ctx: Context, base_cm: Annotated[str, Depends(base_cm_dep)]
) -> str:
    return "chained_" + base_cm


@asynccontextmanager
async def base_async_cm_dep(
    input: EmptyModel, ctx: Context
) -> AsyncGenerator[str, None]:
    try:
        yield CHAINED_ASYNC_CM_VALUE
    finally:
        pass


async def chained_async_dep(
    input: EmptyModel,
    ctx: Context,
    base_async_cm: Annotated[str, Depends(base_async_cm_dep)],
) -> str:
    return "chained_" + base_async_cm
```

#### Typescript

Create a client and attach middleware with `before` and `after` hooks.

- **`before(input, ctx)`** runs before the task. Its return value **replaces** the task input.
- **`after(output, ctx, input)`** runs after the task. Its return value **replaces** the task output.

```typescript
import { HatchetClient, HatchetMiddleware } from '@hatchet/v1';

export type GlobalInputType = {
  first: number;
  second: number;
};

export type GlobalOutputType = {
  extra: number;
};

const myMiddleware = {
  before: (input, ctx) => {
    console.log('before', input.first);
    return { ...input, dependency: 'abc-123' };
  },
  after: (output, ctx, input) => {
    return { ...output, additionalData: 2 };
  },
} satisfies HatchetMiddleware;

export const hatchetWithMiddleware = HatchetClient.init<
  GlobalInputType,
  GlobalOutputType
>().withMiddleware(myMiddleware);
```


  **Spread the original value if you want to keep it.** The return value of each hook **replaces** the input (or output) entirely — it does not shallow-merge. If you omit `...input` in a `before` hook, the original fields are lost. The same applies to `...output` in an `after` hook.

  ```typescript
      // ✅ Keeps original fields and adds `requestId`
      before: (input) => ({ ...input, requestId: crypto.randomUUID() })

      // ❌ Replaces input entirely — task only receives { requestId }
      before: (input) => ({ requestId: crypto.randomUUID() })
  ```


### Chaining Middleware

You can chain multiple `.withMiddleware()` calls to run hooks in sequence. Each `before` hook receives the return value of the previous `before` hook (or the original input for the first hook), and each `after` hook receives the return value of the previous `after` hook.

```typescript
const firstMiddleware = {
  before: (input, ctx) => {
    console.log('before', input.first);
    return { ...input, dependency: 'abc-123' };
  },
  after: (output, ctx, input) => {
    return { ...output, firstExtra: 3 };
  },
} satisfies HatchetMiddleware;

const secondMiddleware = {
  before: (input, ctx) => {
    console.log('before', input.dependency); // available from previous middleware
    return { ...input, anotherDep: true };
  },
  after: (output, ctx, input) => {
    return { ...output, secondExtra: 4 };
  },
} satisfies HatchetMiddleware;

export const hatchetWithMiddlewareChaining = HatchetClient.init()
  .withMiddleware(firstMiddleware)
  .withMiddleware(secondMiddleware);
```

#### Go

> **Info:** Middleware support for the Go SDK is coming soon. Join our [Discord](https://hatchet.run/discord) to stay up to date.

#### Ruby

Define your dependencies as callable objects (lambdas). They receive the input, context, and optionally a hash of previously resolved dependencies for chaining.

```ruby
sync_dep = ->(_input, _ctx) { SYNC_DEPENDENCY_VALUE }
async_dep = ->(_input, _ctx) { ASYNC_DEPENDENCY_VALUE }

sync_cm_dep = lambda { |_input, _ctx, deps|
  "#{SYNC_CM_DEPENDENCY_VALUE}_#{deps[:sync_dep]}"
}

async_cm_dep = lambda { |_input, _ctx, deps|
  "#{ASYNC_CM_DEPENDENCY_VALUE}_#{deps[:async_dep]}"
}

chained_dep = ->(_input, _ctx, deps) { "chained_#{CHAINED_CM_VALUE}" }
chained_async_dep = ->(_input, _ctx, deps) { "chained_#{CHAINED_ASYNC_CM_VALUE}" }
```

## How Middleware Executes

#### Python

Dependencies are resolved before each task execution. Each dependency function receives the original workflow input and the task context, and its return value is injected as a named parameter to the task function.

#### Typescript

When a task runs, the worker applies middleware hooks in this order:


### Before hooks run in registration order

Each `before` hook receives the current input and the task `Context`. Its return value **replaces** the input for the next hook (or the task itself). Returning `undefined` (or `void`) skips replacement and passes the input through unchanged.

### The task function executes

The task receives the final input after all `before` hooks have run.

### After hooks run in registration order

Each `after` hook receives the current output, the task `Context`, and the final input. Its return value **replaces** the output for the next hook (or the final result). Returning `undefined` skips replacement.


Both `before` and `after` hooks can be **async** — return a `Promise` and it will be awaited before proceeding.

> **Info:** If a middleware hook throws an error, the task run fails with that error. There is no built-in error recovery within middleware — use try/catch inside your hooks if you need graceful fallback.

### The `ctx` Parameter

The second parameter of both `before` and `after` hooks is the task `Context` object. This gives middleware access to:
- `ctx.workflowRunId` — the ID of the current workflow run
- `ctx.stepRunId` — the ID of the current step run
- `ctx.log()` — emit structured logs visible in the Hatchet dashboard
- `ctx.cancel()` — cancel the current run from within middleware

### Global Types vs Middleware Types

There are two ways extra fields end up on a task's input:

| Mechanism | Set via | Required at call site? | Available at runtime? |
|---|---|---|---|
| **Global input type** | `HatchetClient.init()` | Yes — callers must provide these fields | Yes |
| **Middleware before hook** | `.withMiddleware({ before })` | No — injected automatically by the worker | Yes |

Global input types (`T` in `init()`) represent fields that **callers must supply** when triggering a task. This is useful when you know every task must always receive certain parameters — for example, a `userId` for authentication or a `tenantId` for multi-tenant routing. By declaring these as the global type, TypeScript enforces that every caller provides them.

Middleware `before` hooks, on the other hand, inject fields that are **computed at runtime** (e.g. request IDs, decrypted secrets, fetched config) and are **not** required from callers.

```typescript
    type RequiredContext = { userId: string; orgId: string };

    const client = HatchetClient.init()
      .withMiddleware({
        before: (input) => ({
          ...input,
          resolvedAt: Date.now(),        // injected, not required from caller
          permissions: lookupPerms(input.userId), // derived from global type
        }),
      });

    // Callers MUST provide userId and orgId — TypeScript enforces this
    await myTask.run({ userId: 'usr_123', orgId: 'org_456', /* ...task fields */ });
```

#### Go

> **Info:** Middleware support for the Go SDK is coming soon. Join our [Discord](https://hatchet.run/discord) to stay up to date.

#### Ruby

Dependencies are resolved in the order they are declared in the `deps` hash. Each dependency function can optionally receive already-resolved dependencies as its third argument, enabling chaining.

## Using Middleware in Tasks

#### Python

Inject dependencies into your tasks using `Depends` and type annotations. The dependency results are passed directly as function parameters.

```python
@hatchet.task()
async def async_task_with_dependencies(
    _i: EmptyModel,
    ctx: Context,
    async_dep: Annotated[str, Depends(async_dep)],
    sync_dep: Annotated[str, Depends(sync_dep)],
    async_cm_dep: Annotated[str, Depends(async_cm_dep)],
    sync_cm_dep: Annotated[str, Depends(sync_cm_dep)],
    chained_dep: Annotated[str, Depends(chained_dep)],
    chained_async_dep: Annotated[str, Depends(chained_async_dep)],
) -> Output:
    return Output(
        sync_dep=sync_dep,
        async_dep=async_dep,
        async_cm_dep=async_cm_dep,
        sync_cm_dep=sync_cm_dep,
        chained_dep=chained_dep,
        chained_async_dep=chained_async_dep,
    )
```


  Your dependency functions must take two positional arguments: the workflow input and the `Context` (the same as any other task).


#### Typescript

Tasks created from a middleware-enabled client automatically receive the merged input and output types. There is no extra configuration needed on the task itself.

```typescript
import { hatchetWithMiddleware } from './client';

type TaskInput = {
  message: string;
};

type TaskOutput = {
  message: string;
};

export const taskWithMiddleware = hatchetWithMiddleware.task({
  name: 'task-with-middleware',
  fn: (input, _ctx) => {
    console.log('task', input.message); // string  (from TaskInput)
    console.log('task', input.first); // number  (from GlobalInputType)
    console.log('task', input.second); // number  (from GlobalInputType)
    console.log('task', input.dependency); // string  (from Pre Middleware)
    return {
      message: input.message,
      extra: 1,
    };
  },
});
// !!
```

The task's `input` type is the intersection of `TaskInput`, `GlobalInputType`, and the return type of the `before` middleware hook. The task's return type must satisfy `TaskOutput` and `GlobalOutputType`, while the caller receives the intersection of those with the `after` middleware return type.

#### Go

> **Info:** Middleware support for the Go SDK is coming soon. Join our [Discord](https://hatchet.run/discord) to stay up to date.

#### Ruby

Pass a `deps` hash when defining a task. The resolved dependency values are available inside the task block via `ctx.deps`.

```ruby
ASYNC_TASK_WITH_DEPS = HATCHET.task(
  name: "async_task_with_dependencies",
  deps: {
    sync_dep: sync_dep,
    async_dep: async_dep,
    sync_cm_dep: sync_cm_dep,
    async_cm_dep: async_cm_dep,
    chained_dep: chained_dep,
    chained_async_dep: chained_async_dep
  }
) do |input, ctx|
  {
    "sync_dep" => ctx.deps[:sync_dep],
    "async_dep" => ctx.deps[:async_dep],
    "async_cm_dep" => ctx.deps[:async_cm_dep],
    "sync_cm_dep" => ctx.deps[:sync_cm_dep],
    "chained_dep" => ctx.deps[:chained_dep],
    "chained_async_dep" => ctx.deps[:chained_async_dep]
  }
end

SYNC_TASK_WITH_DEPS = HATCHET.task(
  name: "sync_task_with_dependencies",
  deps: {
    sync_dep: sync_dep,
    async_dep: async_dep,
    sync_cm_dep: sync_cm_dep,
    async_cm_dep: async_cm_dep,
    chained_dep: chained_dep,
    chained_async_dep: chained_async_dep
  }
) do |input, ctx|
  {
    "sync_dep" => ctx.deps[:sync_dep],
    "async_dep" => ctx.deps[:async_dep],
    "async_cm_dep" => ctx.deps[:async_cm_dep],
    "sync_cm_dep" => ctx.deps[:sync_cm_dep],
    "chained_dep" => ctx.deps[:chained_dep],
    "chained_async_dep" => ctx.deps[:chained_async_dep]
  }
end

DURABLE_ASYNC_TASK_WITH_DEPS = HATCHET.durable_task(
  name: "durable_async_task_with_dependencies",
  deps: {
    sync_dep: sync_dep,
    async_dep: async_dep,
    sync_cm_dep: sync_cm_dep,
    async_cm_dep: async_cm_dep,
    chained_dep: chained_dep,
    chained_async_dep: chained_async_dep
  }
) do |input, ctx|
  {
    "sync_dep" => ctx.deps[:sync_dep],
    "async_dep" => ctx.deps[:async_dep],
    "async_cm_dep" => ctx.deps[:async_cm_dep],
    "sync_cm_dep" => ctx.deps[:sync_cm_dep],
    "chained_dep" => ctx.deps[:chained_dep],
    "chained_async_dep" => ctx.deps[:chained_async_dep]
  }
end

DURABLE_SYNC_TASK_WITH_DEPS = HATCHET.durable_task(
  name: "durable_sync_task_with_dependencies",
  deps: {
    sync_dep: sync_dep,
    async_dep: async_dep,
    sync_cm_dep: sync_cm_dep,
    async_cm_dep: async_cm_dep,
    chained_dep: chained_dep,
    chained_async_dep: chained_async_dep
  }
) do |input, ctx|
  {
    "sync_dep" => ctx.deps[:sync_dep],
    "async_dep" => ctx.deps[:async_dep],
    "async_cm_dep" => ctx.deps[:async_cm_dep],
    "sync_cm_dep" => ctx.deps[:sync_cm_dep],
    "chained_dep" => ctx.deps[:chained_dep],
    "chained_async_dep" => ctx.deps[:chained_async_dep]
  }
end

DI_WORKFLOW = HATCHET.workflow(name: "dependency-injection-workflow")

# Workflow tasks with dependencies follow the same pattern
DI_WORKFLOW.task(:wf_task_with_dependencies) do |input, ctx|
  {
    "sync_dep" => SYNC_DEPENDENCY_VALUE,
    "async_dep" => ASYNC_DEPENDENCY_VALUE
  }
end
```

## Running a Worker

#### Python

No special worker configuration is needed — dependencies are evaluated automatically each time a task runs.

#### Typescript

Workers are created from the same middleware-enabled client. No special setup is required — the middleware hooks are applied automatically when tasks execute.

```typescript
import { hatchetWithMiddleware } from './client';
import { taskWithMiddleware } from './workflow';

async function main() {
  const worker = await hatchetWithMiddleware.worker('task-with-middleware', {
    workflows: [taskWithMiddleware],
  });

  await worker.start();
}

if (require.main === module) {
  main();
}
```

#### Go

> **Info:** Middleware support for the Go SDK is coming soon. Join our [Discord](https://hatchet.run/discord) to stay up to date.

#### Ruby

No special worker configuration is needed — dependencies are resolved automatically before each task execution.

## Practical Examples

The examples below show TypeScript middleware for common production patterns. Each can be adapted to the Python dependency injection model by extracting the same logic into a dependency function.

### End-to-End Encryption

Encrypt sensitive input fields before they reach the Hatchet server, and decrypt the output on the way back. This ensures plaintext data never leaves your worker process.

```typescript
import { HatchetClient, HatchetMiddleware } from '@hatchet/v1';
import { randomUUID, createCipheriv, createDecipheriv, randomBytes } from 'crypto';
```

> **Info:** The `before` hook decrypts incoming data so your task function works with
>   plaintext. The `after` hook encrypts the output before it is stored. The
>   encryption key never leaves the worker environment.

### Offloading Large Payloads to S3

When task inputs or outputs exceed Hatchet's payload size limit (or you simply want to keep large blobs out of the control plane), upload them to S3 and pass a signed URL instead.

```typescript
import { S3Client, PutObjectCommand, GetObjectCommand } from '@aws-sdk/client-s3';
import { getSignedUrl } from '@aws-sdk/s3-request-presigner';

const ALGORITHM = 'aes-256-gcm';
const KEY = Buffer.from(process.env.ENCRYPTION_KEY!, 'hex');

type EncryptedEnvelope = { ciphertext: string; iv: string; tag: string };

function encrypt(plaintext: string): EncryptedEnvelope {
  const iv = randomBytes(16);
  const cipher = createCipheriv(ALGORITHM, KEY, iv);
  const encrypted = Buffer.concat([cipher.update(plaintext, 'utf8'), cipher.final()]);
  return {
    ciphertext: encrypted.toString('base64'),
    iv: iv.toString('base64'),
    tag: cipher.getAuthTag().toString('base64'),
  };
}

function decrypt(ciphertext: string, iv: string, tag: string): string {
  const decipher = createDecipheriv(ALGORITHM, KEY, Buffer.from(iv, 'base64'));
  decipher.setAuthTag(Buffer.from(tag, 'base64'));
  return decipher.update(ciphertext, 'base64', 'utf8') + decipher.final('utf8');
}

type EncryptedInput = { encrypted?: EncryptedEnvelope };

const e2eEncryption: HatchetMiddleware = {
  before: (input) => {
    if (!input.encrypted) {
      return input;
    }
    const { ciphertext, iv, tag } = input.encrypted;
    const decrypted = JSON.parse(decrypt(ciphertext, iv, tag));
    return { ...input, ...decrypted, encrypted: undefined };
  },
  after: (output) => {
    const payload = JSON.stringify(output);
    return { encrypted: encrypt(payload) };
  },
};

const encryptionClient = HatchetClient.init().withMiddleware(e2eEncryption);

const s3 = new S3Client({ region: process.env.AWS_REGION });
const BUCKET = process.env.S3_BUCKET!;
const PAYLOAD_THRESHOLD = 256 * 1024; // 256 KB

async function uploadToS3(data: unknown): Promise<string> {
  const key = `hatchet-payloads/${randomUUID()}.json`;
  await s3.send(
    new PutObjectCommand({
      Bucket: BUCKET,
      Key: key,
      Body: JSON.stringify(data),
      ContentType: 'application/json',
    })
  );
  return getSignedUrl(s3, new GetObjectCommand({ Bucket: BUCKET, Key: key }), {
    expiresIn: 3600,
  });
}

async function downloadFromS3(url: string): Promise<unknown> {
  const res = await fetch(url);
  return res.json();
}

type S3Input = { s3Url?: string };

const s3Offload: HatchetMiddleware = {
  before: async (input) => {
    if (input.s3Url) {
      const restored = (await downloadFromS3(input.s3Url)) as Record<string, any>;
      return { ...restored, s3Url: undefined };
    }
    return input;
  },
  after: async (output) => {
    const serialized = JSON.stringify(output);
    if (serialized.length > PAYLOAD_THRESHOLD) {
      const url = await uploadToS3(output);
      return { s3Url: url };
    }
    return output;
  },
};

const s3Client = HatchetClient.init().withMiddleware(s3Offload);
```


  The caller is responsible for uploading oversized inputs to S3 before triggering the task. The `before` hook only handles the download side. You can use the same `uploadToS3` helper on the caller side to upload the input and pass `{ __s3Url: url }` as the task input.


## FAQ

### What is Hatchet middleware and how does it differ from Express middleware?

Hatchet middleware runs **inside the worker process** around each task invocation — not on an HTTP request path. A `before` hook transforms input before the task runs, and an `after` hook transforms output after. Unlike Express middleware, there is no `next()` function; hooks return their result directly and the runner chains them automatically.

### Can I use middleware with both tasks and workflows?

Yes. Middleware is registered on the `HatchetClient` instance, so it applies to every task created from that client — whether the task is a standalone `client.task()` or part of a multi-step `client.workflow()`. Each step in a workflow will have middleware applied independently.

### Does middleware run on the server or on the worker?

Middleware runs entirely **on the worker**. The Hatchet server never sees or executes your middleware code. This is what makes patterns like end-to-end encryption possible — plaintext data stays within your infrastructure.

### What happens if my middleware throws an error?

If a `before` or `after` hook throws (or returns a rejected `Promise`), the task run fails with that error. There is no automatic retry of middleware itself, but the task's configured retry policy will still apply, re-running the task (and its middleware) from scratch.

### Can I use async/await in middleware hooks?

Yes. Both `before` and `after` hooks can be synchronous or asynchronous. If a hook returns a `Promise`, the worker will `await` it before proceeding to the next hook or the task function.

### How do I share state between `before` and `after` hooks?

The `after` hook receives the task input (after `before` hooks have run) as its third argument. Add fields in `before` (e.g. `startedAt`, `traceId`) and read them from `input` in `after`. There is no separate shared context object — the input itself is the carrier.

### Does middleware apply to child tasks spawned via fanout?

Middleware is scoped to the **client instance**. If a child task is defined on the same middleware-enabled client, its middleware will run when that child task executes. If the child task uses a different client instance, only that client's middleware (if any) applies.

### Can I selectively skip middleware for certain tasks?

Middleware applies to **all** tasks on a given client. To skip middleware for specific tasks, create a second client without middleware and define those tasks on it. This is a deliberate design choice — middleware is a cross-cutting concern, and selective opt-out is handled at the client boundary.

### Is there a performance overhead to using middleware?

Middleware hooks are plain JavaScript functions that run in-process on the worker. The overhead is the execution time of your hook code. For lightweight operations (adding a field, logging), the overhead is negligible. For heavier operations (network calls like S3 uploads or decryption), the task's total duration will include that time, so keep hooks as efficient as possible.

### What is the difference between global types and middleware types in TypeScript?

Global types (`HatchetClient.init()`) define fields that **callers must provide** when triggering a task. Middleware types (inferred from `withMiddleware` return values) define fields that are **injected at runtime** by the worker. Both end up on the task's `input` type, but only global types appear in the caller-facing `run()` signature.

### Can I use middleware for rate limiting or authentication?

Yes. A `before` hook can check rate limits, validate API keys, or verify JWTs before the task runs. If the check fails, throw an error to abort the task. However, for rate limiting specifically, consider using Hatchet's built-in [rate limiting](/home/rate-limits) feature, which operates at the scheduling layer and is more efficient than in-worker checks.

### How do I test middleware in isolation?

Middleware hooks are plain functions — you can unit-test them directly by calling them with mock input and a mock context object. For integration tests, the e2e test pattern of creating a client, attaching middleware, defining a task, starting a worker, and asserting on the result works well. See the [middleware example on GitHub](https://github.com/hatchet-dev/hatchet/tree/main/examples/typescript/middleware) for a complete test setup.


---

<!-- Source: https://docs.hatchet.run/v1/streaming -->

# Streaming in Hatchet

Hatchet tasks can stream data back to a consumer in real-time. This has a number of valuable uses, such as streaming the results of an LLM call back from a Hatchet worker to a frontend or sending progress updates as a task chugs along.

## Publishing Stream Events

You can stream data out of a task run by using the `put_stream` (or equivalent) method on the `Context`.

#### Python

```python
anna_karenina = """
Happy families are all alike; every unhappy family is unhappy in its own way.

Everything was in confusion in the Oblonskys' house. The wife had discovered that the husband was carrying on an intrigue with a French girl, who had been a governess in their family, and she had announced to her husband that she could not go on living in the same house with him.
"""


def create_chunks(content: str, n: int) -> Generator[str, None, None]:
    for i in range(0, len(content), n):
        yield content[i : i + n]


chunks = list(create_chunks(anna_karenina, 10))


@hatchet.task()
async def stream_task(input: EmptyModel, ctx: Context) -> None:
    # 👀 Sleeping to avoid race conditions
    await asyncio.sleep(2)

    for chunk in chunks:
        await ctx.aio_put_stream(chunk)
        await asyncio.sleep(0.20)
```

#### Typescript

```typescript
const annaKarenina = `
Happy families are all alike; every unhappy family is unhappy in its own way.

Everything was in confusion in the Oblonskys' house. The wife had discovered that the husband was carrying on an intrigue with a French girl, who had been a governess in their family, and she had announced to her husband that she could not go on living in the same house with him.
`;

function* createChunks(content: string, n: number): Generator<string, void, unknown> {
  for (let i = 0; i < content.length; i += n) {
    yield content.slice(i, i + n);
  }
}

export const streamingTask = hatchet.task({
  name: 'stream-example',
  fn: async (_, ctx) => {
    await sleep(2000);

    for (const chunk of createChunks(annaKarenina, 10)) {
      ctx.putStream(chunk);
      await sleep(200);
    }
  },
});
```

#### Go

```go
const annaKarenina = `
Happy families are all alike; every unhappy family is unhappy in its own way.

Everything was in confusion in the Oblonskys' house. The wife had discovered that the husband was carrying on an intrigue with a French girl, who had been a governess in their family, and she had announced to her husband that she could not go on living in the same house with him.
`

func createChunks(content string, n int) []string {
	var chunks []string
	for i := 0; i < len(content); i += n {
		end := i + n
		if end > len(content) {
			end = len(content)
		}
		chunks = append(chunks, content[i:end])
	}
	return chunks
}

func StreamTask(ctx hatchet.Context, input StreamTaskInput) (*StreamTaskOutput, error) {
	time.Sleep(2 * time.Second)

	chunks := createChunks(annaKarenina, 10)

	for _, chunk := range chunks {
		ctx.PutStream(chunk)
		time.Sleep(200 * time.Millisecond)
	}

	return &StreamTaskOutput{
		Message: "Streaming completed",
	}, nil
}
```

#### Ruby

```ruby
ANNA_KARENINA = <<~TEXT
  Happy families are all alike; every unhappy family is unhappy in its own way.

  Everything was in confusion in the Oblonskys' house. The wife had discovered that the husband was carrying on an intrigue with a French girl, who had been a governess in their family, and she had announced to her husband that she could not go on living in the same house with him.
TEXT

STREAM_CHUNKS = ANNA_KARENINA.scan(/.{1,10}/)

STREAM_TASK = HATCHET.task(name: "stream_task") do |input, ctx|
  # Sleeping to avoid race conditions
  sleep 2

  STREAM_CHUNKS.each do |chunk|
    ctx.put_stream(chunk)
    sleep 0.20
  end
end
```

This task will stream small chunks of content through Hatchet, which can then be consumed elsewhere. Here we use some text as an example, but this is intended to replicate streaming the results of an LLM call back to a consumer.

## Consuming Streams

You can easily consume stream events by using the stream method on the workflow run ref that the various [fire-and-forget](/v1/running-your-task#fire-and-forget) methods return.

#### Python

```python
ref = await stream_task.aio_run_no_wait()

async for chunk in hatchet.runs.subscribe_to_stream(ref.workflow_run_id):
    print(chunk, flush=True, end="")
```

#### Typescript

```typescript
const ref = await streamingTask.runNoWait({});
const id = await ref.getWorkflowRunId();

for await (const content of hatchet.runs.subscribeToStream(id)) {
  process.stdout.write(content);
}
```

#### Go

```go
func main() {
	client, err := hatchet.NewClient()
	if err != nil {
		log.Fatalf("Failed to create Hatchet client: %v", err)
	}

	ctx := context.Background()

	streamingWorkflow := shared.StreamingWorkflow(client)

	workflowRun, err := streamingWorkflow.RunNoWait(ctx, shared.StreamTaskInput{})
	if err != nil {
		log.Fatalf("Failed to run workflow: %v", err)
	}

	id := workflowRun.RunId
	stream := client.Runs().SubscribeToStream(ctx, id)

	for content := range stream {
		fmt.Print(content)
	}

	fmt.Println("\nStreaming completed!")
}
```

#### Ruby

```ruby
ref = STREAM_TASK.run_no_wait

HATCHET.runs.subscribe_to_stream(ref.workflow_run_id) do |chunk|
  print chunk
end
```

In the examples above, this will result in the famous text below being gradually printed to the console, bit by bit.

```
Happy families are all alike; every unhappy family is unhappy in its own way.

Everything was in confusion in the Oblonskys' house. The wife had discovered that the husband was carrying on an intrigue with a French girl, who had been a governess in their family, and she had announced to her husband that she could not go on living in the same house with him.
```


  You must begin consuming the stream before any events are published. Any
  events published before a consumer is initialized will be dropped. In
  practice, this will not be an issue in most cases, but adding a short sleep
  before beginning streaming results back can help.


## Streaming to a Web Application

It's common to want to stream events out of a Hatchet task and back to the frontend of your application, for consumption by an end user. As mentioned before, some clear cases where this is useful would be for streaming back progress of some long-running task for a customer to monitor, or streaming back the results of an LLM call.

In both cases, we recommend using your application's backend as a proxy for the stream, where you would subscribe to the stream of events from Hatchet, and then stream events through to the frontend as they're received by the backend.

#### Python

For example, with FastAPI, you'd do the following:

```python
hatchet = Hatchet()
app = FastAPI()


@app.get("/stream")
async def stream() -> StreamingResponse:
    ref = await stream_task.aio_run_no_wait()

    return StreamingResponse(
        hatchet.runs.subscribe_to_stream(ref.workflow_run_id), media_type="text/plain"
    )
```

#### Typescript

For example, with NextJS backend-as-frontend, you'd do the following:

```typescript
export async function GET(): Promise {
  try {
    const ref = await streamingTask.runNoWait({});
    const workflowRunId = await ref.getWorkflowRunId();

    const stream = Readable.from(hatchet.runs.subscribeToStream(workflowRunId));

    return new Response(Readable.toWeb(stream), {
      headers: {
        'Content-Type': 'text/plain',
        'Cache-Control': 'no-cache',
        Connection: 'keep-alive',
      },
    });
  } catch (error) {
    return new Response('Internal Server Error', { status: 500 });
  }
}
```

#### Go

For example, with Go's built-in HTTP server, you'd do the following:

```go
func main() {
	client, err := hatchet.NewClient()
	if err != nil {
		log.Fatalf("Failed to create Hatchet client: %v", err)
	}

	streamingWorkflow := shared.StreamingWorkflow(client)

	http.HandleFunc("/stream", func(w http.ResponseWriter, r *http.Request) {
		ctx := context.Background()

		w.Header().Set("Content-Type", "text/plain")
		w.Header().Set("Cache-Control", "no-cache")
		w.Header().Set("Connection", "keep-alive")

		workflowRun, err := streamingWorkflow.RunNoWait(ctx, shared.StreamTaskInput{})
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		stream := client.Runs().SubscribeToStream(ctx, workflowRun.RunId)

		flusher, _ := w.(http.Flusher)
		for content := range stream {
			fmt.Fprint(w, content)
			if flusher != nil {
				flusher.Flush()
			}
		}
	})

	server := &http.Server{
		Addr:         ":8000",
		ReadTimeout:  5 * time.Second,
		WriteTimeout: 10 * time.Second,
	}

	if err := server.ListenAndServe(); err != nil {
		log.Println("Failed to start server:", err)
	}
}
```

#### Ruby


Then, assuming you run the server on port `8000`, running `curl -N http://localhost:8000/stream` would result in the text streaming back to your console from Hatchet through your FastAPI proxy.


---

<!-- Source: https://docs.hatchet.run/v1/environments -->

# Managing Environments with Hatchet

## Multiple Developers, One Orchestrator

When multiple developers share a single Hatchet orchestrator, conflicts can arise as workflow runs and events intermingle. Without proper isolation, one developer's workflows might interfere with another's testing or development work.

Hatchet provides three key solutions for managing this challenge: namespaces, multi-tenancy, and a local Hatchet instance.

### Solution 1: Multi-Tenancy

The easiest way to isolate environments for different developers or teams is to use Hatchet's multi-tenancy feature. Each tenant represents a separate environment with its own set of workflows and workers. To add a new tenant for each developer, create an organization and follow these steps:

1. Access the organization dropdown in the dashboard (top right)
2. Select the `+` icon next to your organization's name
3. Generate a new token for that tenant
4. Each developer configures their environment with their designated tenant token

### Solution 2: Local Hatchet Instance

If you are using Hatchet locally, you can create a local instance of Hatchet to manage your isolated local development environment. Follow instructions [here](/self-hosting/hatchet-lite) to get started.


---

<!-- Source: https://docs.hatchet.run/v1/troubleshooting/index -->

# Troubleshooting Hatchet Workers

This guide covers common issues when deploying and operating Hatchet workers.

## Quick debugging checklist

Before diving into specific issues, run through these checks:

1. **Verify your API token** — make sure `HATCHET_CLIENT_TOKEN` matches the token generated in the Hatchet dashboard for your tenant.
2. **Check worker logs** — look for connection errors, heartbeat failures, or crash traces in your worker output.
3. **Check the dashboard** — navigate to the Workers tab to see if your worker is registered and healthy.
4. **Confirm network connectivity** — workers need to reach the Hatchet engine over gRPC. Firewalls, VPNs, or missing TLS configuration can block this.
5. **Check SDK version** — ensure your SDK version is compatible with your engine version. Mismatches can cause subtle failures.

## Could not send task to worker

If you see this error in the event history of a task, it could mean several things:

1. The worker is closing its network connection while the task is being sent. This could be caused by the worker crashing or going offline.

2. The payload is too large for the worker to accept or the Hatchet engine to send. The default maximum payload size is 4MB. Consider reducing the size of the input data or output data of your tasks.

3. The worker has a large backlog of tasks in-flight on the network connection and is rejecting new tasks. This can occur if workers are geographically distant from the Hatchet engine or if there are network issues causing delays. Hatchet Cloud runs by default in `us-west-2` (Oregon, USA), so consider deploying your workers in a region close to that for the best performance.

   If you are self-hosting, you can increase the maximum backlog size via the `SERVER_GRPC_WORKER_STREAM_MAX_BACKLOG_SIZE` environment variable in your Hatchet engine configuration. The default is 20.

## No workers visible in dashboard

If you have deployed workers but they are not visible in the Hatchet dashboard, it is likely that:

1. Your API token is invalid or incorrect. Ensure that the token you are using to start the worker matches the token generated in the Hatchet dashboard for your tenant.

2. Worker heartbeats are not reaching the Hatchet engine. You will see noisy logs in the worker output if this is the case.

## Tasks stuck in QUEUED state

If tasks remain in the `QUEUED` state and never move to `RUNNING`:

1. **No workers registered for the task** — check the Workers tab in the dashboard and confirm a worker is registered that handles the task name. If you recently renamed a task, make sure the worker has been restarted with the updated code.

2. **All worker slots are full** — if every slot is occupied by other tasks, new tasks will wait in the queue. Check worker utilization in the dashboard or increase the [slot count](/v1/workers#slots).

3. **Concurrency or rate limit is blocking** — if you've configured [concurrency limits](/v1/concurrency) or [rate limits](/v1/rate-limits), tasks may be held back intentionally. Review your configuration.

## Worker keeps disconnecting

If your worker repeatedly connects and then drops:

1. **Resource exhaustion** — the worker process may be running out of memory or CPU and getting killed by the OS or orchestrator (OOM kill). Check system logs and increase resource limits.

2. **Network instability** — intermittent connectivity between the worker and the Hatchet engine will cause reconnection cycles. Check for packet loss or high latency between the worker and the engine.

3. **Graceful shutdown not configured** — if your deployment platform sends `SIGTERM` and the worker doesn't handle it, in-flight tasks may be interrupted. Ensure your worker handles shutdown signals and gives tasks time to complete.

## Phantom workers active in dashboard

This is often due to workers still running in your deployed environment. We see this most often with very long termination periods for workers, or in local development environments where worker processes are leaking. If you are in a local development environment, you can usually view running Hatchet worker processes via `ps -a | grep worker` (or whatever your entrypoint binary is called) and kill them manually.


---

<!-- Source: https://docs.hatchet.run/v1/architecture-and-guarantees -->

# Architecture & Guarantees

This page explains how Hatchet is put together, what the main components do, and what reliability guarantees you should design your workers around.

## Architecture overview

Hatchet has three main moving pieces:

- **API server**: the HTTP surface area for triggering workflows, querying state, and powering the UI
- **Engine**: schedules and dispatches work, enforces dependencies/policies, and records state transitions durably
- **Workers**: your processes that run the actual task code

State is stored durably (PostgreSQL is the source of truth). In many deployments that’s enough—no separate broker required—while self-hosted high-throughput setups can add additional components (for example, RabbitMQ) based on your needs.

Hatchet Cloud and self-hosted Hatchet share the same architecture; the difference is who runs and operates the Hatchet services.

```mermaid
graph LR
    subgraph "External (Optional)"
        EXT[Webhooks<br/>Events]
    end

    subgraph "Your Infrastructure"
        APP[Your API, App, Service, etc.]
        W[Workers]
    end

    subgraph "Hatchet"
        API[API Server]
        ENG[Engine]
        DB[(Database)]
    end

    EXT --> API
    APP <--> API
    API --> ENG
    ENG <--> DB
    API <--> DB
    ENG <-.->|gRPC| W

    classDef userInfra fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    classDef hatchet fill:#f1f8e9,stroke:#388e3c,stroke-width:2px,color:#1b5e20
    classDef external fill:#fff8e1,stroke:#f57c00,stroke-width:2px,color:#e65100

    class APP,W userInfra
    class API,ENG,DB hatchet
    class EXT external
```

## Core components

### API server

The API server is the front door to Hatchet. It’s what your application and the Hatchet UI talk to in order to:

- trigger workflows with input data
- query workflow/task state (and, where supported, subscribe to updates)
- manage resources like schedules and settings
- ingest webhooks/events (optional)

### Engine

The engine is responsible for turning “a workflow should run” into “these tasks are ready and should be executed.” In practice, it:

- evaluates workflow dependencies
- enforces policies like concurrency limits, rate limits, and priorities
- schedules ready tasks and dispatches them to connected workers
- records state transitions durably and applies retry/timeout behavior
- runs scheduled/cron workflows

Workers connect to the engine over bidirectional gRPC, which allows low-latency dispatch and frequent status updates.

### Workers

Workers are your processes. They connect to the engine, receive tasks, run your code, and report progress/results back to Hatchet.

Workers are intentionally flexible: you can run them locally, in containers, or on VMs, and you can scale workers independently from the Hatchet services. You can also run different “types” of workers (and even different languages) depending on what your system needs.

### Storage (and optional messaging)

PostgreSQL is the durable store for workflow definitions and execution state (queued/running/completed, inputs/outputs, retries, etc.). In self-hosted deployments, you can start with PostgreSQL-only and add components like RabbitMQ if you need higher throughput.

## Guarantees & tradeoffs

Hatchet aims to sit in the middle: more structure than a simple queue, but simpler to operate than a full distributed workflow system.

### Good fit for

- **Workflow orchestration** with dependencies, retries, and timeouts
- **Durable background jobs** where “don’t lose work” matters
- **Moderate to high throughput** systems (and a path to higher scale with tuning/sharding). If you’re pushing the limits, [contact us](https://hatchet.run/contact).
- **Multi-language / polyglot workers**
- **Teams already on PostgreSQL** who want operational simplicity
- **Cloud or air-gapped environments** ([Hatchet Cloud](https://cloud.onhatchet.run) or [self-hosting](/self-hosting))

### Not a good fit for

- **Extremely high throughput** without sharding/custom tuning (for example, sustaining 10,000+ tasks/sec)
- **Sub-millisecond dispatch latency** requirements
- **In-memory-only queuing** where durability is unnecessary
- **Serverless-only runtimes** (e.g. AWS Lambda / Cloud Functions) as your primary worker model

## Core reliability guarantees

### At-least-once task execution

Hatchet is **at least once**: tasks are not silently dropped, and failures retry according to your configuration. This also means **a task can run more than once**, so your task code should be **idempotent** (or otherwise safe to retry).

### Durable state transitions

Workflow state is persisted in PostgreSQL, and state transitions are performed transactionally. This helps keep dependency resolution consistent and makes the system resilient to restarts and transient failures.

### Execution policies are explicit

By default, task assignment is FIFO, and you can change execution behavior using:

- [Concurrency policies](/v1/concurrency)
- [Rate limits](/v1/rate-limits)
- [Priorities](/v1/priority)

### Stateless services; resilient workers

The engine and API server are designed to restart without losing state, which also enables horizontal scaling by running multiple instances. Workers reconnect after network interruptions and can run close to your services (or close to Hatchet) depending on your latency goals.

## Performance expectations

Real-world performance depends heavily on topology (worker ↔ engine network latency), database sizing, and workload shape.

- **Dispatch latency**: often sub-50ms with PostgreSQL-backed storage; in optimized, “hot worker” setups it can be closer to ~25ms P95.
- **Throughput**: varies by setup. PostgreSQL-only deployments often handle hundreds of tasks/sec per engine instance; higher throughput typically requires additional tuning and/or components like RabbitMQ. With tuning and sharding, Hatchet can scale into the high tens of thousands of tasks/sec—[contact us](https://hatchet.run/contact) if you want to design for that.
- **Common bottlenecks**: DB connection limits, large payloads (e.g. > 1MB), complex dependency graphs, and cross-region latency.

> **Warning:** **Not seeing expected performance?**
>
> If you're not seeing the performance you expect, please [reach out to us](https://hatchet.run/office-hours) or [join our community](https://hatchet.run/discord) to explore tuning options.

## Next Steps

- **[Quick Start](/v1/quickstart)**: set up your first Hatchet worker
- **[Self-Hosting](/self-hosting)**: deploy Hatchet on your own infrastructure


---

<!-- Source: https://docs.hatchet.run/v1/cloud-vs-oss -->

# Cloud vs OSS

Hatchet is available as **Hatchet Cloud** (managed) and as **open source** (self-hosted). The programming model is the same: you write tasks/workflows in code and run workers that connect to Hatchet.

This page helps you decide which deployment model fits your team.

## Quick decision guide

Choose **Hatchet Cloud** if you want:

- the Hatchet control plane operated for you (upgrades, scaling, backups)
- the fastest path to production
- a status page and managed incident response

Choose **self-hosted (OSS)** if you need:

- full control over infrastructure and networking
- strict data residency or air-gapped environments
- a deployment you can customize and operate with your own tooling

## What’s the same in both

- **SDK + worker model**: your workers run your code and connect to Hatchet
- **Durability + retries**: tasks are durably tracked and retry according to configuration
- **Observability surfaces**: you can inspect runs, workers, and workflow history
- **Core semantics**: the same workflows/tasks/concurrency patterns apply

## What changes (operational responsibilities)

### Hatchet Cloud (managed)

Hatchet runs and operates the Hatchet services. You bring:

- your worker processes
- your application code that triggers workflows
- your operational policies (timeouts, retries, concurrency, rate limits)

For security and compliance documentation, see the **[Hatchet Trust Center](https://trust.hatchet.run/)**. For current incidents and historical uptime, see **[status.hatchet.run](https://status.hatchet.run/)**.

### Self-hosted (OSS)

You run and operate the Hatchet services and their dependencies. Typical responsibilities include:

- provisioning and scaling the Hatchet services
- managing PostgreSQL (and any optional components you deploy)
- backups, upgrades, and monitoring
- network security and access control for the API/DB

If you’re planning production usage, start with:

- [Self Hosting](/self-hosting)
- [High Availability](/self-hosting/high-availability)
- [Security](/v1/security)

## Migrating between Cloud and self-hosted

You can move between deployment models without rewriting worker code. In practice, migration usually means:

- pointing workers and clients at a new endpoint
- swapping credentials/tokens
- validating environment-specific settings (TLS, networking, retention, etc.)

## Next steps

- **[Quickstart](/v1/quickstart)**: run a worker and trigger your first workflow
- **[Architecture & Guarantees](/v1/architecture-and-guarantees)**: understand reliability semantics and tradeoffs
- **[Self Hosting](/self-hosting)**: deploy Hatchet on your own infrastructure


---

<!-- Source: https://docs.hatchet.run/v1/security -->

# Security

This page points you to Hatchet's security resources and highlights the most important security considerations for Hatchet Cloud and self-hosted deployments.

## Trust center

Hatchet is SOC 2 Type II, HIPAA, and GDPR compliant. Company-level security practices, compliance reports, and security documentation are available at the **[Hatchet Trust Center](https://trust.hatchet.run/)**.

## Same source, same security

Hatchet Cloud and self-hosted Hatchet run the same codebase. The open source project is 100% MIT licensed and undergoes regular third-party penetration testing. Findings are remediated across both deployment models, so security improvements benefit all users equally.

## Hatchet Cloud

Hatchet Cloud is Hatchet's managed service:

- **Encryption in transit**: all API and worker traffic is encrypted with TLS. gRPC connections between workers and the engine use TLS by default.
- **Encryption at rest**: data stored in Hatchet Cloud is encrypted at rest.
- **Tenant isolation**: each tenant's data is logically isolated. Requests are authenticated and scoped to a single tenant.
- **Authentication**: API tokens are scoped per-tenant with configurable expiration. The dashboard supports SSO via Google, GitHub, and more coming soon.
- **Penetration testing**: Hatchet Cloud is regularly tested by independent security firms. Findings are tracked and remediated on a defined timeline.
- **Infrastructure**: Hatchet Cloud runs on AWS with private networking, automated patching, and centralized logging.

For the definitive controls, policies, and compliance reports, refer to the **[Hatchet Trust Center](https://trust.hatchet.run/)**.

## Self-hosted

When you self-host Hatchet, your security posture depends on how you deploy and operate the Hatchet services and their dependencies. A practical baseline:

- **Put TLS in front of the API**: terminate TLS at your ingress/load balancer (or directly on the API) and only expose it to the networks that need it.
- **Treat tokens and DB credentials as secrets**: use a secrets manager and rotate credentials; avoid committing secrets into git or baking them into images.
- **Limit network reachability**: restrict access to the Hatchet API and PostgreSQL to trusted networks (VPC, private subnets, or Kubernetes network policies).
- **Use least privilege**: run Hatchet with the minimum DB permissions needed; don't reuse "admin" DB credentials.
- **Stay current**: keep Hatchet and dependencies up to date to pick up security fixes.

See [Self Hosting](/self-hosting) for deployment and configuration guidance, or [contact us](https://hatchet.run/contact) for help.


---

<!-- Source: https://docs.hatchet.run/v1/region-availability -->

# Region availability

Hatchet Cloud is available in multiple regions so you can run workloads close to your users and data.

## Current regions

**Hatchet Cloud** ([cloud.onhatchet.run](https://cloud.onhatchet.run)) is currently deployed in **us-west-2** (Oregon).

We are expanding availability. Planned or available regions include:

| Region         | Location         | Status       |
| -------------- | ---------------- | ------------ |
| us-west-2      | Oregon (US)      | **Live**     |
| us-east-1      | N. Virginia (US) | Private Beta |
| eu-west-1      | Ireland          | Private Beta |
| ap-southeast-2 | Sydney           | Private Beta |

## Request a region

We are always open to rolling out new regions based on demand. If you need a specific region for latency or compliance, [contact us](https://hatchet.run/contact) and we can discuss availability.


---

<!-- Source: https://docs.hatchet.run/v1/uptime -->

# Uptime and status

For Hatchet Cloud availability and incident updates, use the status page. For self-hosted deployments, availability depends on your own infrastructure.

## Hatchet Cloud status page

Use **[status.hatchet.run](https://status.hatchet.run/)** for real-time status and incident history for Hatchet Cloud and related services:

- **API**: Hatchet API availability
- **Hatchet Cloud**: `cloud.onhatchet.run`
- **Website**: `hatchet.run` and documentation sites

You can also subscribe to updates (email/SMS/etc.) directly from the status page.

## Self-hosted deployments

If you self-host Hatchet, you’re responsible for uptime, monitoring, backups, and upgrade procedures.

- **Deployment guidance**: [Self Hosting](/self-hosting)
- **Redundancy & failover**: [High Availability](/self-hosting/high-availability)


---

<!-- Source: https://docs.hatchet.run/v1/developer-experience -->

# Developer experience

Hatchet is designed to be practical day-to-day: write workflows in code, run workers locally with a tight feedback loop, and debug production runs with good visibility.

## Workflows as code

You define tasks and workflows in your application code, then trigger them with input data. Hatchet handles the operational pieces you’d otherwise build yourself:

- **Durability** (work isn’t lost on restarts)
- **Retries/timeouts**
- **Concurrency and rate limiting**
- **Visibility into what ran, where, and why**

## Dashboard (UI)

The dashboard is where you go to understand “what is happening right now?”:

- **Runs**: status, inputs/outputs, and execution history
- **Workers**: connected workers and health
- **Workflows**: definitions and recent activity
- **Settings**: tenants, API tokens, configuration

It’s useful for debugging, operational checks, and ad-hoc triggers.

## CLI

The [Hatchet CLI](/reference/cli) is the fastest way to develop and operate Hatchet from your terminal:

- **`hatchet worker dev`**: run a local worker with hot reload
- **`hatchet trigger`**: trigger a workflow from the command line (handy for smoke tests)
- **`hatchet tui`**: terminal UI for runs/workers/workflows
- **`hatchet profile`**: switch between tenants and environments

See the [CLI reference](/reference/cli) for installation and the full command set.

## Coding agents (MCP)

If you use AI coding tools in your editor, Hatchet’s docs can be used via an [MCP (Model Context Protocol) server](/v1/using-coding-agents). We also publish “agent skills” (short, step-by-step playbooks) so coding agents can run common Hatchet workflows—like starting a worker, triggering a workflow, and debugging a run—without guessing at CLI usage.

See [Using Coding Agents](/v1/using-coding-agents) for setup.


---

<!-- Source: https://docs.hatchet.run/cookbooks/index -->

---
asIndexPage: true
---

import { Callout, Cards } from "nextra/components";

# Cookbooks

End-to-end examples for common use cases, with working code in Python, TypeScript, Go, and Ruby. Each cookbook builds a complete workflow you can run locally and adapt to your own project.

> **Info:** These guides assume you have the Hatchet SDK installed and a worker running.
>   If you haven't done that yet, start with [Get Started](/).

## AI


  
    Build agents that reason, act, and observe in a loop. Covers reasoning
    loops, routing, multi-agent orchestration, and parallelization.
  
  
    Pause a task for human review or approval, freeing the worker slot until the
    decision arrives. The task resumes exactly where it left off.
  
  
    Ingest documents, split into chunks, generate embeddings, and write to a
    vector database using a DAG workflow.
  
  
    Chain multiple model calls with validation, retries, and structured outputs.
    Each step is a durable task with independent retry and rate-limit controls.
  


## Data & Processing


  
    Run the same operation across a large set of items with fan-out, retry, and
    concurrency control.
  
  
    Parse PDFs and files, extract content with OCR or LLMs, validate, enrich,
    and classify using a DAG pipeline.
  
  
    Fetch, process, and store web content with retries, timeouts, rate limits,
    and cron scheduling for recurring refreshes.
  


## Troubleshooting


  
    Debug common issues with Hatchet workers, including connection failures,
    tasks stuck in queued state, and phantom workers.


---

<!-- Source: https://docs.hatchet.run/cookbooks/ai-agents/index -->

# What is an AI Agent?

An **AI agent** is a program that uses an LLM to decide what to do next at runtime. Instead of following a fixed pipeline, the agent reasons about its goal, picks a tool or action, observes the result, and loops until the goal is met. This makes agents extremely powerful, but hard to run reliably.

Agents generally fall into two categories:

- **Semi-autonomous agents** rely on pre-written code that codifies business logic or procedures. The LLM decides _which_ tool or path to take, but every action it can invoke is defined ahead of time.
- **Fully autonomous agents** can write and execute arbitrary code. The LLM generates code at runtime, runs it, and acts on the output. These agents are highly flexible but require sandboxing and careful guardrails.

You can build both with Hatchet, but most teams choose semi-autonomous agents for the majority of production workloads because they are easier to reason about, test, and run more reliably.

Agents fail in production when the process hosting them dies mid-loop, when they hold resources for hours or days while waiting on external input, or when a long-running reasoning chain exhausts a timeout. Hatchet solves these problems by making every agent a **[durable task](/v1/patterns/durable-task-execution)**.

```mermaid
sequenceDiagram
    participant U as User
    participant A as Agent (Durable Task)
    participant L as LLM
    participant T as Tool (Child Task)

    U->>A: Send query
    loop Reasoning loop
        A->>L: Call LLM
        L-->>A: Tool call / response
        A->>T: RunChild (tool execution)
        T-->>A: Result
    end
    A-->>U: Final answer
```

## How agents map to Hatchet

| Agent concept       | Hatchet primitive                                                               |
| ------------------- | ------------------------------------------------------------------------------- |
| Agent               | [Durable task](/v1/patterns/durable-task-execution)                             |
| Reasoning loop      | [Child spawning](/v1/child-spawning): task re-spawns itself until done          |
| Tool calls          | [Child tasks](/v1/child-spawning): sequential or [parallel](/v1/child-spawning) |
| Human approval gate | [WaitForEvent](/v1/events): slot freed while waiting                            |
| Routing by LLM      | `if`/`else` in code + spawn child to different workflows                        |

## Why Hatchet for agents

**Simple primitives, flexible composition.** Hatchet gives you a small set of primitives for managing state and distributing workloads. You compose them however your agent needs, and they scale reliably without custom infrastructure.

**Survives crashes.** Every step in an agent's orchestration path is checkpointed. If a worker dies, the agent resumes from the last checkpoint rather than restarting from scratch.

**Frees slots during waits.** When an agent waits for a human approval event, external event, or sleeps for a scheduled retry, the worker slot is [evicted](/v1/task-eviction) and freed. No resources are held while the agent is idle, even if the wait lasts hours or days.

**Handles streaming.** Pipe LLM tokens from inside the task to connected clients as they're generated. Hatchet manages the plumbing so you don't build your own pub/sub layer. See [Streaming](/v1/streaming).

**Controls concurrency and rate limits.** Use [`CANCEL_IN_PROGRESS`](/v1/concurrency) on a session key so new user messages cancel stale agent runs. Use [`GROUP_ROUND_ROBIN`](/v1/concurrency) to distribute work fairly across users at scale. Add [rate limits](/v1/rate-limits) to stay within external API quotas.

**Full observability.** Every child run appears in the Hatchet dashboard. You can trace the full reasoning chain: which tools were called, what the LLM returned, where the loop terminated.

## Agent patterns


  
    The core agent pattern. Reason → act → observe → repeat until done. Includes
    the evaluator-optimizer variant.
  
  
    Classify incoming requests with an LLM or rule, then route to a specialist.
  
  
    An orchestrator delegates to specialist workflows. Each specialist has its
    own prompt and tools.
  
  
    Fan out independent tool calls or sub-tasks in parallel. Aggregate results
    before the agent continues.
  
  
    Pause the agent for human approval. The slot is freed; the agent resumes
    when the event arrives.
  
  
    Pipe LLM tokens to frontends in real time.


---

<!-- Source: https://docs.hatchet.run/cookbooks/ai-agents/reasoning-loop -->

# Reasoning Loop

AI agents follow a **reason-act-observe** loop that can run for minutes or hours, repeating until the LLM determines the task is complete or a deterministic exit condition is met (max iterations, timeout, tool signal).


In Hatchet, this is implemented as a [durable task](/v1/patterns/durable-task-execution) with a loop. At each iteration, the task [spawns a child](/v1/child-spawning) to call the LLM, execute any tool calls, and determine whether additional iterations are required. Each completed iteration is checkpointed, so the agent survives crashes and worker slots are freed between iterations.

## When to use

| Scenario                                        | Fit                                                               |
| ----------------------------------------------- | ----------------------------------------------------------------- |
| Chatbot that picks tools based on user messages | Good: the loop runs until the agent has a final answer            |
| Multi-step research that may take minutes       | Good: durable execution survives long-running loops               |
| Agent that needs human approval mid-loop        | Good: combine with [Human-in-the-Loop](/guides/human-in-the-loop) |
| Fixed pipeline (prompt, generate, validate)     | Skip: use [LLM Pipelines](/guides/llm-pipelines) instead          |
| One-shot classification or extraction           | Skip: a single [task](/v1/tasks) is simpler                       |

## Step-by-step walkthrough

You'll build a durable agent task that streams tokens and survives restarts.


### Reasoning loop

Define the core loop. Each iteration calls the LLM, executes any tool calls, and checks whether the task is complete.

#### Python

```python
async def agent_reasoning_loop(query: str) -> dict:
    llm = get_llm_service()
    tools = get_tool_service()
    messages = [{"role": "user", "content": query}]
    for _ in range(10):
        resp = llm.complete(messages)
        if resp.get("done"):
            return {"response": resp["content"]}
        for tc in resp.get("tool_calls", []):
            result = tools.run(tc["name"], tc.get("args", {}))
            messages.append({"role": "tool", "content": result})
    return {"response": "Max iterations reached"}
```

#### Typescript

```typescript
async function agentReasoningLoop(query: string) {
  const messages: Array<{ role: string; content: string }> = [{ role: 'user', content: query }];
  for (let i = 0; i < 10; i++) {
    const resp = callLlm(messages);
    if (resp.done) return { response: resp.content };
    for (const tc of resp.toolCalls) {
      const result = runTool(tc.name, tc.args);
      messages.push({ role: 'tool', content: result });
    }
  }
  return { response: 'Max iterations reached' };
}
```

#### Go

```go
agentReasoningLoop := func(query string) (map[string]interface{}, error) {
	messages := []map[string]interface{}{{"role": "user", "content": query}}
	for i := 0; i < 10; i++ {
		resp := CallLLM(messages)
		if resp.Done {
			return map[string]interface{}{"response": resp.Content}, nil
		}
		for _, tc := range resp.ToolCalls {
			args := make(map[string]interface{})
			for k, v := range tc.Args {
				args[k] = v
			}
			result := RunTool(tc.Name, args)
			messages = append(messages, map[string]interface{}{"role": "tool", "content": result})
		}
	}
	return map[string]interface{}{"response": "Max iterations reached"}, nil
}
```

#### Ruby

```ruby
def agent_reasoning_loop(query)
  messages = [{ 'role' => 'user', 'content' => query }]
  10.times do
    resp = call_llm(messages)
    return { 'response' => resp['content'] } if resp['done']

    (resp['tool_calls'] || []).each do |tc|
      result = run_tool(tc['name'], tc['args'] || {})
      messages << { 'role' => 'tool', 'content' => result }
    end
  end
  { 'response' => 'Max iterations reached' }
end
```

The examples above use a mock LLM. To call a real provider, swap `get_llm_service()` with one of these. Tool execution is typically your own APIs; encapsulate them in a service module like the `get_tool_service()` helper shown above.

<!-- Could not resolve @/components/LLMIntegrationTabs.mdx -->

### Wrap it in a durable task

Create a [durable task](/v1/patterns/durable-task-execution) that invokes the reasoning loop from Step 1. Concurrency is set to `CANCEL_IN_PROGRESS` so new user messages cancel stale runs.

#### Python

```python
@hatchet.durable_task(
    name="ReasoningLoopAgent",
    concurrency=ConcurrencyExpression(
        expression="input.session_id != null ? string(input.session_id) : 'constant'",
        max_runs=1,
        limit_strategy=ConcurrencyLimitStrategy.CANCEL_IN_PROGRESS,
    ),
)
async def agent_task(input: EmptyModel, ctx: DurableContext) -> dict:
    """Agent loop: reason, act, observe. Streams output, survives restarts."""
    query = "Hello"
    if isinstance(input, dict) and input.get("query"):
        query = str(input["query"])
    elif hasattr(input, "query") and input.query:
        query = str(input.query)
    return await agent_reasoning_loop(query)
```

#### Typescript

```typescript
export const agentTask = hatchet.durableTask({
  name: 'reasoning-loop-agent',
  executionTimeout: '30m',
  concurrency: {
    expression: "input.session_id != null ? string(input.session_id) : 'constant'",
    maxRuns: 1,
    limitStrategy: ConcurrencyLimitStrategy.CANCEL_IN_PROGRESS,
  },
  fn: async (input) => {
    const query = (input as { query?: string })?.query ?? 'Hello';
    return agentReasoningLoop(query);
  },
});
```

#### Go

```go
agentTask := client.NewStandaloneDurableTask("reasoning-loop-agent", func(ctx hatchet.DurableContext, input map[string]interface{}) (map[string]interface{}, error) {
	query := "Hello"
	if q, ok := input["query"].(string); ok && q != "" {
		query = q
	}
	return agentReasoningLoop(query)
})
```

#### Ruby

```ruby
AGENT_TASK = HATCHET.durable_task(name: 'ReasoningLoopAgent') do |input, _ctx|
  query = input.is_a?(Hash) && input['query'] ? input['query'].to_s : 'Hello'
  agent_reasoning_loop(query)
end
```

### Stream the response

Emit LLM tokens from the task as they are generated. Clients subscribe to the stream and receive them in real-time. See [Streaming](/v1/streaming) for the full API.

#### Python

```python
@hatchet.durable_task(
    name="StreamingAgentTask",
    concurrency=ConcurrencyExpression(
        expression="input.session_id != null ? string(input.session_id) : 'constant'",
        max_runs=1,
        limit_strategy=ConcurrencyLimitStrategy.CANCEL_IN_PROGRESS,
    ),
)
async def streaming_agent(input: EmptyModel, ctx: DurableContext) -> dict:
    """Stream tokens to the client as they're generated."""
    tokens = ["Hello", " ", "world", "!"]
    for t in tokens:
        await ctx.aio_put_stream(t)
    return {"done": True}
```

#### Typescript

```typescript
export const streamingAgentTask = hatchet.durableTask({
  name: 'streaming-agent-task',
  executionTimeout: '30m',
  concurrency: {
    expression: "'constant'",
    maxRuns: 1,
    limitStrategy: ConcurrencyLimitStrategy.CANCEL_IN_PROGRESS,
  },
  fn: async (_, ctx) => {
    const tokens = ['Hello', ' ', 'world', '!'];
    for (const t of tokens) {
      ctx.putStream(t);
    }
    return { done: true };
  },
});
```

#### Go

```go
streamingTask := client.NewStandaloneDurableTask("streaming-agent-task", func(ctx hatchet.DurableContext, input map[string]interface{}) (map[string]interface{}, error) {
	tokens := []string{"Hello", " ", "world", "!"}
	for _, t := range tokens {
		ctx.PutStream(t)
	}
	return map[string]interface{}{"done": true}, nil
})
```

#### Ruby

```ruby
STREAMING_AGENT = HATCHET.durable_task(name: 'StreamingAgentTask') do |_input, ctx|
  %w[Hello \s world !].each { |t| ctx.put_stream(t) }
  { 'done' => true }
end
```

### Run the worker

Start the worker. The task definitions above use `CANCEL_IN_PROGRESS` concurrency so new user messages cancel stale runs. Pass `session_id` in input for per-session grouping.

#### Python

```python
worker = hatchet.worker(
    "agent-worker",
    workflows=[agent_task, streaming_agent],
    slots=5,
)
worker.start()
```

#### Typescript

```typescript
const worker = await hatchet.worker('agent-worker', {
  workflows: [agentTask, streamingAgentTask],
  slots: 5,
});
await worker.start();
```

#### Go

```go
worker, err := client.NewWorker("agent-worker",
	hatchet.WithWorkflows(agentTask, streamingTask),
	hatchet.WithSlots(5),
	hatchet.WithDurableSlots(5),
)
if err != nil {
	log.Fatalf("failed to create worker: %v", err)
}

interruptCtx, cancel := cmdutils.NewInterruptContext()
defer cancel()

if err := worker.StartBlocking(interruptCtx); err != nil {
	cancel()
	log.Fatalf("failed to start worker: %v", err)
}
```

#### Ruby

```ruby
worker = HATCHET.worker('agent-worker', slots: 5, workflows: [AGENT_TASK, STREAMING_AGENT])
worker.start
```


> **Warning:** Always set a **timeout** and **max iteration count** on agent loops. Without
>   bounds, an agent can loop indefinitely. See [Timeouts](/v1/timeouts) for
>   configuration.

## Variant: Evaluator-Optimizer

The evaluator-optimizer is a specialized reasoning loop that uses two LLM calls per iteration: one to **generate** a candidate output and one to **evaluate** it against a rubric. If the score is below a threshold, the evaluator provides feedback and the generator tries again. This trades compute cost for output quality.

| Use case            | Generator                | Evaluator                                             |
| ------------------- | ------------------------ | ----------------------------------------------------- |
| **Content writing** | Draft post/email/copy    | Score clarity, tone, length; provide edit suggestions |
| **Code generation** | Write function or query  | Run tests or linter; feed back errors                 |
| **Data extraction** | Extract fields from text | Validate against schema; flag missing fields          |
| **Translation**     | Translate text           | Back-translate and compare; score fidelity            |


### Define the generator and evaluator tasks

Create separate tasks for generation and evaluation. The generator takes a topic and optional feedback; the evaluator scores a draft.

#### Python

```python
@generator_wf.task()
async def generate_draft(input: dict, ctx: Context) -> dict:
    prompt = (
        f"Improve this draft.\n\nDraft: {input['previous_draft']}\nFeedback: {input['feedback']}"
        if input.get("feedback")
        else f"Write a social media post about \"{input['topic']}\" for {input['audience']}. Under 100 words."
    )
    return {"draft": mock_generate(prompt)}


@evaluator_wf.task()
async def evaluate_draft(input: dict, ctx: Context) -> dict:
    return mock_evaluate(input["draft"])
```

#### Typescript

```typescript
const generatorTask = hatchet.task({
  name: 'generate-draft',
  fn: async (input: GeneratorInput) => {
    const prompt = input.feedback
      ? `Improve this draft.\n\nDraft: ${input.previousDraft}\nFeedback: ${input.feedback}`
      : `Write a social media post about "${input.topic}" for ${input.audience}. Under 100 words.`;
    return { draft: mockGenerate(prompt) };
  },
});

const evaluatorTask = hatchet.task({
  name: 'evaluate-draft',
  fn: async (input: EvaluatorInput) => {
    return mockEvaluate(input.draft);
  },
});
```

#### Go

```go
generatorTask := client.NewStandaloneTask("generate-draft", func(ctx hatchet.Context, input GeneratorInput) (map[string]interface{}, error) {
	var prompt string
	if input.Feedback != nil {
		prompt = fmt.Sprintf("Improve this draft.\n\nDraft: %s\nFeedback: %s", *input.PreviousDraft, *input.Feedback)
	} else {
		prompt = fmt.Sprintf("Write a social media post about \"%s\" for %s. Under 100 words.", input.Topic, input.Audience)
	}
	return map[string]interface{}{"draft": MockGenerate(prompt)}, nil
})

evaluatorTask := client.NewStandaloneTask("evaluate-draft", func(ctx hatchet.Context, input EvaluatorInput) (map[string]interface{}, error) {
	result := MockEvaluate(input.Draft)
	return map[string]interface{}{"score": result.Score, "feedback": result.Feedback}, nil
})
```

#### Ruby

```ruby
GENERATOR_WF.task(:generate_draft) do |input, _ctx|
  prompt = if input['feedback']
             "Improve this draft.\n\nDraft: #{input['previous_draft']}\nFeedback: #{input['feedback']}"
           else
             "Write a social media post about \"#{input['topic']}\" for #{input['audience']}. Under 100 words."
           end
  { 'draft' => mock_generate(prompt) }
end

EVALUATOR_WF.task(:evaluate_draft) do |input, _ctx|
  mock_evaluate(input['draft'])
end
```

### Optimization loop

The evaluator-optimizer task loops: generate, evaluate, check score. Each generator and evaluator call is a [spawned child task](/v1/child-spawning) that is checkpointed on completion.

#### Python

```python
@hatchet.durable_task(name="EvaluatorOptimizer", execution_timeout="5m")
async def evaluator_optimizer(input: EmptyModel, ctx: DurableContext) -> dict:
    max_iterations = 3
    threshold = 0.8
    draft = ""
    feedback = ""

    for i in range(max_iterations):
        generated = await generator_wf.aio_run(
            input={
                "topic": input["topic"],
                "audience": input["audience"],
                "previous_draft": draft or None,
                "feedback": feedback or None,
            }
        )
        draft = generated["draft"]

        evaluation = await evaluator_wf.aio_run(
            input={"draft": draft, "topic": input["topic"], "audience": input["audience"]}
        )

        if evaluation["score"] >= threshold:
            return {"draft": draft, "iterations": i + 1, "score": evaluation["score"]}
        feedback = evaluation["feedback"]

    return {"draft": draft, "iterations": max_iterations, "score": -1}
```

#### Typescript

```typescript
const optimizerTask = hatchet.durableTask({
  name: 'evaluator-optimizer',
  executionTimeout: '5m',
  fn: async (input: { topic: string; audience: string }) => {
    const maxIterations = 3;
    const threshold = 0.8;
    let draft = '';
    let feedback = '';

    for (let i = 0; i < maxIterations; i++) {
      const generated = await generatorTask.run({
        topic: input.topic,
        audience: input.audience,
        previousDraft: draft || undefined,
        feedback: feedback || undefined,
      });
      draft = generated.draft;

      const evaluation = await evaluatorTask.run({
        draft,
        topic: input.topic,
        audience: input.audience,
      });

      if (evaluation.score >= threshold) {
        return { draft, iterations: i + 1, score: evaluation.score };
      }
      feedback = evaluation.feedback;
    }

    return { draft, iterations: maxIterations, score: -1 };
  },
});
```

#### Go

```go
optimizerTask := client.NewStandaloneDurableTask("evaluator-optimizer", func(ctx hatchet.DurableContext, input map[string]interface{}) (map[string]interface{}, error) {
	maxIterations := 3
	threshold := 0.8
	draft := ""
	feedback := ""
	topic := input["topic"].(string)
	audience := input["audience"].(string)

	for i := 0; i < maxIterations; i++ {
		genInput := GeneratorInput{Topic: topic, Audience: audience}
		if draft != "" {
			genInput.PreviousDraft = &draft
		}
		if feedback != "" {
			genInput.Feedback = &feedback
		}
		genResult, err := generatorTask.Run(ctx, genInput)
		if err != nil {
			return nil, err
		}
		var genData map[string]interface{}
		if err := genResult.Into(&genData); err != nil {
			return nil, err
		}
		draft = genData["draft"].(string)

		evalResult, err := evaluatorTask.Run(ctx, EvaluatorInput{Draft: draft, Topic: topic, Audience: audience})
		if err != nil {
			return nil, err
		}
		var evalData map[string]interface{}
		if err := evalResult.Into(&evalData); err != nil {
			return nil, err
		}

		score := evalData["score"].(float64)
		if score >= threshold {
			return map[string]interface{}{"draft": draft, "iterations": i + 1, "score": score}, nil
		}
		feedback = evalData["feedback"].(string)
	}

	return map[string]interface{}{"draft": draft, "iterations": maxIterations, "score": -1}, nil
})
```

#### Ruby

```ruby
OPTIMIZER_TASK = HATCHET.durable_task(name: 'EvaluatorOptimizer', execution_timeout: '5m') do |input, _ctx|
  max_iterations = 3
  threshold = 0.8
  draft = ''
  feedback = ''

  max_iterations.times do |i|
    generated = GENERATOR_WF.run(
      'topic' => input['topic'], 'audience' => input['audience'],
      'previous_draft' => draft.empty? ? nil : draft,
      'feedback' => feedback.empty? ? nil : feedback
    )
    draft = generated['draft']

    evaluation = EVALUATOR_WF.run(
      'draft' => draft, 'topic' => input['topic'], 'audience' => input['audience']
    )

    next { 'draft' => draft, 'iterations' => i + 1, 'score' => evaluation['score'] } if evaluation['score'] >= threshold

    feedback = evaluation['feedback']
  end

  { 'draft' => draft, 'iterations' => max_iterations, 'score' => -1 }
end
```


## Related Patterns


  
    The core loop pattern behind agent reasoning, where a task re-spawns itself
    until a goal is met.
  
  
    Pause agents for human feedback or scheduled retries without holding worker
    slots.
  
  
    Add approval gates to agent workflows. Pause for human review, then resume.
  
  
    Agents that spawn parallel tool calls or sub-agent tasks.
  
  
    Route agent behavior based on LLM tool call decisions or user preferences.
  


## Next Steps

- [What is an Agent?](/guides/ai-agents): overview and pattern index
- [Durable Workflows](/v1/patterns/durable-task-execution): understand checkpointing and replay
- [Streaming](/v1/streaming): set up real-time LLM output streaming
- [Concurrency Control](/v1/concurrency): configure CANCEL_IN_PROGRESS for chat agents


---

<!-- Source: https://docs.hatchet.run/cookbooks/ai-agents/routing -->

# Routing

Routing classifies an incoming request and directs it to a specialist [durable task](/v1/patterns/durable-task-execution). A single entry point handles all requests; the routing logic (an LLM call, a rule-based check, or a keyword match) determines which downstream task runs. Only one branch executes per request.

This pattern improves response quality because each specialist task has its own prompt, tools, and context optimized for that category. It also simplifies the caller: trigger one task and let the router decide where to send it.

```mermaid
flowchart TD
    R[Router Task] -->|classify| C{Category}
    C -->|support| S[Support Task]
    C -->|sales| B[Sales Task]
    C -->|billing| D[Billing Task]
    S --> O[Return result]
    B --> O
    D --> O
```

## When to use

| Scenario                                               | Fit                                                      |
| ------------------------------------------------------ | -------------------------------------------------------- |
| Customer service (support vs. sales vs. billing)       | Good: distinct domains with different prompts and tools  |
| Document processing (invoice vs. receipt vs. contract) | Good: each type needs different extraction logic         |
| Request triage (simple auto-reply vs. complex agent)   | Good: avoid expensive agent loops for easy questions     |
| All requests follow the same path                      | Skip: no benefit from routing                            |
| Routing rules are simple and known at definition time  | Use [Parent Conditions](/v1/conditions) in a DAG instead |

## How it maps to Hatchet

The router is a **[durable task](/v1/patterns/durable-task-execution)**. It spawns a classifier [child task](/v1/child-spawning) (or does classification inline), then spawns the matching specialist as a [child run](/v1/child-spawning). Since each specialist is a separate durable task, they can have their own [timeouts](/v1/timeouts), [retries](/v1/retry-policies), [rate limits](/v1/rate-limits), and [concurrency](/v1/concurrency) settings.

Routing decisions are checkpointed. If the worker dies after classification but before the specialist finishes, the router resumes and does not re-classify.

## Step-by-step walkthrough


### Define the classifier task

A separate task classifies the incoming message. This lets you observe the classification result and retry independently if the LLM fails.

#### Python

```python
@hatchet.durable_task(name="ClassifyMessage")
async def classify_message(input: EmptyModel, ctx: DurableContext) -> dict:
    return {"category": mock_classify(input["message"])}
```

#### Typescript

```typescript
const classifyTask = hatchet.durableTask({
  name: 'classify-message',
  fn: async (input: MessageInput) => {
    return { category: mockClassify(input.message) };
  },
});
```

#### Go

```go
classifyTask := client.NewStandaloneDurableTask("classify-message", func(ctx hatchet.DurableContext, input MessageInput) (map[string]interface{}, error) {
	return map[string]interface{}{"category": MockClassify(input.Message)}, nil
})
```

#### Ruby

```ruby
CLASSIFY_TASK = HATCHET.durable_task(name: 'ClassifyMessage') do |input, _ctx|
  { 'category' => mock_classify(input['message']) }
end
```

### Define the specialist tasks

Each specialist is a standalone durable task with its own prompt and tools. They run independently with their own timeout and retry settings.

#### Python

```python
@hatchet.durable_task(name="HandleSupport")
async def handle_support(input: EmptyModel, ctx: DurableContext) -> dict:
    return {"response": mock_reply(input["message"], "support"), "category": "support"}


@hatchet.durable_task(name="HandleSales")
async def handle_sales(input: EmptyModel, ctx: DurableContext) -> dict:
    return {"response": mock_reply(input["message"], "sales"), "category": "sales"}


@hatchet.durable_task(name="HandleDefault")
async def handle_default(input: EmptyModel, ctx: DurableContext) -> dict:
    return {"response": mock_reply(input["message"], "other"), "category": "other"}
```

#### Typescript

```typescript
const supportTask = hatchet.durableTask({
  name: 'handle-support',
  fn: async (input: MessageInput) => {
    return { response: mockReply(input.message, 'support'), category: 'support' };
  },
});

const salesTask = hatchet.durableTask({
  name: 'handle-sales',
  fn: async (input: MessageInput) => {
    return { response: mockReply(input.message, 'sales'), category: 'sales' };
  },
});

const defaultTask = hatchet.durableTask({
  name: 'handle-default',
  fn: async (input: MessageInput) => {
    return { response: mockReply(input.message, 'other'), category: 'other' };
  },
});
```

#### Go

```go
supportTask := client.NewStandaloneDurableTask("handle-support", func(ctx hatchet.DurableContext, input MessageInput) (map[string]interface{}, error) {
	return map[string]interface{}{"response": MockReply(input.Message, "support"), "category": "support"}, nil
})

salesTask := client.NewStandaloneDurableTask("handle-sales", func(ctx hatchet.DurableContext, input MessageInput) (map[string]interface{}, error) {
	return map[string]interface{}{"response": MockReply(input.Message, "sales"), "category": "sales"}, nil
})

defaultTask := client.NewStandaloneDurableTask("handle-default", func(ctx hatchet.DurableContext, input MessageInput) (map[string]interface{}, error) {
	return map[string]interface{}{"response": MockReply(input.Message, "other"), "category": "other"}, nil
})
```

#### Ruby

```ruby
SUPPORT_TASK = HATCHET.durable_task(name: 'HandleSupport') do |input, _ctx|
  { 'response' => mock_reply(input['message'], 'support'), 'category' => 'support' }
end

SALES_TASK = HATCHET.durable_task(name: 'HandleSales') do |input, _ctx|
  { 'response' => mock_reply(input['message'], 'sales'), 'category' => 'sales' }
end

DEFAULT_TASK = HATCHET.durable_task(name: 'HandleDefault') do |input, _ctx|
  { 'response' => mock_reply(input['message'], 'other'), 'category' => 'other' }
end
```

### Route with a durable task

The router classifies the message, then spawns the matching specialist. The classification result is checkpointed, so if the worker dies after classifying, it resumes and spawns the specialist without re-classifying.

#### Python

```python
@hatchet.durable_task(name="MessageRouter", execution_timeout="2m")
async def message_router(input: EmptyModel, ctx: DurableContext) -> dict:
    classification = await classify_message.aio_run({"message": input["message"]})

    if classification["category"] == "support":
        return await handle_support.aio_run({"message": input["message"]})
    if classification["category"] == "sales":
        return await handle_sales.aio_run({"message": input["message"]})
    return await handle_default.aio_run({"message": input["message"]})
```

#### Typescript

```typescript
const routerTask = hatchet.durableTask({
  name: 'message-router',
  executionTimeout: '2m',
  fn: async (input: MessageInput) => {
    const { category } = await classifyTask.run(input);

    switch (category) {
      case 'support':
        return supportTask.run(input);
      case 'sales':
        return salesTask.run(input);
      default:
        return defaultTask.run(input);
    }
  },
});
```

#### Go

```go
routerTask := client.NewStandaloneDurableTask("message-router", func(ctx hatchet.DurableContext, input map[string]interface{}) (map[string]interface{}, error) {
	msg := input["message"].(string)
	classResult, err := classifyTask.Run(ctx, MessageInput{Message: msg})
	if err != nil {
		return nil, err
	}
	var classData map[string]interface{}
	if err := classResult.Into(&classData); err != nil {
		return nil, err
	}

	runAndUnmarshal := func(t *hatchet.StandaloneTask) (map[string]interface{}, error) {
		tr, err := t.Run(ctx, MessageInput{Message: msg})
		if err != nil {
			return nil, err
		}
		var out map[string]interface{}
		if err := tr.Into(&out); err != nil {
			return nil, err
		}
		return out, nil
	}
	switch classData["category"].(string) {
	case "support":
		return runAndUnmarshal(supportTask)
	case "sales":
		return runAndUnmarshal(salesTask)
	default:
		return runAndUnmarshal(defaultTask)
	}
})
```

#### Ruby

```ruby
ROUTER_TASK = HATCHET.durable_task(name: 'MessageRouter', execution_timeout: '2m') do |input, _ctx|
  classification = CLASSIFY_TASK.run('message' => input['message'])

  case classification['category']
  when 'support'
    SUPPORT_TASK.run('message' => input['message'])
  when 'sales'
    SALES_TASK.run('message' => input['message'])
  else
    DEFAULT_TASK.run('message' => input['message'])
  end
end
```

### Run the worker

Register all tasks and start the worker.

#### Python

```python
worker = hatchet.worker(
    "routing-worker",
    workflows=[classify_message, handle_support, handle_sales, handle_default, message_router],
    slots=5,
)
worker.start()
```

#### Typescript

```typescript
const worker = await hatchet.worker('routing-worker', {
  workflows: [classifyTask, supportTask, salesTask, defaultTask, routerTask],
  slots: 5,
});
await worker.start();
```

#### Go

```go
worker, err := client.NewWorker("routing-worker",
	hatchet.WithWorkflows(classifyTask, supportTask, salesTask, defaultTask, routerTask),
	hatchet.WithSlots(5),
	hatchet.WithDurableSlots(5),
)
if err != nil {
	log.Fatalf("failed to create worker: %v", err)
}

interruptCtx, cancel := cmdutils.NewInterruptContext()
defer cancel()

if err := worker.StartBlocking(interruptCtx); err != nil {
	log.Fatalf("failed to start worker: %v", err)
}
```

#### Ruby

```ruby
worker = HATCHET.worker('routing-worker', slots: 5,
                                          workflows: [CLASSIFY_TASK, SUPPORT_TASK, SALES_TASK, DEFAULT_TASK, ROUTER_TASK])
worker.start
```


> **Info:** For simple routing based on input fields (not LLM classification), you can
>   skip the classify task and route directly in the durable task body based on
>   `input.type` or similar fields.

## Routing vs. DAG branching

|                       | Routing (durable task)                         | DAG Parent Conditions                                 |
| --------------------- | ---------------------------------------------- | ----------------------------------------------------- |
| **Branch decided by** | Runtime code (`if`/`else`, LLM call)           | Declared conditions on parent task output             |
| **Use when**          | Category is unknown until an LLM classifies it | Branch criteria are known at workflow definition time |
| **Observability**     | Router + specialist appear as separate runs    | All branches visible in the DAG graph                 |

## Related Patterns


  
    Like routing but with a loop: the orchestrator may call multiple specialists
    across iterations.
  
  
    DAG-level branching for when routing rules are fixed at definition time.
  
  
    An agent loop can use routing internally to pick tools per iteration.
  
  
    Fixed-sequence pipelines; route to different pipelines based on input type.
  


## Next Steps

- [Durable Task Execution](/v1/patterns/durable-task-execution): understand how the router and specialists checkpoint
- [Child Spawning](/v1/child-spawning): spawn specialist tasks from the router
- [Timeouts](/v1/timeouts): set execution timeouts on the router and each specialist
- [Retry Policies](/v1/retry-policies): configure retries for classification and specialist tasks


---

<!-- Source: https://docs.hatchet.run/cookbooks/ai-agents/multi-agent -->

# Multi-Agent

Multi-agent orchestration uses a coordinating agent that delegates work to specialist agents. Unlike [routing](/guides/ai-agents/routing) (which classifies once and calls one handler), the orchestrator runs a **reasoning loop**: it may call multiple specialists across multiple iterations, passing results between them, until the overall goal is met.

Each specialist is a separate [durable task](/v1/patterns/durable-task-execution) with its own prompt, tools, timeout, and retry settings. The orchestrator's LLM decides which specialist to call next based on the accumulated context.

```mermaid
sequenceDiagram
    participant O as Orchestrator
    participant R as Research Agent
    participant W as Writing Agent
    participant C as Code Agent

    O->>O: Decide next step
    O->>R: RunChild(research)
    R-->>O: Research results
    O->>O: Decide next step
    O->>C: RunChild(code)
    C-->>O: Code snippet
    O->>O: Decide next step
    O->>W: RunChild(writing)
    W-->>O: Final draft
    O-->>O: Done
```

## When to use

| Scenario                                                              | Fit                                                |
| --------------------------------------------------------------------- | -------------------------------------------------- |
| Complex tasks needing different expertise (research + code + writing) | Good: each specialist focuses on one domain        |
| Customer service with support, sales, and billing specialists         | Good: orchestrator picks the right expert per turn |
| Tasks where output from one specialist feeds the next                 | Good: orchestrator passes context between calls    |
| Simple tasks a single agent can handle end-to-end                     | Skip: orchestration overhead isn't worth it        |
| Specialists always run in a fixed sequence                            | Use [LLM Pipelines](/guides/llm-pipelines) instead |

## How it maps to Hatchet

The orchestrator is a **[durable task](/v1/patterns/durable-task-execution)** running a reasoning loop via [child spawning](/v1/child-spawning). Each specialist is a standalone durable task spawned as a child run. The orchestrator's LLM returns structured tool calls, and each tool name maps to a specialist task.

Because each specialist call is a child run, the orchestrator's slot is freed while specialists execute. If the orchestrator dies mid-loop, it resumes from the last checkpoint without re-running completed specialist calls.

## Step-by-step walkthrough


### Define the specialist tasks

Each specialist is a standalone durable task with its own prompt and timeout. They run independently and can be reused across different orchestrators.

#### Python

```python
@hatchet.durable_task(name="ResearchSpecialist", execution_timeout="3m")
async def research(input: EmptyModel, ctx: DurableContext) -> dict:
    return {"result": mock_specialist_llm(input["task"], "research")}


@hatchet.durable_task(name="WritingSpecialist", execution_timeout="2m")
async def write(input: EmptyModel, ctx: DurableContext) -> dict:
    return {"result": mock_specialist_llm(input["task"], "writing")}


@hatchet.durable_task(name="CodeSpecialist", execution_timeout="2m")
async def code(input: EmptyModel, ctx: DurableContext) -> dict:
    return {"result": mock_specialist_llm(input["task"], "code")}
```

#### Typescript

```typescript
const researchTask = hatchet.durableTask({
  name: 'research-specialist',
  executionTimeout: '3m',
  fn: async (input: SpecialistInput) => {
    return { result: mockSpecialistLlm(input.task, 'research') };
  },
});

const writingTask = hatchet.durableTask({
  name: 'writing-specialist',
  executionTimeout: '2m',
  fn: async (input: SpecialistInput) => {
    return { result: mockSpecialistLlm(input.task, 'writing') };
  },
});

const codeTask = hatchet.durableTask({
  name: 'code-specialist',
  executionTimeout: '2m',
  fn: async (input: SpecialistInput) => {
    return { result: mockSpecialistLlm(input.task, 'code') };
  },
});
```

#### Go

```go
researchTask := client.NewStandaloneDurableTask("research-specialist", func(ctx hatchet.DurableContext, input SpecialistInput) (map[string]interface{}, error) {
	return map[string]interface{}{"result": MockSpecialistLLM(input.Task, "research")}, nil
})

writingTask := client.NewStandaloneDurableTask("writing-specialist", func(ctx hatchet.DurableContext, input SpecialistInput) (map[string]interface{}, error) {
	return map[string]interface{}{"result": MockSpecialistLLM(input.Task, "writing")}, nil
})

codeTask := client.NewStandaloneDurableTask("code-specialist", func(ctx hatchet.DurableContext, input SpecialistInput) (map[string]interface{}, error) {
	return map[string]interface{}{"result": MockSpecialistLLM(input.Task, "code")}, nil
})
```

#### Ruby

```ruby
RESEARCH_TASK = HATCHET.durable_task(name: 'ResearchSpecialist', execution_timeout: '3m') do |input, _ctx|
  { 'result' => mock_specialist_llm(input['task'], 'research') }
end

WRITING_TASK = HATCHET.durable_task(name: 'WritingSpecialist', execution_timeout: '2m') do |input, _ctx|
  { 'result' => mock_specialist_llm(input['task'], 'writing') }
end

CODE_TASK = HATCHET.durable_task(name: 'CodeSpecialist', execution_timeout: '2m') do |input, _ctx|
  { 'result' => mock_specialist_llm(input['task'], 'code') }
end
```

### Orchestrator loop

The orchestrator runs a [reasoning loop](/guides/ai-agents/reasoning-loop): call LLM, parse tool choice, [spawn specialist](/v1/child-spawning), observe result, repeat. Context accumulates across iterations so later specialist calls have full history.

#### Python

```python
@hatchet.durable_task(name="MultiAgentOrchestrator", execution_timeout="15m")
async def orchestrator(input: EmptyModel, ctx: DurableContext) -> dict:
    messages = [{"role": "user", "content": input["goal"]}]

    for _ in range(10):
        response = mock_orchestrator_llm(messages)

        if response["done"]:
            return {"result": response["content"]}

        specialist = specialists.get(response["tool_call"]["name"])
        if not specialist:
            raise ValueError(f"Unknown specialist: {response['tool_call']['name']}")

        result = await specialist.aio_run(input={
            "task": response["tool_call"]["args"]["task"],
            "context": "\n".join(m["content"] for m in messages),
        })

        messages.append({"role": "assistant", "content": f"Called {response['tool_call']['name']}"})
        messages.append({"role": "tool", "content": result["result"]})

    return {"result": "Max iterations reached"}
```

#### Typescript

```typescript
const specialists: Record<string, typeof researchTask> = {
  research: researchTask,
  writing: writingTask,
  code: codeTask,
};

const orchestrator = hatchet.durableTask({
  name: 'multi-agent-orchestrator',
  executionTimeout: '15m',
  fn: async (input: { goal: string }) => {
    const messages: Array<{ role: string; content: string }> = [
      { role: 'user', content: input.goal },
    ];

    for (let i = 0; i < 10; i++) {
      const response = mockOrchestratorLlm(messages);

      if (response.done) return { result: response.content };

      const specialist = specialists[response.toolCall!.name];
      if (!specialist) throw new Error(`Unknown specialist: ${response.toolCall!.name}`);

      const { result } = await specialist.run({
        task: response.toolCall!.args.task,
        context: messages.map((m) => m.content).join('\n'),
      });

      messages.push(
        { role: 'assistant', content: `Called ${response.toolCall!.name}` },
        { role: 'tool', content: result }
      );
    }

    return { result: 'Max iterations reached' };
  },
});
```

#### Go

```go
orchestrator := client.NewStandaloneDurableTask("multi-agent-orchestrator", func(ctx hatchet.DurableContext, input map[string]interface{}) (map[string]interface{}, error) {
	messages := []map[string]interface{}{{"role": "user", "content": input["goal"].(string)}}

	for i := 0; i < 10; i++ {
		response := MockOrchestratorLLM(messages)

		if response.Done {
			return map[string]interface{}{"result": response.Content}, nil
		}

		specialist, ok := specialists[response.ToolCall.Name]
		if !ok {
			return nil, fmt.Errorf("unknown specialist: %s", response.ToolCall.Name)
		}

		var contextParts []string
		for _, m := range messages {
			contextParts = append(contextParts, m["content"].(string))
		}

		taskResult, err := specialist.Run(ctx, SpecialistInput{
			Task:    response.ToolCall.Args["task"],
			Context: strings.Join(contextParts, "\n"),
		})
		if err != nil {
			return nil, err
		}
		var result map[string]interface{}
		if err := taskResult.Into(&result); err != nil {
			return nil, err
		}

		messages = append(messages,
			map[string]interface{}{"role": "assistant", "content": fmt.Sprintf("Called %s", response.ToolCall.Name)},
			map[string]interface{}{"role": "tool", "content": result["result"].(string)},
		)
	}

	return map[string]interface{}{"result": "Max iterations reached"}, nil
})
```

#### Ruby

```ruby
ORCHESTRATOR = HATCHET.durable_task(name: 'MultiAgentOrchestrator', execution_timeout: '15m') do |input, _ctx|
  messages = [{ 'role' => 'user', 'content' => input['goal'] }]

  result = nil
  10.times do
    response = mock_orchestrator_llm(messages)

    if response['done']
      result = { 'result' => response['content'] }
      break
    end

    specialist = SPECIALISTS[response['tool_call']['name']]
    raise "Unknown specialist: #{response['tool_call']['name']}" unless specialist

    specialist_result = specialist.run(
      'task' => response['tool_call']['args']['task'],
      'context' => messages.map { |m| m['content'] }.join("\n")
    )

    messages << { 'role' => 'assistant', 'content' => "Called #{response['tool_call']['name']}" }
    messages << { 'role' => 'tool', 'content' => specialist_result['result'] }
  end

  result || { 'result' => 'Max iterations reached' }
end
```

### Run the worker

Register all specialists and the orchestrator, then start the worker.

#### Python

```python
worker = hatchet.worker(
    "multi-agent-worker",
    workflows=[research, write, code, orchestrator],
    slots=10,
)
worker.start()
```

#### Typescript

```typescript
const worker = await hatchet.worker('multi-agent-worker', {
  workflows: [researchTask, writingTask, codeTask, orchestrator],
  slots: 10,
});
await worker.start();
```

#### Go

```go
worker, err := client.NewWorker("multi-agent-worker",
	hatchet.WithWorkflows(researchTask, writingTask, codeTask, orchestrator),
	hatchet.WithSlots(10),
	hatchet.WithDurableSlots(5),
)
if err != nil {
	log.Fatalf("failed to create worker: %v", err)
}

interruptCtx, cancel := cmdutils.NewInterruptContext()
defer cancel()

if err := worker.StartBlocking(interruptCtx); err != nil {
	log.Fatalf("failed to start worker: %v", err)
}
```

#### Ruby

```ruby
worker = HATCHET.worker('multi-agent-worker', slots: 10, workflows: [RESEARCH_TASK, WRITING_TASK, CODE_TASK, ORCHESTRATOR])
worker.start
```


> **Warning:** Always set a **max iteration count** and **execution timeout** on the
>   orchestrator. Without bounds, the loop can call specialists indefinitely.

## Multi-agent vs. routing

|                      | Multi-agent                                       | Routing                       |
| -------------------- | ------------------------------------------------- | ----------------------------- |
| **Specialist calls** | Multiple, across loop iterations                  | One per request               |
| **Orchestration**    | Reasoning loop, LLM decides next step dynamically | Classify once, route once     |
| **Use when**         | Task needs multiple types of expertise            | Task fits a single specialist |

## Related Patterns


  
    Multi-agent is a reasoning loop where "tools" are specialist durable tasks
    instead of API calls.
  
  
    Classify once and route to one handler. Multi-agent loops and may call many.
  
  
    When multiple specialists can work independently, spawn them in parallel
    within a single iteration.
  
  
    The Hatchet primitive used to spawn specialist tasks from the orchestrator.
  


## Next Steps

- [Durable Task Execution](/v1/patterns/durable-task-execution): understand checkpointing and replay for the orchestrator
- [Child Spawning](/v1/child-spawning): spawn specialist tasks from the orchestrator loop
- [Timeouts](/v1/timeouts): set execution timeouts on the orchestrator and each specialist
- [Concurrency Control](/v1/concurrency): limit how many orchestrator runs execute in parallel


---

<!-- Source: https://docs.hatchet.run/cookbooks/ai-agents/parallelization -->

# Parallelization

Parallelization spawns multiple independent tasks at the same time and aggregates results before continuing. Inside an agent loop, this typically means running several tool calls concurrently when they don't depend on each other. At a system level, it can mean running the same input through multiple evaluators and picking the best (or majority) result.

Hatchet distributes child runs across all running workers where the task is registered. The parent's slot is [freed while children execute](/v1/task-eviction), so you don't hold resources during parallel work.

There are two common variants:

- **Sectioning**: different tasks handle different concerns in parallel (e.g., content generation + safety check).
- **Voting**: the same task runs N times and results are aggregated by majority vote or best score.

```mermaid
flowchart LR
    subgraph Sectioning
        A1[Agent] -->|spawn| S1[Content Generation]
        A1 -->|spawn| S2[Safety Check]
        S1 --> A2[Aggregate]
        S2 --> A2
    end

    subgraph Voting
        B1[Agent] -->|spawn| V1[Evaluator 1]
        B1 -->|spawn| V2[Evaluator 2]
        B1 -->|spawn| V3[Evaluator 3]
        V1 --> B2[Majority Vote]
        V2 --> B2
        V3 --> B2
    end
```

## When to use

| Scenario                                              | Fit                                                                           |
| ----------------------------------------------------- | ----------------------------------------------------------------------------- |
| Agent calls 3 independent APIs (weather, news, stock) | Good: no dependencies between calls, latency drops to max of the three        |
| Content generation + safety guardrail in parallel     | Good: sectioning, both run at once, block if unsafe                           |
| Multiple evaluators vote on content quality           | Good: voting, aggregate for more reliable decisions                           |
| Processing a batch of items (100+ documents)          | Good: see [Batch Processing](/guides/batch-processing) for large-scale fanout |
| Steps depend on each other (output of A feeds B)      | Skip: run sequentially                                                        |
| Provider rate limits are tight                        | Careful: parallel calls may hit limits; use [Rate Limits](/v1/rate-limits)    |

## How it maps to Hatchet

The parent task spawns children via [child spawning](/v1/child-spawning). Each child runs on any available worker. The parent's slot is [evicted](/v1/task-eviction) while children execute, so you're not holding resources during the parallel work. When all children complete, the parent resumes and aggregates.

## Step-by-step walkthrough


### Define the parallel tasks

Create separate tasks for each concern. These run independently and can be composed in different patterns.

#### Python

```python
@content_wf.task()
async def generate_content(input: dict, ctx: Context) -> dict:
    return {"content": mock_generate_content(input["message"])}


@safety_wf.task()
async def safety_check(input: dict, ctx: Context) -> dict:
    return mock_safety_check(input["message"])


@evaluator_wf.task()
async def evaluate_content(input: dict, ctx: Context) -> dict:
    return mock_evaluate(input["content"])
```

#### Typescript

```typescript
const contentTask = hatchet.task({
  name: 'generate-content',
  fn: async (input: MessageInput) => {
    return { content: mockGenerateContent(input.message) };
  },
});

const safetyTask = hatchet.task({
  name: 'safety-check',
  fn: async (input: MessageInput) => {
    return mockSafetyCheck(input.message);
  },
});

const evaluateTask = hatchet.task({
  name: 'evaluate-content',
  fn: async (input: { content: string }) => {
    return mockEvaluate(input.content);
  },
});
```

#### Go

```go
contentTask := client.NewStandaloneTask("generate-content", func(ctx hatchet.Context, input MessageInput) (map[string]interface{}, error) {
	return map[string]interface{}{"content": MockGenerateContent(input.Message)}, nil
})

safetyTask := client.NewStandaloneTask("safety-check", func(ctx hatchet.Context, input MessageInput) (map[string]interface{}, error) {
	result := MockSafetyCheck(input.Message)
	return map[string]interface{}{"safe": result.Safe, "reason": result.Reason}, nil
})

evaluateTask := client.NewStandaloneTask("evaluate-content", func(ctx hatchet.Context, input ContentInput) (map[string]interface{}, error) {
	result := MockEvaluateContent(input.Content)
	return map[string]interface{}{"score": result.Score, "approved": result.Approved}, nil
})
```

#### Ruby

```ruby
CONTENT_WF.task(:generate_content) do |input, _ctx|
  { 'content' => mock_generate_content(input['message']) }
end

SAFETY_WF.task(:safety_check) do |input, _ctx|
  mock_safety_check(input['message'])
end

EVALUATOR_WF.task(:evaluate_content) do |input, _ctx|
  mock_evaluate_content(input['content'])
end
```

### Sectioning (parallel concerns)

Sectioning runs different concerns in parallel. The example generates content and checks safety at the same time. If the safety check fails, the content is blocked even though generation succeeded.

#### Python

```python
@hatchet.durable_task(name="ParallelSectioning", execution_timeout="2m")
async def sectioning_task(input: EmptyModel, ctx: DurableContext) -> dict:
    content_result, safety_result = await asyncio.gather(
        content_wf.aio_run(input={"message": input["message"]}),
        safety_wf.aio_run(input={"message": input["message"]}),
    )

    if not safety_result["safe"]:
        return {"blocked": True, "reason": safety_result["reason"]}
    return {"blocked": False, "content": content_result["content"]}
```

#### Typescript

```typescript
const sectioningTask = hatchet.durableTask({
  name: 'parallel-sectioning',
  executionTimeout: '2m',
  fn: async (input: MessageInput) => {
    const [content, safety] = await Promise.all([
      contentTask.run(input),
      safetyTask.run(input),
    ]);

    if (!safety.safe) {
      return { blocked: true, reason: safety.reason };
    }
    return { blocked: false, content: content.content };
  },
});
```

#### Go

```go
sectioningTask := client.NewStandaloneDurableTask("parallel-sectioning", func(ctx hatchet.DurableContext, input map[string]interface{}) (map[string]interface{}, error) {
	msg := input["message"].(string)

	var contentTr, safetyTr *hatchet.TaskResult
	var contentErr, safetyErr error
	var wg sync.WaitGroup
	wg.Add(2)

	go func() {
		defer wg.Done()
		contentTr, contentErr = contentTask.Run(ctx, MessageInput{Message: msg})
	}()
	go func() {
		defer wg.Done()
		safetyTr, safetyErr = safetyTask.Run(ctx, MessageInput{Message: msg})
	}()
	wg.Wait()

	if contentErr != nil {
		return nil, contentErr
	}
	if safetyErr != nil {
		return nil, safetyErr
	}
	var contentResult, safetyResult map[string]interface{}
	if err := contentTr.Into(&contentResult); err != nil {
		return nil, err
	}
	if err := safetyTr.Into(&safetyResult); err != nil {
		return nil, err
	}

	if safe, ok := safetyResult["safe"].(bool); !ok || !safe {
		return map[string]interface{}{"blocked": true, "reason": safetyResult["reason"]}, nil
	}
	return map[string]interface{}{"blocked": false, "content": contentResult["content"]}, nil
})
```

#### Ruby

```ruby
SECTIONING_TASK = HATCHET.durable_task(name: 'ParallelSectioning', execution_timeout: '2m') do |input, _ctx|
  threads = []
  threads << Thread.new { CONTENT_WF.run('message' => input['message']) }
  threads << Thread.new { SAFETY_WF.run('message' => input['message']) }
  content_result, safety_result = threads.map(&:value)

  if safety_result['safe']
    { 'blocked' => false, 'content' => content_result['content'] }
  else
    { 'blocked' => true, 'reason' => safety_result['reason'] }
  end
end
```

### Voting (parallel consensus)

Voting runs the same evaluation N times and aggregates by majority or average score. This produces more reliable decisions than a single evaluation.

#### Python

```python
@hatchet.durable_task(name="ParallelVoting", execution_timeout="3m")
async def voting_task(input: EmptyModel, ctx: DurableContext) -> dict:
    votes = await asyncio.gather(
        evaluator_wf.aio_run(input={"content": input["content"]}),
        evaluator_wf.aio_run(input={"content": input["content"]}),
        evaluator_wf.aio_run(input={"content": input["content"]}),
    )

    approvals = sum(1 for v in votes if v["approved"])
    avg_score = sum(v["score"] for v in votes) / len(votes)

    return {"approved": approvals >= 2, "average_score": avg_score, "votes": len(votes)}
```

#### Typescript

```typescript
const votingTask = hatchet.durableTask({
  name: 'parallel-voting',
  executionTimeout: '3m',
  fn: async (input: { content: string }) => {
    const votes = await Promise.all([
      evaluateTask.run(input),
      evaluateTask.run(input),
      evaluateTask.run(input),
    ]);

    const approvals = votes.filter((v) => v.approved).length;
    const avgScore = votes.reduce((sum, v) => sum + v.score, 0) / votes.length;

    return {
      approved: approvals >= 2,
      averageScore: avgScore,
      votes: votes.length,
    };
  },
});
```

#### Go

```go
votingTask := client.NewStandaloneDurableTask("parallel-voting", func(ctx hatchet.DurableContext, input map[string]interface{}) (map[string]interface{}, error) {
	content := input["content"].(string)
	numVoters := 3
	taskResults := make([]*hatchet.TaskResult, numVoters)
	errs := make([]error, numVoters)

	var wg sync.WaitGroup
	for i := 0; i < numVoters; i++ {
		wg.Add(1)
		go func(idx int) {
			defer wg.Done()
			taskResults[idx], errs[idx] = evaluateTask.Run(ctx, ContentInput{Content: content})
		}(i)
	}
	wg.Wait()

	results := make([]map[string]interface{}, numVoters)
	for i := 0; i < numVoters; i++ {
		if errs[i] != nil {
			return nil, errs[i]
		}
		if err := taskResults[i].Into(&results[i]); err != nil {
			return nil, err
		}
	}

	approvals := 0
	totalScore := 0.0
	for _, r := range results {
		if approved, ok := r["approved"].(bool); ok && approved {
			approvals++
		}
		if score, ok := r["score"].(float64); ok {
			totalScore += score
		}
	}

	return map[string]interface{}{
		"approved":     approvals >= 2,
		"averageScore": totalScore / float64(numVoters),
		"votes":        numVoters,
	}, nil
})
```

#### Ruby

```ruby
VOTING_TASK = HATCHET.durable_task(name: 'ParallelVoting', execution_timeout: '3m') do |input, _ctx|
  threads = 3.times.map { Thread.new { EVALUATOR_WF.run('content' => input['content']) } }
  votes = threads.map(&:value)

  approvals = votes.count { |v| v['approved'] }
  avg_score = votes.sum { |v| v['score'] } / votes.size.to_f

  { 'approved' => approvals >= 2, 'average_score' => avg_score, 'votes' => votes.size }
end
```

### Run the worker

Register all tasks and start the worker.

#### Python

```python
worker = hatchet.worker(
    "parallelization-worker",
    workflows=[content_wf, safety_wf, evaluator_wf, sectioning_task, voting_task],
    slots=10,
)
worker.start()
```

#### Typescript

```typescript
const worker = await hatchet.worker('parallelization-worker', {
  workflows: [contentTask, safetyTask, evaluateTask, sectioningTask, votingTask],
  slots: 10,
});
await worker.start();
```

#### Go

```go
worker, err := client.NewWorker("parallelization-worker",
	hatchet.WithWorkflows(contentTask, safetyTask, evaluateTask, sectioningTask, votingTask),
	hatchet.WithSlots(10),
	hatchet.WithDurableSlots(5),
)
if err != nil {
	log.Fatalf("failed to create worker: %v", err)
}

interruptCtx, cancel := cmdutils.NewInterruptContext()
defer cancel()

if err := worker.StartBlocking(interruptCtx); err != nil {
	log.Fatalf("failed to start worker: %v", err)
}
```

#### Ruby

```ruby
worker = HATCHET.worker('parallelization-worker', slots: 10,
                                                  workflows: [CONTENT_WF, SAFETY_WF, EVALUATOR_WF, SECTIONING_TASK, VOTING_TASK])
worker.start
```


> **Info:** For large-scale parallelism (hundreds or thousands of items), see the [Batch
>   Processing](/guides/batch-processing) guide, which covers fan-out with
>   concurrency control.

## Related Patterns


  
    Large-scale fan-out with concurrency limits and progress tracking.
  
  
    Parallelization applies within one iteration of an agent loop when multiple
    tools are independent.
  
  
    Combine voting (parallel evaluators) with optimization (feedback loop) for
    higher-quality iteration.
  
  
    The Hatchet concept: spawn children in parallel, parent waits for all.
  


## Next Steps

- [Child Spawning](/v1/child-spawning): spawn parallel children from a parent task
- [Task Eviction](/v1/task-eviction): free the parent's slot while children execute
- [Rate Limits](/v1/rate-limits): throttle parallel calls to external APIs
- [Concurrency Control](/v1/concurrency): limit how many children run simultaneously


---

<!-- Source: https://docs.hatchet.run/cookbooks/human-in-the-loop -->

# Human-in-the-Loop

Human-in-the-loop [durable tasks](/v1/patterns/durable-task-execution) pause for human review or approval before continuing. An AI agent proposes an action, a human approves or rejects it, and the workflow resumes with the decision. When the human responds, the task picks up exactly where it left off.


The task pauses on a [durable event](/v1/events), freeing the worker slot until the approval arrives. If your workflow is a fixed DAG and the approval gate is known at definition time, [Event Conditions](/v1/events) are a simpler alternative. It is your responsibility to emit the event from a different part of your application to restore the task.

## Step-by-step walkthrough

You'll build a durable task that proposes an action, waits for a human to push an approval event, and resumes with the decision.


### Write a wait-for-approval helper

Define a helper that calls `WaitForEvent` to pause execution until a human responds. The [CEL expression](/v1/events#event-filters) filters on the workflow run ID so the event only matches the specific task that is waiting. Hatchet frees the worker slot while the task is suspended and resumes it when the matching event arrives.

#### Python

```python
async def wait_for_approval(ctx: DurableContext) -> dict:
    run_id = ctx.workflow_run_id
    approval = await ctx.aio_wait_for(
        "approval",
        UserEventCondition(
            event_key=APPROVAL_EVENT_KEY,
            expression=f"input.runId == '{run_id}'",
        ),
    )
    return approval
```

#### Typescript

```typescript
function waitForApproval(ctx: DurableContext<unknown>) {
  const runId = ctx.workflowRunId();
  return ctx.waitFor({
    eventKey: APPROVAL_EVENT_KEY,
    expression: `input.runId == '${runId}'`,
  });
}
```

#### Go

```go
waitForApproval := func(ctx hatchet.DurableContext) (map[string]interface{}, error) {
	runID := ctx.WorkflowRunId()
	expression := fmt.Sprintf("input.runId == '%s'", runID)
	event, err := ctx.WaitForEvent("approval:decision", expression)
	if err != nil {
		return nil, err
	}
	var eventData map[string]interface{}
	if err := hatchet.EventInto(event, &eventData); err != nil {
		return nil, err
	}
	return eventData, nil
}
```

#### Ruby

```ruby
def wait_for_approval(ctx)
  run_id = ctx.workflow_run_id
  ctx.wait_for(
    'approval',
    Hatchet::UserEventCondition.new(
      event_key: APPROVAL_EVENT_KEY,
      expression: "input.runId == '#{run_id}'"
    )
  )
end
```

### Define the approval task

Create a durable task that proposes an action, calls the helper from Step 1, and branches on the result.

#### Python

```python
@hatchet.durable_task(name="ApprovalTask")
async def approval_task(input: EmptyModel, ctx: DurableContext) -> dict:
    proposed_action = {"action": "send_email", "to": "user@example.com"}
    approval = await wait_for_approval(ctx)
    if approval.get("approved"):
        return {"status": "approved", "action": proposed_action}
    return {"status": "rejected", "reason": approval.get("reason", "")}
```

#### Typescript

```typescript
export const approvalTask = hatchet.durableTask({
  name: 'approval-task',
  executionTimeout: '30m',
  fn: async (_, ctx) => {
    const proposedAction = { action: 'send_email', to: 'user@example.com' };
    const approval = waitForApproval(ctx);
    if (approval?.approved) {
      return { status: 'approved', action: proposedAction };
    }
    return { status: 'rejected', reason: approval?.reason ?? '' };
  },
});
```

#### Go

```go
task := client.NewStandaloneDurableTask("approval-task", func(ctx hatchet.DurableContext, input ApprovalInput) (ApprovalOutput, error) {
	proposedAction := map[string]string{"action": "send_email", "to": "user@example.com"}
	approval, err := waitForApproval(ctx)
	if err != nil {
		return ApprovalOutput{}, err
	}
	approved, _ := approval["approved"].(bool)
	if approved {
		return ApprovalOutput{Status: "approved", Action: proposedAction}, nil
	}
	reason, _ := approval["reason"].(string)
	return ApprovalOutput{Status: "rejected", Reason: reason}, nil
})
```

#### Ruby

```ruby
APPROVAL_TASK = HATCHET.durable_task(name: 'ApprovalTask') do |_input, ctx|
  proposed_action = { 'action' => 'send_email', 'to' => 'user@example.com' }
  approval = wait_for_approval(ctx)
  if approval['approved']
    { 'status' => 'approved', 'action' => proposed_action }
  else
    { 'status' => 'rejected', 'reason' => approval['reason'].to_s }
  end
end
```

### Push the approval event

When the human clicks Approve or Reject in your UI, your frontend or API pushes the event to Hatchet. Include the `runId` in the payload so the CEL expression in Step 1 matches it to the correct waiting task.

#### Python

```python
# Include the run_id so the event matches the specific task waiting for it.
def push_approval(run_id: str, approved: bool, reason: str = "") -> None:
    hatchet.event.push(
        "approval:decision",
        {"runId": run_id, "approved": approved, "reason": reason},
    )


# Approve: push_approval("run-id-from-ui", True)
# Reject:  push_approval("run-id-from-ui", False, reason="needs review")
```

#### Typescript

```typescript
// Include the runId so the event matches the specific task waiting for it.
export async function pushApproval(runId: string, approved: boolean, reason = '') {
  await hatchet.event.push('approval:decision', { runId, approved, reason });
}

// Approve: await pushApproval('run-id-from-ui', true);
// Reject:  await pushApproval('run-id-from-ui', false, 'needs review');
```

#### Go

```go
// Include the runID so the event matches the specific task waiting for it.
func pushApproval(client *hatchet.Client, runID string, approved bool, reason string) {
	_ = client.Events().Push(context.Background(), "approval:decision", map[string]interface{}{
		"runId":    runID,
		"approved": approved,
		"reason":   reason,
	})
}
```

#### Ruby

```ruby
# Include the run_id so the event matches the specific task waiting for it.
def push_approval(run_id:, approved:, reason: '')
  HATCHET.events.create(
    key: 'approval:decision',
    data: { 'runId' => run_id, 'approved' => approved, 'reason' => reason }
  )
end

# Approve: push_approval(run_id: 'run-id-from-ui', approved: true)
# Reject:  push_approval(run_id: 'run-id-from-ui', approved: false, reason: "needs review")
```

### Run the worker

Register and start the worker. Use [Branching](/v1/conditions) to route on approve vs reject from the event payload.

#### Python

```python
worker = hatchet.worker(
    "human-in-the-loop-worker",
    workflows=[approval_task],
)
worker.start()
```

#### Typescript

```typescript
const worker = await hatchet.worker('human-in-the-loop-worker', {
  workflows: [approvalTask],
});
await worker.start();
```

#### Go

```go
worker, err := client.NewWorker("human-in-the-loop-worker",
	hatchet.WithWorkflows(task),
	hatchet.WithDurableSlots(5),
)
if err != nil {
	log.Fatalf("failed to create worker: %v", err)
}

interruptCtx, cancel := cmdutils.NewInterruptContext()
defer cancel()

go func() {
	if err := worker.StartBlocking(interruptCtx); err != nil {
		log.Fatalf("failed to start worker: %v", err)
	}
}()
```

#### Ruby

```ruby
worker = HATCHET.worker(
  'human-in-the-loop-worker',
  workflows: [APPROVAL_TASK]
)
worker.start
```


> **Warning:** Always set an **execution timeout** on the durable task itself so it does not
>   wait indefinitely if a human never responds. See [Timeouts](/v1/timeouts) for
>   configuration.

## Common Patterns

| Pattern                         | Description                                                             |
| ------------------------------- | ----------------------------------------------------------------------- |
| **Content moderation**          | Agent flags content; human approves or rejects before publish           |
| **Financial approvals**         | Agent proposes payment or transfer; human approves via dashboard        |
| **Customer support escalation** | Agent drafts response; human reviews and sends, or edits before sending |
| **LLM output review**           | Agent generates copy or code; human approves before it goes live        |

For DAG workflows with a fixed approval gate, use [Event Conditions](/v1/events). For agent loops where the decision to wait is dynamic, use a durable task with `WaitForEvent`.

## Related Patterns


  
    Pause workflows for external signals (events or sleep) without holding
    slots.
  
  
    Agent workflows that may need human approval at decision points.
  
  
    Route workflow behavior based on approve vs reject from the event payload.
  
  
    Declare approval gates in DAG workflows when the wait is known at definition
    time.
  


## Next Steps

- [Durable Events](/v1/events): `WaitForEvent` API and event filters
- [Pushing Events](/v1/external-events/pushing-events): push approval events from your frontend or API
- [Event Conditions](/v1/events): approval gates in DAG workflows
- [Long Waits](/v1/sleep): general pattern for durable pauses
- [Branching](/v1/conditions): route on approve vs reject


---

<!-- Source: https://docs.hatchet.run/cookbooks/rag-and-indexing -->

# RAG & Data Indexing

RAG and indexing pipelines share a common shape: ingest documents, split them into chunks, generate embeddings, and write to a vector database. Because the stages are known upfront, these pipelines map naturally to a [DAG workflow](/v1/patterns/directed-acyclic-graphs), where each stage is a task and dependencies between stages are declared before execution begins.


You declare the full graph (ingest → chunk → embed → index) and Hatchet executes tasks in order, running independent tasks in parallel automatically. You can add [fanout](/v1/child-spawning) within the chunking stage to process documents in parallel.

## Step-by-step walkthrough

You'll define a workflow, then add tasks for ingesting, chunking, embedding, and querying, all using a mock embedding client so you can run it without API keys.


### Define the workflow

Define your input type and create an empty [DAG workflow](/v1/patterns/directed-acyclic-graphs). You'll add tasks to this workflow in the following steps.

#### Python

```python
class DocInput(BaseModel):
    doc_id: str
    content: str


rag_wf = hatchet.workflow(name="RAGPipeline", input_validator=DocInput)
```

#### Typescript

```typescript
type DocInput = { doc_id: string; content: string };

const ragWf = hatchet.workflow({ name: 'RAGPipeline' });
```

#### Go

```go
workflow := client.NewWorkflow("RAGPipeline")
```

#### Ruby

```ruby
RAG_WF = HATCHET.workflow(name: 'RAGPipeline')
```

### Define the ingest task

Add a task that ingests documents. A trigger (event, cron, or API call) starts the pipeline with document references.

#### Python

```python
@rag_wf.task()
async def ingest(input: DocInput, ctx: Context) -> dict[str, Any]:
    return {"doc_id": input.doc_id, "content": input.content}
```

#### Typescript

```typescript
const ingest = ragWf.task({
  name: 'ingest',
  fn: async (input) => ({ doc_id: input.doc_id, content: input.content }),
});
```

#### Go

```go
ingest := workflow.NewTask("ingest", func(ctx hatchet.Context, input DocInput) (map[string]interface{}, error) {
	return map[string]interface{}{"doc_id": input.DocID, "content": input.Content}, nil
})
```

#### Ruby

```ruby
INGEST = RAG_WF.task(:ingest) do |input, _ctx|
  { 'doc_id' => input['doc_id'], 'content' => input['content'] }
end
```

### Chunk the documents

The ingest task (Step 2) fans out to one child per document. Each child splits its document into chunks. Use [child spawning](/v1/child-spawning) for per-document parallelism.

#### Python

```python
def _chunk_content(content: str, chunk_size: int = 100) -> list[str]:
    return [content[i : i + chunk_size] for i in range(0, len(content), chunk_size)]
```

#### Typescript

```typescript
function chunkContent(content: string, chunkSize = 100): string[] {
  const chunks: string[] = [];
  for (let i = 0; i < content.length; i += chunkSize) {
    chunks.push(content.slice(i, i + chunkSize));
  }
  return chunks;
}
```

#### Go

```go
chunkContent := func(content string, chunkSize int) []string {
	var chunks []string
	for i := 0; i < len(content); i += chunkSize {
		end := i + chunkSize
		if end > len(content) {
			end = len(content)
		}
		chunks = append(chunks, content[i:end])
	}
	return chunks
}
_ = chunkContent
```

#### Ruby

```ruby
def chunk_content(content, chunk_size = 100)
  content.scan(/.{1,#{chunk_size}}/)
end
```

### Embed and index

Define a standalone `embed-chunk` task, then spawn one [child task](/v1/child-spawning) per chunk from the DAG's `chunk-and-embed` task. Each child runs on any available worker and is individually retryable, so a single embedding failure does not restart the entire batch. [Rate Limits](/v1/rate-limits) throttle embedding API calls across all workers.

#### Python

```python
@hatchet.task(name="embed-chunk")
async def embed_chunk(input: dict, ctx: Context) -> dict[str, Any]:
    embedder = get_embedding_service()
    return {"vector": embedder.embed(input["chunk"])}


@rag_wf.durable_task(parents=[ingest])
async def chunk_and_embed(input: DocInput, ctx: Context) -> dict[str, Any]:
    ingested = ctx.task_output(ingest)
    chunks = [ingested["content"][i : i + 100] for i in range(0, len(ingested["content"]), 100)]
    results = await embed_chunk.aio_run_many(
        [embed_chunk.create_bulk_run_item(input={"chunk": c}) for c in chunks]
    )
    return {"doc_id": ingested["doc_id"], "vectors": [r["vector"] for r in results]}
```

#### Typescript

```typescript
const embedChunkTask = hatchet.task<{ chunk: string }>({
  name: 'embed-chunk',
  fn: async (input) => ({ vector: embed(input.chunk) }),
});

const chunkAndEmbed = ragWf.durableTask({
  name: 'chunk-and-embed',
  parents: [ingest],
  fn: async (input, ctx) => {
    const ingested = await ctx.parentOutput(ingest);
    const chunks: string[] = [];
    for (let i = 0; i < ingested.content.length; i += 100) {
      chunks.push(ingested.content.slice(i, i + 100));
    }
    const results = await Promise.all(chunks.map((chunk) => embedChunkTask.run({ chunk })));
    return { doc_id: ingested.doc_id, vectors: results.map((r) => r.vector) };
  },
});
```

#### Go

```go
embedChunkTask := client.NewStandaloneTask("embed-chunk", func(ctx hatchet.Context, input ChunkInput) (map[string]interface{}, error) {
	return map[string]interface{}{"vector": embed(input.Chunk)}, nil
})

chunkAndEmbed := workflow.NewDurableTask("chunk-and-embed", func(ctx hatchet.DurableContext, input DocInput) (map[string]interface{}, error) {
	var ingested map[string]interface{}
	if err := ctx.ParentOutput(ingest, &ingested); err != nil {
		return nil, err
	}
	content := ingested["content"].(string)
	var chunks []string
	for i := 0; i < len(content); i += 100 {
		end := i + 100
		if end > len(content) {
			end = len(content)
		}
		chunks = append(chunks, content[i:end])
	}
	inputs := make([]hatchet.RunManyOpt, len(chunks))
	for i, c := range chunks {
		inputs[i] = hatchet.RunManyOpt{Input: ChunkInput{Chunk: c}}
	}
	runRefs, err := embedChunkTask.RunMany(ctx, inputs)
	if err != nil {
		return nil, err
	}
	vectors := make([]interface{}, len(runRefs))
	for i, ref := range runRefs {
		result, err := ref.Result()
		if err != nil {
			return nil, err
		}
		var parsed map[string]interface{}
		if err := result.TaskOutput("embed-chunk").Into(&parsed); err != nil {
			return nil, err
		}
		vectors[i] = parsed["vector"]
	}
	return map[string]interface{}{"doc_id": ingested["doc_id"], "vectors": vectors}, nil
}, hatchet.WithParents(ingest))
```

#### Ruby

```ruby
EMBED_CHUNK_TASK = HATCHET.task(name: 'embed-chunk') do |input, _ctx|
  { 'vector' => embed(input['chunk']) }
end

RAG_WF.durable_task(:chunk_and_embed, parents: [INGEST]) do |_input, ctx|
  ingested = ctx.task_output(INGEST)
  content = ingested['content']
  chunks = content.scan(/.{1,100}/)
  results = EMBED_CHUNK_TASK.run_many(
    chunks.map { |c| EMBED_CHUNK_TASK.create_bulk_run_item(input: { 'chunk' => c }) }
  )
  { 'doc_id' => ingested['doc_id'], 'vectors' => results.map { |r| r['vector'] } }
end
```

The examples above use a mock embedding client. To use a real provider, swap `get_embedding_service()` with one of these. Pick a provider, then your language:

<!-- Could not resolve @/components/EmbeddingIntegrationTabs.mdx -->

### Query

Add a query task that reuses the same `embed-chunk` child task to embed the query, then performs a vector similarity search. In production, replace the empty results with a real vector DB lookup.

#### Python

```python
@hatchet.durable_task(name="rag-query")
async def query_task(input: dict, ctx: Context) -> dict[str, Any]:
    result = await embed_chunk.aio_run(input={"chunk": input["query"]})
    # Replace with a real vector DB lookup in production
    return {"query": input["query"], "vector": result["vector"], "results": []}
```

#### Typescript

```typescript
type QueryInput = { query: string; top_k?: number };

const queryTask = hatchet.durableTask({
  name: 'rag-query',
  fn: async (input) => {
    const { vector } = await embedChunkTask.run({ chunk: input.query });
    // Replace with a real vector DB lookup in production
    return { query: input.query, vector, results: [] };
  },
});
```

#### Go

```go
queryTask := client.NewStandaloneDurableTask("rag-query", func(ctx hatchet.DurableContext, input QueryInput) (map[string]interface{}, error) {
	res, err := embedChunkTask.Run(ctx, ChunkInput{Chunk: input.Query})
	if err != nil {
		return nil, err
	}
	var parsed map[string]interface{}
	if err := res.Into(&parsed); err != nil {
		return nil, err
	}
	// Replace with a real vector DB lookup in production
	return map[string]interface{}{"query": input.Query, "vector": parsed["vector"], "results": []interface{}{}}, nil
})
```

#### Ruby

```ruby
QUERY_TASK = HATCHET.durable_task(name: 'rag-query') do |input, _ctx|
  result = EMBED_CHUNK_TASK.run('chunk' => input['query'])
  # Replace with a real vector DB lookup in production
  { 'query' => input['query'], 'vector' => result['vector'], 'results' => [] }
end
```

### Run the worker

Start the worker and register the DAG workflow, the `embed-chunk` child task, and the `rag-query` task.

#### Python

```python
worker = hatchet.worker(
    "rag-worker",
    workflows=[rag_wf, embed_chunk, query_task],
)
worker.start()
```

#### Typescript

```typescript
const worker = await hatchet.worker('rag-worker', {
  workflows: [ragWf, embedChunkTask, queryTask],
});
await worker.start();
```

#### Go

```go
worker, err := client.NewWorker("rag-worker", hatchet.WithWorkflows(workflow, embedChunkTask, queryTask))
if err != nil {
	log.Fatalf("failed to create worker: %v", err)
}

interruptCtx, cancel := cmdutils.NewInterruptContext()
defer cancel()

if err := worker.StartBlocking(interruptCtx); err != nil {
	log.Fatalf("failed to start worker: %v", err)
}
```

#### Ruby

```ruby
worker = HATCHET.worker('rag-worker', workflows: [RAG_WF, EMBED_CHUNK_TASK, QUERY_TASK])
worker.start
```


> **Warning:** When fanning out to many chunks, ensure your workers have enough slots or use
>   [Concurrency Control](/v1/concurrency) to limit how many run simultaneously.

## Multi-Tenant Indexing

For SaaS applications where multiple tenants share the same pipeline:

- **GROUP_ROUND_ROBIN concurrency** distributes scheduling fairly so no single tenant monopolizes workers
- **Additional metadata** tags each run with a tenant ID for filtering in the dashboard
- **Priority queues** allow higher-priority indexing jobs to run ahead of lower-priority ones

## Related Patterns


  
    Declare tasks and dependencies upfront so Hatchet can execute them in order.
  
  
    Parallelize document and chunk processing across your worker fleet.
  
  
    Implement incremental indexing that re-crawls until all changes are
    processed.
  
  
    General-purpose batch processing patterns that apply to indexing workloads.
  
  
    Extract and transform documents (invoices, contracts, forms), distinct from
    RAG's chunk-and-embed for retrieval.
  


## Next Steps

- [DAG Workflows](/v1/patterns/directed-acyclic-graphs): define multi-stage pipelines
- [Rate Limits](/v1/rate-limits): configure rate limiting for embedding APIs
- [Child Spawning](/v1/child-spawning): fan out to per-document tasks
- [Concurrency Control](/v1/concurrency): fair scheduling for multi-tenant indexing


---

<!-- Source: https://docs.hatchet.run/cookbooks/llm-pipelines -->

# LLM Pipelines

LLM pipelines chain multiple model calls together with validation, retries, and structured outputs. Hatchet turns each step into a durable task so failures retry individually, rate limits protect provider APIs, and the full pipeline is observable in the dashboard.

Because each LLM call maps to a task and validation steps gate what runs next, these pipelines are a natural fit for [DAG Workflows](/v1/patterns/directed-acyclic-graphs).

## Step-by-step walkthrough

You'll build a three-stage DAG pipeline (prompt, generate, validate) using a mock LLM so you can run it without API keys.


### Define the pipeline

Create a workflow with prompt construction, LLM generation, and validation stages.

#### Python

```python
class PipelineInput(BaseModel):
    prompt: str


llm_wf = hatchet.workflow(name="LLMPipeline", input_validator=PipelineInput)


@llm_wf.task()
async def prompt_task(input: PipelineInput, ctx: Context) -> dict:
    return {"prompt": input.prompt}
```

#### Typescript

```typescript
const llmWf = hatchet.workflow({ name: 'LLMPipeline' });

const promptTask = llmWf.task({
  name: 'prompt-task',
  fn: async (input) => ({ prompt: input.prompt }),
});
```

#### Go

```go
workflow := client.NewWorkflow("LLMPipeline")
```

#### Ruby

```ruby
LLM_WF = HATCHET.workflow(name: 'LLMPipeline')

PROMPT_TASK = LLM_WF.task(:prompt_task) do |input, _ctx|
  { 'prompt' => input['prompt'] }
end
```

### Prompt task

The prompt task depends on the pipeline input (Step 1). Build the prompt from user input and context. This step may include retrieval from a vector database (see [RAG & Indexing](/guides/rag-and-indexing)).

#### Python

```python
def _build_prompt(user_input: str, context: str = "") -> str:
    return f"Process the following: {user_input}" + (f"\nContext: {context}" if context else "")
```

#### Typescript

```typescript
function buildPrompt(userInput: string, context = ''): string {
  return `Process the following: ${userInput}${context ? `\nContext: ${context}` : ''}`;
}
```

#### Go

```go
buildPrompt := func(userInput, context string) string {
	if context != "" {
		return "Process the following: " + userInput + "\nContext: " + context
	}
	return "Process the following: " + userInput
}
_ = buildPrompt
```

#### Ruby

```ruby
def build_prompt(user_input, context = '')
  base = "Process the following: #{user_input}"
  context.empty? ? base : "#{base}\nContext: #{context}"
end
```

The prompt is passed to your LLM service for generation. The examples above use a mock. To use a real provider, swap `get_llm_service()` with one of these:

<!-- Could not resolve @/components/LLMIntegrationTabs.mdx -->

### Generate and validate

This task takes the prompt from Step 2, calls the LLM, and validates the response. If validation fails, [Retry Policies](/v1/retry-policies) retry just this step with a corrective prompt.

#### Python

```python
@llm_wf.task(parents=[prompt_task])
async def generate_task(input: PipelineInput, ctx: Context) -> dict:
    prev = ctx.task_output(prompt_task)
    output = get_llm_service().generate(prev["prompt"])
    if not output.get("valid"):
        raise ValueError("Validation failed")
    return output
```

#### Typescript

```typescript
const generateTask = llmWf.task({
  name: 'generate-task',
  parents: [promptTask],
  fn: async (input, ctx) => {
    const prev = await ctx.parentOutput(promptTask);
    const output = generate(prev.prompt);
    if (!output.valid) throw new Error('Validation failed');
    return output;
  },
});
```

#### Go

```go
generateTask := workflow.NewTask("generate-task", func(ctx hatchet.Context, input PipelineInput) (map[string]interface{}, error) {
	var prev map[string]interface{}
	if err := ctx.ParentOutput(promptTask, &prev); err != nil {
		return nil, err
	}
	output := generate(prev["prompt"].(string))
	if !output["valid"].(bool) {
		panic("validation failed")
	}
	return output, nil
}, hatchet.WithParents(promptTask))
```

#### Ruby

```ruby
LLM_WF.task(:generate_task, parents: [PROMPT_TASK]) do |_input, ctx|
  prev = ctx.task_output(PROMPT_TASK)
  output = generate(prev['prompt'])
  raise 'Validation failed' unless output['valid']

  output
end
```

### Run the worker

Start the worker. Configure [Rate Limits](/v1/rate-limits) to stay within LLM provider quotas.

#### Python

```python
worker = hatchet.worker(
    "llm-pipeline-worker",
    workflows=[llm_wf],
)
worker.start()
```

#### Typescript

```typescript
const worker = await hatchet.worker('llm-pipeline-worker', {
  workflows: [llmWf],
});
await worker.start();
```

#### Go

```go
worker, err := client.NewWorker("llm-pipeline-worker", hatchet.WithWorkflows(workflow))
if err != nil {
	log.Fatalf("failed to create worker: %v", err)
}

interruptCtx, cancel := cmdutils.NewInterruptContext()
defer cancel()

if err := worker.StartBlocking(interruptCtx); err != nil {
	log.Fatalf("failed to start worker: %v", err)
}
```

#### Ruby

```ruby
worker = HATCHET.worker('llm-pipeline-worker', workflows: [LLM_WF])
worker.start
```


> **Warning:** Always set **timeouts** on LLM call steps. Model providers can hang or respond
>   slowly under load. See [Timeouts](/v1/timeouts) for configuration.

## Common Patterns

| Pattern                  | Description                                                               |
| ------------------------ | ------------------------------------------------------------------------- |
| **Generate → Validate**  | Call LLM, validate structured output, retry with error context on failure |
| **Chain of thought**     | Multi-step reasoning where each LLM call refines the previous output      |
| **Parallel evaluation**  | Fan out the same prompt to multiple models, then pick the best response   |
| **Translation pipeline** | Generate content in one language, translate to others in parallel         |
| **Summarize → Classify** | Summarize long text, then classify the summary for routing or tagging     |

## Related Patterns


  
    When LLM calls happen in a dynamic loop rather than a fixed pipeline.
  
  
    Provide context to LLM pipeline steps via retrieval-augmented generation.
  
  
    Extract structured data from documents using LLM-powered pipelines.
  
  
    Run LLM pipelines across many inputs with fan-out and concurrency control.
  


## Next Steps

- [DAG Workflows](/v1/patterns/directed-acyclic-graphs): define multi-stage LLM pipelines
- [Rate Limits](/v1/rate-limits): configure rate limiting for LLM providers
- [Retry Policies](/v1/retry-policies): handle transient LLM API errors
- [Streaming](/v1/streaming): stream LLM outputs to frontends in real-time


---

<!-- Source: https://docs.hatchet.run/cookbooks/batch-processing -->

# Batch Processing

Batch processing involves running the same operation across a large set of items like images, documents, records, or API calls. We'll structure batch workloads in Hatchet with fan-out, retry, and concurrency control.


At its core, batch processing is [Fanout](/v1/child-spawning) applied at scale. If your batch also has fixed stages (e.g., validate → transform → load), you can combine it with [Pre-Determined Pipelines](/v1/patterns/directed-acyclic-graphs).

## Step-by-step walkthrough

You'll build a parent workflow that fans out to one child task per item and aggregates results.


### Define the parent workflow

Create a parent workflow that receives a batch of item IDs and spawns one child per item.

#### Python

```python
class BatchInput(BaseModel):
    items: list[str]


class ItemInput(BaseModel):
    item_id: str


parent_wf = hatchet.workflow(name="BatchParent", input_validator=BatchInput)
child_wf = hatchet.workflow(name="BatchChild", input_validator=ItemInput)


@parent_wf.durable_task()
async def spawn_children(input: BatchInput, ctx: Context) -> dict[str, Any]:
    """Parent fans out to one child per item."""
    results = await child_wf.aio_run_many(
        [child_wf.create_bulk_run_item(input=ItemInput(item_id=item_id)) for item_id in input.items]
    )
    return {"processed": len(results), "results": results}
```

#### Typescript

```typescript
const parentTask = hatchet.durableTask({
  name: 'spawn-children',
  fn: async (input) => {
    const results = await Promise.all(
      input.items.map((itemId) => childTask.run({ item_id: itemId }))
    );
    return { processed: results.length, results };
  },
});
```

#### Go

```go
parentTask := client.NewStandaloneDurableTask("spawn-children", func(ctx hatchet.DurableContext, input BatchInput) (map[string]interface{}, error) {
	inputs := make([]hatchet.RunManyOpt, len(input.Items))
	for i, itemID := range input.Items {
		inputs[i] = hatchet.RunManyOpt{Input: ItemInput{ItemID: itemID}}
	}
	runRefs, err := childTask.RunMany(ctx, inputs)
	if err != nil {
		return nil, err
	}
	results := make([]interface{}, len(runRefs))
	for i, ref := range runRefs {
		result, err := ref.Result()
		if err != nil {
			return nil, err
		}
		var parsed map[string]interface{}
		if err := result.TaskOutput("process-item").Into(&parsed); err != nil {
			return nil, err
		}
		results[i] = parsed
	}
	return map[string]interface{}{"processed": len(results), "results": results}, nil
})
```

#### Ruby

```ruby
BATCH_PARENT_WF = HATCHET.workflow(name: 'BatchParent')
BATCH_CHILD_WF = HATCHET.workflow(name: 'BatchChild')

BATCH_PARENT_WF.durable_task(:spawn_children) do |input, _ctx|
  items = input['items'] || []
  results = BATCH_CHILD_WF.run_many(
    items.map { |item_id| BATCH_CHILD_WF.create_bulk_run_item(input: { 'item_id' => item_id }) }
  )
  { 'processed' => results.size, 'results' => results }
end
```

### Process each item

Each child task processes a single item independently. Failed items are retried according to your retry policy.

#### Python

```python
@child_wf.task()
async def process_item(input: ItemInput, ctx: Context) -> dict[str, str]:
    """Child processes a single item."""
    return {"status": "done", "item_id": input.item_id}
```

#### Typescript

```typescript
function processItem(input: ItemInput) {
  return { status: 'done', item_id: input.item_id };
}
```

#### Go

```go
childTask := client.NewStandaloneTask("process-item", func(ctx hatchet.Context, input ItemInput) (map[string]string, error) {
	return map[string]string{"status": "done", "item_id": input.ItemID}, nil
})
```

#### Ruby

```ruby
BATCH_CHILD_WF.task(:process_item) do |input, _ctx|
  { 'status' => 'done', 'item_id' => input['item_id'] }
end
```

### Run the worker

Register and start the worker with both parent and child workflows. For large batches, use [durable workflows](/v1/patterns/durable-task-execution) so the parent does not hold a slot while waiting.

#### Python

```python
worker = hatchet.worker(
    "batch-worker",
    slots=20,
    workflows=[parent_wf, child_wf],
)
worker.start()
```

#### Typescript

```typescript
const worker = await hatchet.worker('batch-worker', {
  workflows: [parentTask, childTask],
  slots: 20,
});
await worker.start();
```

#### Go

```go
worker, err := client.NewWorker("batch-worker", hatchet.WithWorkflows(parentTask, childTask), hatchet.WithSlots(20))
if err != nil {
	log.Fatalf("failed to create worker: %v", err)
}

interruptCtx, cancel := cmdutils.NewInterruptContext()
defer cancel()

if err := worker.StartBlocking(interruptCtx); err != nil {
	cancel()
	log.Fatalf("failed to start worker: %v", err)
}
```

#### Ruby

```ruby
worker = HATCHET.worker('batch-worker', slots: 20, workflows: [BATCH_PARENT_WF, BATCH_CHILD_WF])
worker.start
```


> **Warning:** For batches with thousands of items, use **durable workflows** so the parent
>   task doesn't hold a worker slot while waiting for all children to complete.
>   See [Durable Workflows](/v1/patterns/durable-task-execution) for details.

## Common Patterns

| Pattern                   | Description                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------- |
| **Image processing**      | Resize, transcode, or analyze images in parallel across workers                     |
| **Data enrichment**       | Enrich records by calling external APIs (geocoding, company info, email validation) |
| **Report generation**     | Generate per-customer reports in parallel, then aggregate into a summary            |
| **Database migrations**   | Process and migrate records in batches with retry and progress tracking             |
| **Notification delivery** | Send emails, SMS, or push notifications to a user list with rate limiting           |

## Related Patterns


  
    The core pattern behind batch processing, spawning N children from a parent.
  
  
    Chain batch processing with multi-stage transforms in a DAG.
  
  
    A specialized batch processing use case for document indexing pipelines.
  
  
    Process paginated results one page at a time with iterative child spawning.
  


## Next Steps

- [Child Spawning](/v1/child-spawning): learn the fan-out API for batch processing
- [Bulk Run](/v1/bulk-run): trigger large batches efficiently
- [Concurrency Control](/v1/concurrency): limit concurrent item processing
- [Rate Limits](/v1/rate-limits): protect external APIs during batch operations


---

<!-- Source: https://docs.hatchet.run/cookbooks/document-processing -->

# Document Processing

PDF and file pipelines are central to AI workflows: parse documents, extract content with OCR or LLMs, validate and enrich the data, and classify or route it. We'll structure these as Hatchet [DAG workflows](/v1/patterns/directed-acyclic-graphs).


Because the stages are fixed (ingest → parse → extract), document pipelines map naturally to [DAG workflows](/v1/patterns/directed-acyclic-graphs). You can add [child spawning](/v1/child-spawning) within the ingest or parse stage to process multiple documents in parallel.

## Step-by-step walkthrough

You'll build a three-stage pipeline (ingest, parse, extract) using mocks so you can run it locally without API keys.


### Define the DAG

Create a workflow with a fixed pipeline: ingest, parse, extract. Each stage depends on the previous.

#### Python

```python
class DocInput(BaseModel):
    doc_id: str
    content: bytes = b""


doc_wf = hatchet.workflow(name="DocumentPipeline", input_validator=DocInput)


@doc_wf.task()
async def ingest(input: DocInput, ctx: Context) -> dict[str, Any]:
    return {"doc_id": input.doc_id, "content": input.content}
```

#### Typescript

```typescript
const docWf = hatchet.workflow({ name: 'DocumentPipeline' });

const ingest = docWf.task({
  name: 'ingest',
  fn: async (input) => ({ doc_id: input.doc_id, content: input.content }),
});
```

#### Go

```go
workflow := client.NewWorkflow("DocumentPipeline")
```

#### Ruby

```ruby
DOC_WF = HATCHET.workflow(name: 'DocumentPipeline')

INGEST = DOC_WF.task(:ingest) do |input, _ctx|
  { 'doc_id' => input['doc_id'], 'content' => input['content'] }
end
```

### Parse stage

The parse task depends on ingest (Step 1). It converts raw content to structured text (use OCR for images, mock for examples).

#### Python

```python
@doc_wf.task(parents=[ingest])
async def parse(input: DocInput, ctx: Context) -> dict[str, Any]:
    ingested = ctx.task_output(ingest)
    text = get_ocr_service().parse(ingested["content"])
    return {"doc_id": input.doc_id, "text": text}
```

#### Typescript

```typescript
const parse = docWf.task({
  name: 'parse',
  parents: [ingest],
  fn: async (input, ctx) => {
    const ingested = await ctx.parentOutput(ingest);
    const text = parseDocument(ingested.content);
    return { doc_id: input.doc_id, text };
  },
});
```

#### Go

```go
ingest := workflow.NewTask("ingest", func(ctx hatchet.Context, input DocInput) (map[string]interface{}, error) {
	return map[string]interface{}{"doc_id": input.DocID, "content": input.Content}, nil
})

parse := workflow.NewTask("parse", func(ctx hatchet.Context, input DocInput) (map[string]interface{}, error) {
	var ingested map[string]interface{}
	if err := ctx.ParentOutput(ingest, &ingested); err != nil {
		return nil, err
	}
	content := ingested["content"].([]byte)
	text := parseDocument(content)
	return map[string]interface{}{"doc_id": input.DocID, "text": text}, nil
}, hatchet.WithParents(ingest))
```

#### Ruby

```ruby
PARSE = DOC_WF.task(:parse, parents: [INGEST]) do |input, ctx|
  ingested = ctx.task_output(INGEST)
  text = parse_document(ingested['content'])
  { 'doc_id' => input['doc_id'], 'text' => text }
end
```

The examples above use a mock OCR service. To use a real provider, swap in one of these. Pick a provider, then your language:

<!-- Could not resolve @/components/OCRIntegrationTabs.mdx -->

### Extract stage

The extract task depends on parse (Step 2). Use an LLM or rules to extract entities. [Rate Limits](/v1/rate-limits) keep extract tasks within provider quotas.

#### Python

```python
@doc_wf.task(parents=[parse])
async def extract(input: DocInput, ctx: Context) -> dict[str, Any]:
    parsed = ctx.task_output(parse)
    entities = get_extract_service().extract(parsed["text"])
    return {"doc_id": parsed["doc_id"], "entities": entities}
```

#### Typescript

```typescript
const extract = docWf.task({
  name: 'extract',
  parents: [parse],
  fn: async (input, ctx) => {
    const parsed = await ctx.parentOutput(parse);
    return { doc_id: parsed.doc_id, entities: ['entity1', 'entity2'] };
  },
});
```

#### Go

```go
extract := workflow.NewTask("extract", func(ctx hatchet.Context, input DocInput) (map[string]interface{}, error) {
	var parsed map[string]interface{}
	if err := ctx.ParentOutput(parse, &parsed); err != nil {
		return nil, err
	}
	return map[string]interface{}{"doc_id": parsed["doc_id"], "entities": []string{"entity1", "entity2"}}, nil
}, hatchet.WithParents(parse))
```

#### Ruby

```ruby
DOC_WF.task(:extract, parents: [PARSE]) do |_input, ctx|
  parsed = ctx.task_output(PARSE)
  { 'doc_id' => parsed['doc_id'], 'entities' => %w[entity1 entity2] }
end
```

The examples above use a mock extractor. To wire in a real LLM for extraction, swap `get_extract_service()` with a provider:

<!-- Could not resolve @/components/LLMIntegrationTabs.mdx -->

### Run the worker

Start the worker. For per-document parallelism, use [Child Spawning](/v1/child-spawning) within the ingest stage.

#### Python

```python
worker = hatchet.worker(
    "document-worker",
    workflows=[doc_wf],
)
worker.start()
```

#### Typescript

```typescript
const worker = await hatchet.worker('document-worker', {
  workflows: [docWf],
});
await worker.start();
```

#### Go

```go
worker, err := client.NewWorker("document-worker", hatchet.WithWorkflows(workflow))
if err != nil {
	log.Fatalf("failed to create worker: %v", err)
}

interruptCtx, cancel := cmdutils.NewInterruptContext()
defer cancel()

if err := worker.StartBlocking(interruptCtx); err != nil {
	cancel()
	log.Fatalf("failed to start worker: %v", err)
}
```

#### Ruby

```ruby
worker = HATCHET.worker('document-worker', workflows: [DOC_WF])
worker.start
```


> **Warning:** When fanning out to many documents, ensure your workers have enough slots or
>   use [Concurrency Control](/v1/concurrency) to limit how many run
>   simultaneously.

## Common Patterns

| Pattern                     | Description                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Invoice extraction**      | Parse invoices, extract line items and totals with LLM, validate amounts, post to ERP                  |
| **Contract analysis**       | Extract clauses and terms, classify risk, route for legal review                                       |
| **Resume parsing**          | Parse resumes, extract skills and experience, match to job requisitions                                |
| **Form processing**         | Extract form fields from scans, validate against schemas, submit to backend systems                    |
| **Document classification** | Classify documents by type, route to appropriate [DAG workflows](/v1/patterns/directed-acyclic-graphs) |

## Related Patterns


  
    The fixed-stage DAG pattern that document pipelines are built on.
  
  
    When your goal is retrieval (chunk, embed, index) rather than extract and
    transform.
  
  
    General-purpose batch patterns that apply to document workloads.
  
  
    Parallelize document processing across your worker fleet.
  


## Next Steps

- [DAG Workflows](/v1/patterns/directed-acyclic-graphs): define multi-stage pipelines with task dependencies
- [Rate Limits](/v1/rate-limits): configure rate limiting for OCR and LLM APIs
- [Child Spawning](/v1/child-spawning): fan out to per-document tasks
- [Webhooks](/v1/webhooks): trigger pipelines from file upload endpoints
- [Concurrency Control](/v1/concurrency): limit parallel document processing


---

<!-- Source: https://docs.hatchet.run/cookbooks/web-scraping -->

# Web Scraping

Web scraping workflows fetch content from external websites, process it, and store the results. Scraping is inherently unreliable: pages change layout, rate limits kick in, requests time out. Scrape tasks need retries, timeouts, and concurrency control. Hatchet provides all three, plus cron scheduling to refresh scraped data on a recurring cadence.

A typical web scraping pipeline has three parts:

1. **Scrape**: fetch the page content (HTML, rendered JS, or structured API response)
2. **Process**: extract, transform, or summarize the content (optionally with an LLM)
3. **Schedule**: run the pipeline periodically via a cron workflow

```mermaid
flowchart LR
    C[Cron Trigger] --> S[Scrape Task]
    S --> P[Process Task]
    P --> D[(Store Results)]
```

## Step-by-step walkthrough

You'll build a scrape task with retries, a processing step, a cron workflow that refreshes your scraped data every 6 hours, and a rate-limited variant to avoid getting blocked.


### Define the scrape task

Create a task that fetches a URL and returns the content. Set a timeout (pages can hang) and retries (transient failures are common). The examples below use a mock. Swap it for Firecrawl, Playwright, or any HTTP client.

#### Python

```python
@scrape_wf.task(execution_timeout="2m", retries=2)
async def scrape_url(input: dict, ctx: Context) -> dict:
    return mock_scrape(input["url"])
```

#### Typescript

```typescript
const scrapeTask = hatchet.task({
  name: 'scrape-url',
  executionTimeout: '2m',
  retries: 2,
  fn: async (input: ScrapeInput) => {
    return mockScrape(input.url);
  },
});
```

#### Go

```go
scrapeTask := client.NewStandaloneTask("scrape-url", func(ctx hatchet.Context, input ScrapeInput) (map[string]interface{}, error) {
	result := MockScrape(input.URL)
	return map[string]interface{}{
		"url": result.URL, "title": result.Title,
		"content": result.Content, "scraped_at": result.ScrapedAt,
	}, nil
}, hatchet.WithRetries(2))
```

#### Ruby

```ruby
SCRAPE_WF.task(:scrape_url, execution_timeout: '2m', retries: 2) do |input, _ctx|
  mock_scrape(input['url'])
end
```

The examples above use a mock scraper. To use a real scraping provider, swap the mock with one of these. Pick a provider, then your language:

<!-- Could not resolve @/components/ScraperIntegrationTabs.mdx -->

### Process the scraped content

A separate task extracts or transforms the raw scraped content. This could be simple parsing, or an LLM call to summarize or extract structured data. Keeping it separate lets you retry processing independently from scraping.

#### Python

```python
@process_wf.task()
async def process_content(input: dict, ctx: Context) -> dict:
    content = input["content"]
    links = re.findall(r"https?://[^\s<>\"']+", content)
    summary = content[:200].strip()
    word_count = len(content.split())
    return {"summary": summary, "word_count": word_count, "links": links}
```

#### Typescript

```typescript
const processTask = hatchet.task({
  name: 'process-content',
  fn: async (input: { url: string; content: string }) => {
    const links = [...input.content.matchAll(/https?:\/\/[^\s<>"']+/g)].map((m) => m[0]);
    const summary = input.content.slice(0, 200).trim();
    const wordCount = input.content.split(/\s+/).filter(Boolean).length;
    return { summary, wordCount, links };
  },
});
```

#### Go

```go
linkRe := regexp.MustCompile(`https?://[^\s<>"']+`)
processTask := client.NewStandaloneTask("process-content", func(ctx hatchet.Context, input ProcessInput) (map[string]interface{}, error) {
	links := linkRe.FindAllString(input.Content, -1)
	summary := input.Content
	if len(summary) > 200 {
		summary = summary[:200]
	}
	wordCount := len(strings.Fields(input.Content))
	return map[string]interface{}{
		"summary": strings.TrimSpace(summary), "word_count": wordCount, "links": links,
	}, nil
})
```

#### Ruby

```ruby
PROCESS_WF.task(:process_content) do |input, _ctx|
  content = input['content']
  links = content.scan(%r{https?://[^\s<>"']+})
  summary = content[0, 200].strip
  word_count = content.split.size
  { 'summary' => summary, 'word_count' => word_count, 'links' => links }
end
```

### Schedule recurring scrapes

Wrap the pipeline in a cron workflow to refresh data on a schedule. The example below runs every 6 hours and scrapes a list of URLs. Each scrape + process pair runs as child tasks, so failures on one URL don't block the others.

#### Python

```python
cron_wf = hatchet.workflow(name="WebScrapeWorkflow", on_crons=["0 */6 * * *"])


@cron_wf.task()
async def scheduled_scrape(input: EmptyModel, ctx: Context) -> dict:
    urls = [
        "https://example.com/pricing",
        "https://example.com/blog",
        "https://example.com/docs",
    ]

    results = []
    for url in urls:
        scraped = await scrape_wf.aio_run(input={"url": url})
        processed = await process_wf.aio_run(input={"url": url, "content": scraped["content"]})
        results.append({"url": url, **processed})
    return {"refreshed": len(results), "results": results}
```

#### Typescript

```typescript
const scrapeWorkflow = hatchet.workflow({
  name: 'WebScrapeWorkflow',
  on: { cron: '0 */6 * * *' },
});

scrapeWorkflow.task({
  name: 'scheduled-scrape',
  fn: async () => {
    const urls = [
      'https://example.com/pricing',
      'https://example.com/blog',
      'https://example.com/docs',
    ];

    const results = [];
    for (const url of urls) {
      const scraped = await scrapeTask.run({ url });
      const processed = await processTask.run({ url, content: scraped.content });
      results.push({ url, ...processed });
    }
    return { refreshed: results.length, results };
  },
});
```

#### Go

```go
cronWf := client.NewWorkflow("WebScrapeWorkflow", hatchet.WithWorkflowCron("0 */6 * * *"))

cronWf.NewTask("scheduled-scrape", func(ctx hatchet.Context, input map[string]interface{}) (map[string]interface{}, error) {
	urls := []string{
		"https://example.com/pricing",
		"https://example.com/blog",
		"https://example.com/docs",
	}

	results := []map[string]string{}
	for _, url := range urls {
		scrapedResult, err := scrapeTask.Run(ctx, ScrapeInput{URL: url})
		if err != nil {
			return nil, err
		}
		var scraped map[string]interface{}
		if err := scrapedResult.Into(&scraped); err != nil {
			return nil, err
		}
		processedResult, err := processTask.Run(ctx, ProcessInput{URL: url, Content: scraped["content"].(string)})
		if err != nil {
			return nil, err
		}
		var processed map[string]string
		if err := processedResult.Into(&processed); err != nil {
			return nil, err
		}
		results = append(results, processed)
	}
	return map[string]interface{}{"refreshed": len(results), "results": results}, nil
})
```

#### Ruby

```ruby
CRON_WF = HATCHET.workflow(name: 'WebScrapeWorkflow', on_crons: ['0 */6 * * *'])

CRON_WF.task(:scheduled_scrape) do |_input, _ctx|
  urls = %w[
    https://example.com/pricing
    https://example.com/blog
    https://example.com/docs
  ]

  results = urls.map do |url|
    scraped = SCRAPE_WF.run('url' => url)
    processed = PROCESS_WF.run('url' => url, 'content' => scraped['content'])
    { 'url' => url }.merge(processed)
  end
  { 'refreshed' => results.size, 'results' => results }
end
```

### Add rate limiting

Target sites will block you if you send too many requests. Create a separate rate-limited scrape task that caps requests to a fixed number per minute across all workers. Hatchet holds back task executions that would exceed the limit, so you stay within budget without adding sleep logic in your code. See [Rate Limits](/v1/rate-limits) for details.

#### Python

```python
SCRAPE_RATE_LIMIT_KEY = "scrape-rate-limit"

rate_limited_wf = hatchet.workflow(name="RateLimitedScrape")


@rate_limited_wf.task(
    execution_timeout="2m",
    retries=2,
    rate_limits=[RateLimit(static_key=SCRAPE_RATE_LIMIT_KEY, units=1)],
)
async def rate_limited_scrape(input: dict, ctx: Context) -> dict:
    return mock_scrape(input["url"])
```

#### Typescript

```typescript
const SCRAPE_RATE_LIMIT_KEY = 'scrape-rate-limit';

const rateLimitedScrapeTask = hatchet.task({
  name: 'rate-limited-scrape',
  executionTimeout: '2m',
  retries: 2,
  rateLimits: [
    {
      staticKey: SCRAPE_RATE_LIMIT_KEY,
      units: 1,
    },
  ],
  fn: async (input: ScrapeInput) => {
    return mockScrape(input.url);
  },
});
```

#### Go

```go
units := 1
rateLimitedScrapeTask := client.NewStandaloneTask("rate-limited-scrape", func(ctx hatchet.Context, input ScrapeInput) (map[string]interface{}, error) {
	result := MockScrape(input.URL)
	return map[string]interface{}{
		"url": result.URL, "title": result.Title,
		"content": result.Content, "scraped_at": result.ScrapedAt,
	}, nil
}, hatchet.WithRetries(2), hatchet.WithRateLimits(&types.RateLimit{
	Key:   scrapeRateLimitKey,
	Units: &units,
}))
```

#### Ruby

```ruby
SCRAPE_RATE_LIMIT_KEY = 'scrape-rate-limit'

RATE_LIMITED_WF = HATCHET.workflow(name: 'RateLimitedScrape')

RATE_LIMITED_WF.task(
  :rate_limited_scrape,
  execution_timeout: '2m',
  retries: 2,
  rate_limits: [Hatchet::RateLimit.new(static_key: SCRAPE_RATE_LIMIT_KEY, units: 1)]
) do |input, _ctx|
  mock_scrape(input['url'])
end
```

### Run the worker

Register all tasks (including the rate-limited variant) and upsert the rate limit before starting the worker. The cron schedule activates when the worker connects.

#### Python

```python
hatchet.rate_limits.put(SCRAPE_RATE_LIMIT_KEY, 10, RateLimitDuration.MINUTE)

worker = hatchet.worker(
    "web-scraping-worker",
    workflows=[scrape_wf, process_wf, cron_wf, rate_limited_wf],
    slots=5,
)
worker.start()
```

#### Typescript

```typescript
await hatchet.ratelimits.upsert({
  key: SCRAPE_RATE_LIMIT_KEY,
  limit: 10,
  duration: RateLimitDuration.MINUTE,
});

const worker = await hatchet.worker('web-scraping-worker', {
  workflows: [scrapeTask, processTask, scrapeWorkflow, rateLimitedScrapeTask],
  slots: 5,
});
await worker.start();
```

#### Go

```go
err = client.RateLimits().Upsert(features.CreateRatelimitOpts{
	Key:      scrapeRateLimitKey,
	Limit:    10,
	Duration: types.Minute,
})
if err != nil {
	log.Fatalf("failed to upsert rate limit: %v", err)
}

worker, err := client.NewWorker("web-scraping-worker",
	hatchet.WithWorkflows(scrapeTask, processTask, cronWf, rateLimitedScrapeTask),
	hatchet.WithSlots(5),
)
if err != nil {
	log.Fatalf("failed to create worker: %v", err)
}

interruptCtx, cancel := cmdutils.NewInterruptContext()
defer cancel()

if err := worker.StartBlocking(interruptCtx); err != nil {
	log.Fatalf("failed to start worker: %v", err)
}
```

#### Ruby

```ruby
HATCHET.rate_limits.put(SCRAPE_RATE_LIMIT_KEY, 10, :minute)

worker = HATCHET.worker('web-scraping-worker',
                        slots: 5,
                        workflows: [SCRAPE_WF, PROCESS_WF, CRON_WF, RATE_LIMITED_WF])
worker.start
```


> **Warning:** Always set **timeouts** and **retries** on scrape tasks. Pages can hang
>   indefinitely, and transient network failures are common. See
>   [Timeouts](/v1/timeouts) and [Retry Policies](/v1/retry-policies).

## Common Patterns

| Pattern                 | Description                                                                                    |
| ----------------------- | ---------------------------------------------------------------------------------------------- |
| **Price monitoring**    | Scrape competitor pricing pages on a schedule; alert on changes                                |
| **Content aggregation** | Scrape multiple news sources; use LLM to deduplicate and summarize                             |
| **SEO monitoring**      | Scrape your own pages to verify meta tags, headings, and content                               |
| **Lead enrichment**     | Scrape company websites to enrich CRM records with latest info                                 |
| **Documentation sync**  | Scrape external docs; chunk and embed for RAG (see [RAG & Indexing](/guides/rag-and-indexing)) |
| **Compliance checking** | Scrape regulatory pages; alert when content changes                                            |

## Related Patterns


  
    Cron expressions and one-time scheduled runs for periodic scraping.
  
  
    Fan out scrapes across many URLs in parallel with concurrency control.
  
  
    Chunk and embed scraped content for retrieval-augmented generation.
  
  
    Extract structured data from scraped documents with OCR and LLM pipelines.
  


## Next Steps

- [Cron Triggers](/v1/cron-runs): cron expression syntax and configuration
- [Retry Policies](/v1/retry-policies): handle transient scraping failures
- [Rate Limits](/v1/rate-limits): throttle requests to avoid being blocked
- [Concurrency Control](/v1/concurrency): limit parallel scrapes per domain


---

<!-- Source: https://docs.hatchet.run/self-hosting/index -->

# Self-Hosting the Hatchet Control Plane

Self-hosting Hatchet means running your own instance of the **Hatchet Control Plane** - the central orchestration system that manages workflows, schedules tasks, and coordinates worker execution. This is different from running workers, which can connect to any Hatchet instance (self-hosted or Hatchet Cloud).

## What You're Self-Hosting

When you self-host Hatchet, you're deploying:

- **API Server** - REST APIs for workflow management
- **Engine** - gRPC API for core workflow orchestration and task scheduling
- **Database** - PostgreSQL for storing workflow state and metadata
- **Message Queue (optional)** - RabbitMQ for inter-service communication and high-throughput real-time updates
- **Dashboard** - Web UI for monitoring workflows and debugging

Your **workers** (the processes that execute your workflow steps) will connect to your self-hosted control plane and execute tasks.

## Deployment Options

The fastest way to get a Hatchet instance running locally is with the [Hatchet CLI](/cli) (which wraps Hatchet Lite):

```sh
hatchet server start
```

There are currently three supported ways to self-host the Hatchet Control Plane:

Docker:

1. [Hatchet Lite](./self-hosting/hatchet-lite.mdx) - Single docker image with bundled engine and API (development, testing, or low-throughput production)
2. [Docker Compose](./self-hosting/docker-compose.mdx) - Multi-container setup with PostgreSQL and RabbitMQ (production)

Kubernetes:

1. [Quickstart with Helm](./self-hosting/kubernetes-quickstart.mdx) - Production-ready Helm charts (production)


---

<!-- Source: https://docs.hatchet.run/self-hosting/hatchet-lite -->

# Hatchet Lite Deployment

To get up and running quickly, you can deploy via the `hatchet-lite` image. This image is designed for development and low-volume use-cases.


### Prerequisites

This deployment requires [Docker](https://docs.docker.com/engine/install/) installed locally to work.

### Getting Hatchet Lite Running

#### Hatchet CLI

The easiest way to get Hatchet Lite running is via the Hatchet CLI. Simply run the following command:

```sh
hatchet server start
```

#### With Postgres (Default)

To use Postgres as both your DB and message queue, copy the following `docker-compose.hatchet.yml` file to the root of your repository:

> **Info:** If you have an existing Postgres instance already running, you can simply
>   point `DATABASE_URL` to that instance and ignore the `postgres` service
>   deployment in the following docker-compose file.

```yaml filename="docker-compose.hatchet.yml" copy
version: "3.8"
name: hatchet-lite
services:
  postgres:
    image: postgres:15.6
    command: postgres -c 'max_connections=200'
    restart: always
    environment:
      - POSTGRES_USER=hatchet
      - POSTGRES_PASSWORD=hatchet
      - POSTGRES_DB=hatchet
    volumes:
      - hatchet_lite_postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -d hatchet -U hatchet"]
      interval: 10s
      timeout: 10s
      retries: 5
      start_period: 10s
  hatchet-lite:
    image: ghcr.io/hatchet-dev/hatchet/hatchet-lite:latest
    ports:
      - "8888:8888"
      - "7077:7077"
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      # Refer to https://docs.hatchet.run/self-hosting/configuration-options
      # for a list of all supported environment variables
      DATABASE_URL: "postgresql://hatchet:hatchet@postgres:5432/hatchet?sslmode=disable"
      SERVER_AUTH_COOKIE_DOMAIN: localhost
      SERVER_AUTH_COOKIE_INSECURE: "t"
      SERVER_GRPC_BIND_ADDRESS: "0.0.0.0"
      SERVER_GRPC_INSECURE: "t"
      SERVER_GRPC_BROADCAST_ADDRESS: localhost:7077
      SERVER_GRPC_PORT: "7077"
      SERVER_URL: http://localhost:8888
      SERVER_AUTH_SET_EMAIL_VERIFIED: "t"
      SERVER_DEFAULT_ENGINE_VERSION: "V1"
      SERVER_INTERNAL_CLIENT_INTERNAL_GRPC_BROADCAST_ADDRESS: localhost:7077
    volumes:
      - "hatchet_lite_config:/config"

volumes:
  hatchet_lite_postgres_data:
  hatchet_lite_config:
```

Then run `docker-compose -f docker-compose.hatchet.yml up` to get the Hatchet Lite instance running.

#### With Postgres + RabbitMQ

To use Postgres as your DB and RabbitMQ as the message queue, copy the following `docker-compose.hatchet.yml` file to the root of your repository:

> **Info:** If you have an existing Postgres instance already running, you can simply
>   point `DATABASE_URL` to that instance and ignore the `postgres` service
>   deployment in the following docker-compose file.

```yaml filename="docker-compose.hatchet.yml" copy
version: "3.8"
name: hatchet-lite
services:
  postgres:
    image: postgres:15.6
    command: postgres -c 'max_connections=200'
    restart: always
    environment:
      - POSTGRES_USER=hatchet
      - POSTGRES_PASSWORD=hatchet
      - POSTGRES_DB=hatchet
    volumes:
      - hatchet_lite_postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -d hatchet -U hatchet"]
      interval: 10s
      timeout: 10s
      retries: 5
      start_period: 10s
  rabbitmq:
    image: "rabbitmq:3-management"
    hostname: "rabbitmq"
    ports:
      - "5672:5672"
      - "15672:15672"
    environment:
      RABBITMQ_DEFAULT_USER: "user"
      RABBITMQ_DEFAULT_PASS: "password"
    volumes:
      - "hatchet_rabbitmq_data:/var/lib/rabbitmq"
      - "hatchet_rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf"
    healthcheck:
      test: ["CMD", "rabbitmqctl", "status"]
      interval: 30s
      timeout: 10s
      retries: 5
  hatchet-lite:
    image: ghcr.io/hatchet-dev/hatchet/hatchet-lite:latest
    ports:
      - "8888:8888"
      - "7077:7077"
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      SERVER_MSGQUEUE_KIND: rabbitmq
      SERVER_MSGQUEUE_RABBITMQ_URL: "amqp://user:password@rabbitmq:5672/"
      # Refer to https://docs.hatchet.run/self-hosting/configuration-options
      # for a list of all supported environment variables
      DATABASE_URL: "postgresql://hatchet:hatchet@postgres:5432/hatchet?sslmode=disable"
      SERVER_AUTH_COOKIE_DOMAIN: localhost
      SERVER_AUTH_COOKIE_INSECURE: "t"
      SERVER_GRPC_BIND_ADDRESS: "0.0.0.0"
      SERVER_GRPC_INSECURE: "t"
      SERVER_GRPC_BROADCAST_ADDRESS: localhost:7077
      SERVER_GRPC_PORT: "7077"
      SERVER_URL: http://localhost:8888
      SERVER_AUTH_SET_EMAIL_VERIFIED: "t"
      SERVER_DEFAULT_ENGINE_VERSION: "V1"
    volumes:
      - "hatchet_lite_config:/config"

volumes:
  hatchet_lite_postgres_data:
  hatchet_lite_config:
  hatchet_rabbitmq_data:
  hatchet_rabbitmq.conf:
```

Then run `docker-compose -f docker-compose.hatchet.yml up` to get the Hatchet Lite instance running.

### Accessing Hatchet Lite

Once the Hatchet Lite instance is running, you can access the Hatchet Lite UI at [http://localhost:8888](http://localhost:8888).

By default, a user is created with the following credentials:

```
Email: admin@example.com
Password: Admin123!!
```

After logging in, follow the steps in the UI to create your first tenant and run your first workflow!


---

<!-- Source: https://docs.hatchet.run/self-hosting/docker-compose -->

# Docker Compose Deployment

This guide shows how to deploy Hatchet using Docker Compose for a production-ready deployment. If you'd like to get up and running quickly, you can also deploy Hatchet using the `hatchet-lite` image following the tutorial here: [Hatchet Lite Deployment](/self-hosting/hatchet-lite).

This guide uses RabbitMQ as a message broker for Hatchet. This is optional: if you'd like to use Postgres as a message broker, modify the `setup-config` service in the `docker-compose.yml` file with the following env var, and delete all RabbitMQ references:

```sh
SERVER_MSGQUEUE_KIND=postgres
```

## Quickstart


### Prerequisites

This deployment requires [Docker](https://docs.docker.com/engine/install/) installed locally to work.

### Create files

We will be creating a `docker-compose.yml` file in the root of your repository:

```
root/
  docker-compose.yml
docker-compose.yml
```

```yaml filename="docker-compose.yml" copy
version: "3.8"
services:
  postgres:
    image: postgres:15.6
    command: postgres -c 'max_connections=1000'
    restart: always
    hostname: "postgres"
    environment:
      - POSTGRES_USER=hatchet
      - POSTGRES_PASSWORD=hatchet
      - POSTGRES_DB=hatchet
    ports:
      - "5435:5432"
    volumes:
      - hatchet_postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -d hatchet -U hatchet"]
      interval: 10s
      timeout: 10s
      retries: 5
      start_period: 10s
  rabbitmq:
    image: "rabbitmq:3-management"
    hostname: "rabbitmq"
    ports:
      - "5673:5672" # RabbitMQ
      - "15673:15672" # Management UI
    environment:
      RABBITMQ_DEFAULT_USER: "user"
      RABBITMQ_DEFAULT_PASS: "password"
    volumes:
      - "hatchet_rabbitmq_data:/var/lib/rabbitmq"
      - "hatchet_rabbitmq.conf:/etc/rabbitmq/rabbitmq.conf" # Configuration file mount
    healthcheck:
      test: ["CMD", "rabbitmqctl", "status"]
      interval: 10s
      timeout: 10s
      retries: 5
  migration:
    image: ghcr.io/hatchet-dev/hatchet/hatchet-migrate:latest
    command: /hatchet/hatchet-migrate
    environment:
      DATABASE_URL: "postgres://hatchet:hatchet@postgres:5432/hatchet"
    depends_on:
      postgres:
        condition: service_healthy
  setup-config:
    image: ghcr.io/hatchet-dev/hatchet/hatchet-admin:latest
    command: /hatchet/hatchet-admin quickstart --skip certs --generated-config-dir /hatchet/config --overwrite=false
    environment:
      DATABASE_URL: "postgres://hatchet:hatchet@postgres:5432/hatchet"
      SERVER_MSGQUEUE_RABBITMQ_URL: amqp://user:password@rabbitmq:5672/
      SERVER_AUTH_COOKIE_DOMAIN: localhost:8080
      SERVER_AUTH_COOKIE_INSECURE: "t"
      SERVER_GRPC_BIND_ADDRESS: "0.0.0.0"
      SERVER_GRPC_INSECURE: "t"
      SERVER_GRPC_BROADCAST_ADDRESS: localhost:7077
      SERVER_DEFAULT_ENGINE_VERSION: "V1"
      SERVER_INTERNAL_CLIENT_INTERNAL_GRPC_BROADCAST_ADDRESS: hatchet-engine:7070
    volumes:
      - hatchet_certs:/hatchet/certs
      - hatchet_config:/hatchet/config
    depends_on:
      migration:
        condition: service_completed_successfully
      rabbitmq:
        condition: service_healthy
      postgres:
        condition: service_healthy
  hatchet-engine:
    image: ghcr.io/hatchet-dev/hatchet/hatchet-engine:latest
    command: /hatchet/hatchet-engine --config /hatchet/config
    restart: on-failure
    depends_on:
      setup-config:
        condition: service_completed_successfully
      migration:
        condition: service_completed_successfully
    ports:
      - "7077:7070"
    environment:
      DATABASE_URL: "postgres://hatchet:hatchet@postgres:5432/hatchet"
      SERVER_GRPC_BIND_ADDRESS: "0.0.0.0"
      SERVER_GRPC_INSECURE: "t"
    volumes:
      - hatchet_certs:/hatchet/certs
      - hatchet_config:/hatchet/config
  hatchet-dashboard:
    image: ghcr.io/hatchet-dev/hatchet/hatchet-dashboard:latest
    command: sh ./entrypoint.sh --config /hatchet/config
    ports:
      - 8080:80
    restart: on-failure
    depends_on:
      setup-config:
        condition: service_completed_successfully
      migration:
        condition: service_completed_successfully
    environment:
      DATABASE_URL: "postgres://hatchet:hatchet@postgres:5432/hatchet"
    volumes:
      - hatchet_certs:/hatchet/certs
      - hatchet_config:/hatchet/config

volumes:
  hatchet_postgres_data:
  hatchet_rabbitmq_data:
  hatchet_rabbitmq.conf:
  hatchet_config:
  hatchet_certs:
```

### Get Hatchet up and running

To start the services, run the following command in the root of your repository:

```bash
docker compose up
```

Wait for the `hatchet-engine` and `hatchet-dashboard` services to start.

### Accessing Hatchet

Once the Hatchet instance is running, you can access the Hatchet UI at [http://localhost:8080](http://localhost:8080).

By default, a user is created with the following credentials:

```
Email: admin@example.com
Password: Admin123!!
```

## Run tasks against the Hatchet instance

To run tasks against this instance, you will first need to create an API token for your worker. There are two ways to do this:

1. **Using a CLI command**:

   You can run the following command to create a token:

   ```sh
   docker compose run --no-deps setup-config /hatchet/hatchet-admin token create --config /hatchet/config --tenant-id 707d0855-80ab-4e1f-a156-f1c4546cbf52
   ```

2. **Using the Hatchet dashboard**:
   - Log in to the Hatchet dashboard.
   - Navigate to the "Settings" page.
   - Click on the "API Tokens" tab.
   - Click on "Create API Token".

Now that you have an API token, see the guide [here](https://docs.hatchet.run/home/setup) for how to run your first task.


## Repulling images

The docker compose file above uses the `latest` tag for all images. This means that if you want to pull the latest version of the images, you can run the following command:

```bash
docker compose pull
```

## Connecting to the engine from within Docker

If you're also running your worker application inside of `docker-compose`, you should modify the `SERVER_GRPC_BROADCAST_ADDRESS` environment variable in the `setup-config` service to use `hatchet-engine` as the hostname. For example:

```yaml
SERVER_GRPC_BROADCAST_ADDRESS: "hatchet-engine:7077"
```

Make sure your worker depends on hatchet-engine:

```yaml
worker:
  depends_on:
    hatchet-engine:
      condition: service_started
```

> **Info:** **Note:** modifying the GRPC broadcast address or server URL will require
>   re-issuing an API token.

## Additional Docker configuration

### Increase Postgres shared memory

By default, containers have a 64 MB shared memory segment (`/dev/shm`). For larger Hatchet deployments this can be too small and may lead to slow queries or an unresponsive dashboard. Increase the shared memory size for the `postgres` service:

```yaml filename="docker-compose.yml" copy
# ...
services:
  postgres:
    image: postgres:15.6
    shm_size: 1g # Increase shared memory (adjust as needed)
    command: postgres -c 'max_connections=1000'
    restart: always
    hostname: "postgres"
    environment:
      - POSTGRES_USER=hatchet
      - POSTGRES_PASSWORD=hatchet
      - POSTGRES_DB=hatchet
    ports:
      - "5435:5432"
    volumes:
      - hatchet_postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -d hatchet -U hatchet"]
      interval: 10s
      timeout: 10s
      retries: 5
      start_period: 10s
# ...
```


---

<!-- Source: https://docs.hatchet.run/self-hosting/kubernetes-quickstart -->

# Kubernetes Quickstart

## Prerequisites

- A Kubernetes cluster currently set as the current context in `kubectl`
- `kubectl` and `helm` installed

## Quickstart


### Get Hatchet Running

To deploy `hatchet-stack`, run the following commands:

```sh
helm repo add hatchet https://hatchet-dev.github.io/hatchet-charts
helm install hatchet-stack hatchet/hatchet-stack --set caddy.enabled=true
```

This default installation will run the Hatchet server as an internal service in the cluster and spins up a reverse proxy via `Caddy` to get local access. To view the Hatchet server, run the following command:

```sh
export NAMESPACE=default # TODO: replace with your namespace
export POD_NAME=$(kubectl get pods --namespace $NAMESPACE -l "app=caddy" -o jsonpath="{.items[0].metadata.name}")
export CONTAINER_PORT=$(kubectl get pod --namespace $NAMESPACE $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
kubectl --namespace $NAMESPACE port-forward $POD_NAME 8080:$CONTAINER_PORT
```

And then navigate to `http://localhost:8080` to see the Hatchet frontend running. You can log into Hatchet with the following credentials:

```
Email: admin@example.com
Password: Admin123!!
```

### Port forward to the Hatchet engine

```sh
export NAMESPACE=default # TODO: replace with your namespace
export POD_NAME=$(kubectl get pods --namespace $NAMESPACE -l "app.kubernetes.io/name=engine" -o jsonpath="{.items[0].metadata.name}")
export CONTAINER_PORT=$(kubectl get pod --namespace $NAMESPACE $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
kubectl --namespace $NAMESPACE port-forward $POD_NAME 7070:$CONTAINER_PORT
```

This will spin up the Hatchet engine service on `localhost:7070` which you can then connect to from the examples.

### Generate an API token

To generate an API token, navigate to the `Settings` tab in the Hatchet frontend and click on the `API Tokens` tab. Click the `Generate API Token` button to create a new token. Store this token somewhere safe.

### Run your first worker

Now that you have an API token, see the guide [here](https://docs.hatchet.run/home/setup) for how to run your first task.


---

<!-- Source: https://docs.hatchet.run/self-hosting/kubernetes-glasskube -->

# Kubernetes Deployment via Glasskube

## Prerequisites

- A Kubernetes cluster currently set as the current context in `kubectl`
- `docker`, `openssl`, `kubectl` and [`glasskube`](https://glasskube.dev) installed

## What is Glasskube?

[Glasskube](https://glasskube.dev) is an alternative package manager for Kubernetes and part of the CNCF landscape. Glasskube is designed as a Cloud Native application and every installed package is represented by a Custom Resource.


[`glasskube/glasskube`](https://github.com/glasskube/glasskube/) is in active development, with _good first issues_
available for new contributors.


## Quickstart


### Generate encryption keys

There are 4 encryption secrets required for Hatchet to run which can be generated via the following bash script (requires `docker` and `openssl`):

```sh filename=generate.sh copy
#!/bin/bash

# Define an alias for generating random strings. This needs to be a function in a script.
randstring() {
    openssl rand -base64 69 | tr -d "\n=+/" | cut -c1-$1
}

# Create keys directory
mkdir -p ./keys

# Function to clean up the keys directory
cleanup() {
    rm -rf ./keys
}

# Register the cleanup function to be called on the EXIT signal
trap cleanup EXIT

# Check if Docker is installed
if ! command -v docker &> /dev/null
then
    echo "Docker could not be found. Please install Docker."
    exit 1
fi

# Generate keysets using Docker
docker run --user $(id -u):$(id -g) -v $(pwd)/keys:/hatchet/keys ghcr.io/hatchet-dev/hatchet/hatchet-admin:latest /hatchet/hatchet-admin keyset create-local-keys --key-dir /hatchet/keys

# Read keysets from files
SERVER_ENCRYPTION_MASTER_KEYSET=$(<./keys/master.key)
SERVER_ENCRYPTION_JWT_PRIVATE_KEYSET=$(<./keys/private_ec256.key)
SERVER_ENCRYPTION_JWT_PUBLIC_KEYSET=$(<./keys/public_ec256.key)

# Generate the random strings for SERVER_AUTH_COOKIE_SECRETS
SERVER_AUTH_COOKIE_SECRET1=$(randstring 16)
SERVER_AUTH_COOKIE_SECRET2=$(randstring 16)

# Create the YAML file
cat > hatchet-secret.yaml <"
HATCHET_CLIENT_TLS_STRATEGY=none
```

You will need this in the following example.

### Port forward to the Hatchet engine

```sh
export NAMESPACE=hatchet # TODO: change if you modified the namespace
export POD_NAME=$(kubectl get pods --namespace $NAMESPACE -l "app.kubernetes.io/name=hatchet-engine,app.kubernetes.io/instance=hatchet" -o jsonpath="{.items[0].metadata.name}")
export CONTAINER_PORT=$(kubectl get pod --namespace $NAMESPACE $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
kubectl --namespace $NAMESPACE port-forward $POD_NAME 7070:$CONTAINER_PORT
```

This will spin up the Hatchet engine service on `localhost:7070` which you can then connect to from the examples.

### Generate an API token

To generate an API token, navigate to the `Settings` tab in the Hatchet frontend and click on the `API Tokens` tab. Click the `Generate API Token` button to create a new token. Store this token somewhere safe.

### Run your first worker

Now that you have an API token, see the guide [here](https://docs.hatchet.run/home/setup) for how to run your first task.


---

<!-- Source: https://docs.hatchet.run/self-hosting/networking -->

# Kubernetes Networking

## Overview

By default, the Kubernetes Helm chart does not expose any of the Hatchet services over an ingress. There are three services which can possibly be exposed:

1. `hatchet-engine`
2. `hatchet-stack-api`
3. `hatchet-stack-frontend`

To expose these services, you will need to do the following:

1. Configure ingresses for `frontend` and `engine` services (and optionally the `api` service). We recommend configuring the ingress to reverse proxy `/api` endpoints to the `hatchet-stack-api` service, and configuring a separate ingress to proxy to `hatchet-engine`.

2. Update the following configuration variables:

```yaml
api:
  env:
    SERVER_AUTH_COOKIE_DOMAIN: "hatchet.example.com" # example.com should be replaced with your domain
    SERVER_URL: "https://hatchet.example.com" # example.com should be replaced with your domain
    SERVER_GRPC_BIND_ADDRESS: "0.0.0.0"
    SERVER_GRPC_INSECURE: "false"
    SERVER_GRPC_BROADCAST_ADDRESS: "hatchet-engine.example.com:443" # example.com should be replaced with your domain

engine:
  env:
    SERVER_AUTH_COOKIE_DOMAIN: "hatchet.example.com" # example.com should be replaced with your domain
    SERVER_URL: "https://hatchet.example.com" # example.com should be replaced with your domain
    SERVER_GRPC_BIND_ADDRESS: "0.0.0.0"
    SERVER_GRPC_INSECURE: "false"
    SERVER_GRPC_BROADCAST_ADDRESS: "engine.hatchet.example.com:443" # example.com should be replaced with your domain
```

## Example: `nginx-ingress`

Let's walk through an example of exposing Hatchet over `hatchet.example.com` (for the API and frontend) and `engine.hatchet.example.com` (for the engine).

We'll be deploying this with SSL enabled, which requires a valid certificate. We recommend using [cert-manager](https://cert-manager.io/docs/) to manage your certificates. This guide assumes that you have a cert-manager `ClusterIssuer` called `letsencrypt-prod` configured.

Here's an example `values.yaml` file for this setup:

```yaml
api:
  env:
    # TODO: insert these values from the output of the keyset generation command
    SERVER_AUTH_COOKIE_SECRETS: "$SERVER_AUTH_COOKIE_SECRET1 $SERVER_AUTH_COOKIE_SECRET2"
    SERVER_ENCRYPTION_MASTER_KEYSET: "$SERVER_ENCRYPTION_MASTER_KEYSET"
    SERVER_ENCRYPTION_JWT_PRIVATE_KEYSET: "$SERVER_ENCRYPTION_JWT_PRIVATE_KEYSET"
    SERVER_ENCRYPTION_JWT_PUBLIC_KEYSET: "$SERVER_ENCRYPTION_JWT_PUBLIC_KEYSET"
    SERVER_AUTH_COOKIE_DOMAIN: "hatchet.example.com" # example.com should be replaced with your domain
    SERVER_URL: "https://hatchet.example.com" # example.com should be replaced with your domain
    SERVER_GRPC_BIND_ADDRESS: "0.0.0.0"
    SERVER_GRPC_INSECURE: "false"
    SERVER_GRPC_BROADCAST_ADDRESS: "engine.hatchet.example.com:443" # example.com should be replaced with your domain

engine:
  env:
    # TODO: insert these values from the output of the keyset generation command
    SERVER_AUTH_COOKIE_SECRETS: "$SERVER_AUTH_COOKIE_SECRET1 $SERVER_AUTH_COOKIE_SECRET2"
    SERVER_ENCRYPTION_MASTER_KEYSET: "$SERVER_ENCRYPTION_MASTER_KEYSET"
    SERVER_ENCRYPTION_JWT_PRIVATE_KEYSET: "$SERVER_ENCRYPTION_JWT_PRIVATE_KEYSET"
    SERVER_ENCRYPTION_JWT_PUBLIC_KEYSET: "$SERVER_ENCRYPTION_JWT_PUBLIC_KEYSET"
    SERVER_AUTH_COOKIE_DOMAIN: "hatchet.example.com" # example.com should be replaced with your domain
    SERVER_URL: "https://hatchet.example.com" # example.com should be replaced with your domain
    SERVER_GRPC_BIND_ADDRESS: "0.0.0.0"
    SERVER_GRPC_INSECURE: "false"
    SERVER_GRPC_BROADCAST_ADDRESS: "engine.hatchet.example.com:443" # example.com should be replaced with your domain
  ingress:
    enabled: true
    ingressClassName: nginx
    labels: {}
    annotations:
      cert-manager.io/cluster-issuer: letsencrypt-prod
      nginx.ingress.kubernetes.io/auth-tls-verify-client: "optional"
      nginx.ingress.kubernetes.io/auth-tls-secret: "${kubernetes_namespace.cloud.metadata[0].name}/engine-cert"
      nginx.ingress.kubernetes.io/auth-tls-verify-depth: "1"
      nginx.ingress.kubernetes.io/auth-tls-pass-certificate-to-upstream: "true"
      nginx.ingress.kubernetes.io/backend-protocol: "GRPC"
      nginx.ingress.kubernetes.io/ssl-redirect: "true"
      nginx.ingress.kubernetes.io/grpc-backend: "true"
      nginx.ingress.kubernetes.io/server-snippet: |
        grpc_read_timeout 1d;
        grpc_send_timeout 1h;
        client_header_timeout 1h;
        client_body_timeout 1h;
    hosts:
      - host: engine.hatchet.example.com
        paths:
          - path: /
        backend:
          serviceName: hatchet-engine
          servicePort: 7070
    tls:
      - hosts:
          - engine.hatchet.example.com
        secretName: engine-cert
        servicePort: 7070

frontend:
  ingress:
    enabled: true
    ingressClassName: nginx
    labels: {}
    annotations:
      nginx.ingress.kubernetes.io/proxy-body-size: 50m
      nginx.ingress.kubernetes.io/proxy-send-timeout: "60"
      nginx.ingress.kubernetes.io/proxy-read-timeout: "60"
      nginx.ingress.kubernetes.io/proxy-connect-timeout: "60"
      cert-manager.io/cluster-issuer: letsencrypt-prod
    hosts:
      - host: hatchet.example.com
        paths:
          - path: /api
            backend:
              serviceName: hatchet-api
              servicePort: 8080
          - path: /
            backend:
              serviceName: hatchet-frontend
              servicePort: 8080
    tls:
      - secretName: hatchet-api
        hosts:
          - hatchet.example.com
```


---

<!-- Source: https://docs.hatchet.run/self-hosting/kubernetes-helm-configuration -->

# Configuring the Helm Chart

## Shared Config

For the `hatchet-stack` and `hatchet-ha` Helm charts, the `sharedConfig` object in the `values.yaml` file allows you to configure shared settings for all backend services. The default values are:

```yaml
sharedConfig:
  # you can disable shared config by setting this to false
  enabled: true

  # these are the most commonly configured values
  serverUrl: "http://localhost:8080"
  serverAuthCookieDomain: "localhost:8080" # the domain for the auth cookie
  serverAuthCookieInsecure: "t" # allows cookies to be set over http
  serverAuthSetEmailVerified: "t" # automatically sets email_verified to true for all users
  serverAuthBasicAuthEnabled: "t" # allows login via basic auth (email/password)
  grpcBroadcastAddress: "localhost:7070" # the endpoint for the gRPC server, exposed via the `grpc` service
  grpcInsecure: "true" # allows gRPC to be served over http
  defaultAdminEmail: "admin@example.com" # in exposed/production environments, change this to a valid email
  defaultAdminPassword: "Admin123!!" # in exposed/production environments, change this to a secure password

  # you can set additional environment variables here, which will override any defaults
  env: {}
```

### Networking

- **`sharedConfig.serverUrl`** (default: `"http://localhost:8080"`): specifies the base URL for the server. This URL should be the public-facing URL of the Hatchet API server (which is typically bundled behind a reverse proxy with the Hatchet frontend).

- **`sharedConfig.grpcBroadcastAddress`** (default: `"localhost:7070"`): defines the address for the gRPC server endpoint, which is exposed via the `grpc` service.

- **`sharedConfig.grpcInsecure`** (default: `"true"`): when set to `true`, allows the gRPC server to be served over HTTP instead of HTTPS. Use this in non-production environments only.

### Authentication

- **`sharedConfig.serverAuthCookieDomain`** (default: `"localhost:8080"`): specifies the domain for the authentication cookie. Should be set to the appropriate domain when deploying to production.

- **`sharedConfig.serverAuthCookieInsecure`** (default: `"t"`): if set to `"t"`, allows authentication cookies to be set over HTTP, useful for local development. In production, use a secure setting.

- **`sharedConfig.serverAuthSetEmailVerified`** (default: `"t"`): automatically sets `email_verified` to `true` for all users. This is useful for testing environments where email verification is not necessary.

- **`sharedConfig.serverAuthBasicAuthEnabled`** (default: `"t"`): enables basic authentication (using email and password) for users. Should be enabled if the system needs to support user logins via email/password.

- **`sharedConfig.defaultAdminEmail`** (default: `"admin@example.com"`): specifies the email for the default administrator account. Change this to a valid email when deploying to production environments.

- **`sharedConfig.defaultAdminPassword`** (default: `"Admin123!!"`): defines the password for the default administrator account. This should be changed to a strong password for production deployments.

### Additional Env Variables

You can set additional environment variables for the backend services using the `env` object. For example:

```yaml
sharedConfig:
  env:
    MY_ENV_VAR: "my-value"
```

This will set the environment variable `MY_ENV_VAR` to `"my-value"` for all backend services. These values will override any default environment settings for the services.

### Seeding Data

The `sharedConfig` object also allows you to seed the database with a default tenant and user. The following environment variables are used for seeding:

````yaml
The following environment variables are used to seed the database:

```yaml
seed:
  defaultAdminEmail: "admin@example.com" # in exposed/production environments, change this to a valid email
  defaultAdminPassword: "Admin123!!" # in exposed/production environments, change this to a secure password
  env:
    ADMIN_NAME: "Admin User"
    DEFAULT_TENANT_NAME: "Default"
    DEFAULT_TENANT_SLUG: "default"
    DEFAULT_TENANT_ID: "707d0855-80ab-4e1f-a156-f1c4546cbf52"
````


---

<!-- Source: https://docs.hatchet.run/self-hosting/kubernetes-external-database -->

# Setting up Hatchet with an external database

## Connecting to Postgres

To connect to an external Postgres instance, set `postgres.enabled` to `false` in the `values.yaml` file. This will disable the internal Postgres instance and allow you to connect to an external database. You should then add the following configuration for the `hatchet-stack` or `hatchet-ha` charts:

> Note: Either `DATABASE_URL` or `DATABASE_POSTGRES_*` are required

```yaml
sharedConfig:
  env:
    DATABASE_URL: "postgres://<user>:<password>@<host>:5432/<db-name>?sslmode=disable"
    DATABASE_POSTGRES_HOST: "<host>"
    DATABASE_POSTGRES_PORT: "5432"
    DATABASE_POSTGRES_USERNAME: "<user>"
    DATABASE_POSTGRES_PASSWORD: "<password>"
    DATABASE_POSTGRES_DB_NAME: "<db-name>"
    DATABASE_POSTGRES_SSL_MODE: "disable"
```

## Mounting environment variables

Environment variables can also be mounted from secrets or configmaps via the `deploymentEnvFrom` field, which corresponds to the `envFrom` field in a Kubernetes deployment. For example, to mount the `DATABASE_URL` environment variable from a secret, you can use the following configuration:

```yaml
hatchet-api:
  deploymentEnvFrom:
    - secretRef:
        name: hatchet-api-secrets
        key: DATABASE_URL

hatchet-engine:
  deploymentEnvFrom:
    - secretRef:
        name: hatchet-api-secrets
        key: DATABASE_URL
```

For more information on mounting environment variables from secrets, refer to the [Kubernetes documentation](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#configure-all-key-value-pairs-in-a-secret-as-container-environment-variables).

## Migrations

In order for migrations to run, the database user requires permissions to write and modify schemas **on a clean database**. It is therefore recommended to create a separate database instance where Hatchet can run and grant permissions on this database to the Hatchet user. For example, to create a new database and user `hatchet` in Postgres, run the following commands (**warning:** change the username/password for production usage):

```sql
create database hatchet;

create role hatchet
with
    login password 'hatchet';

grant hatchet to postgres;

alter database hatchet owner to hatchet;
```


---

<!-- Source: https://docs.hatchet.run/self-hosting/high-availability -->

# High Availability

If you are running Hatchet in a high-throughput production environment, you may want to set up an HA (High Availability) configuration to ensure that your system remains available in the event of infrastructure failures or other issues.

There are multiple levels that you can configure Hatchet to be high availability:

- At the **database level** by using a managed Postgres provider like AWS RDS or Google Cloud SQL which supports HA options.
- At the **RabbitMQ level** by configuring the RabbitMQ cluster to have at least 3 replicas across multiple zones within a region.
- At the **Hatchet Engine/API level** by running multiple instances of the Hatchet engine behind a load balancer and splitting the different Hatchet services into separate deployments.

This guide will focus on the last level of high availability.


To view an end-to-end example of configuring Hatchet for high availability on GCP using Terraform, check out the GCP deployment guide [here](https://github.com/hatchet-dev/hatchet-infra-examples/blob/main/self-hosting/gcp)


## HA Helm Chart

Hatchet offers an HA Helm chart that can be used to deploy Hatchet in a high availability configuration. To use this Helm chart:

```sh
helm repo add hatchet https://hatchet-dev.github.io/hatchet-charts
helm install hatchet-ha hatchet/hatchet-ha
```

This chart accepts the same parameters as `hatchet-stack` for the top-level `api`, `frontend`, `postgres` and `rabbitmq` objects, but you can additionally configure the following services:

```yaml
grpc:
  replicaCount: 4
controllers:
  replicaCount: 2
scheduler:
  replicaCount: 2
```

See the [Helm configuration](./kubernetes-helm-configuration) guide for more information on configuring the Hatchet Helm charts.


---

<!-- Source: https://docs.hatchet.run/self-hosting/configuration-options -->

# Configuration Options

The Hatchet server and engine can be configured via environment variables using several prefixes. This document contains a comprehensive list of all 197+ available options organized by component.

## Environment Variable Prefixes

Hatchet uses the following environment variable prefixes:

- **`SERVER_`** (173 variables) - Main server configuration including runtime, authentication, encryption, monitoring, and integrations
- **`DATABASE_`** (19 variables) - PostgreSQL database connection and configuration
- **`READ_REPLICA_`** (4 variables) - Read replica database configuration
- **`ADMIN_`** (3 variables) - Administrator user setup for initial seeding
- **`DEFAULT_`** (3 variables) - Default tenant configuration
- **`SCHEDULER_`** (1 variable) - Scheduler-specific rate limiting
- **`SEED_`** (1 variable) - Development environment seeding
- **`CACHE_`** (1 variable) - Cache duration settings

_Note: This documentation excludes `HATCHET*CLIENT*_` variables which are specific to Go SDK client configuration.\*

## Required Environment Variables

The following variables are **absolutely required** for Hatchet to start successfully:

### Encryption Keys (Required - Choose One Strategy)

**Option A: Local Encryption Keys**

```bash
SERVER_ENCRYPTION_MASTER_KEYSET="<base64-encoded-keyset>"
SERVER_ENCRYPTION_JWT_PUBLIC_KEYSET="<base64-encoded-jwt-public>"
SERVER_ENCRYPTION_JWT_PRIVATE_KEYSET="<base64-encoded-jwt-private>"
```

**Option B: File-based Keys**

```bash
SERVER_ENCRYPTION_MASTER_KEYSET_FILE="/path/to/master.keyset"
SERVER_ENCRYPTION_JWT_PUBLIC_KEYSET_FILE="/path/to/jwt-public.keyset"
SERVER_ENCRYPTION_JWT_PRIVATE_KEYSET_FILE="/path/to/jwt-private.keyset"
```

**Option C: Google Cloud KMS**

```bash
SERVER_ENCRYPTION_CLOUDKMS_ENABLED=true
SERVER_ENCRYPTION_CLOUDKMS_KEY_URI="gcp-kms://your-key-uri"
SERVER_ENCRYPTION_CLOUDKMS_CREDENTIALS_JSON="<credentials-json>"
```

### Authentication Secrets (Required)

```bash
SERVER_AUTH_COOKIE_SECRETS="<secret1> <secret2>"
```

### Database Connection (Required)

**Option A: Connection String**

```bash
DATABASE_URL="postgresql://user:password@host:port/dbname"
```

**Option B: Individual Parameters** (uses defaults if not specified)

```bash
DATABASE_POSTGRES_HOST=your-postgres-host
DATABASE_POSTGRES_PASSWORD=your-secure-password
```

## Minimal Configuration Example

```bash
# Database
DATABASE_URL='postgresql://hatchet:hatchet@127.0.0.1:5431/hatchet'

# Encryption (using key files - recommended for development)
SERVER_ENCRYPTION_MASTER_KEYSET_FILE=./keys/master.key
SERVER_ENCRYPTION_JWT_PRIVATE_KEYSET_FILE=./keys/private_ec256.key
SERVER_ENCRYPTION_JWT_PUBLIC_KEYSET_FILE=./keys/public_ec256.key

# Authentication
SERVER_AUTH_COOKIE_SECRETS="your-secret-key-1 your-secret-key-2"
SERVER_AUTH_SET_EMAIL_VERIFIED=true

# Basic server config
SERVER_PORT=8080
SERVER_URL=http://localhost:8080

# Development settings (optional but recommended)
SERVER_GRPC_INSECURE=true
SERVER_INTERNAL_CLIENT_BASE_STRATEGY=none
SERVER_LOGGER_LEVEL=error
SERVER_LOGGER_FORMAT=console
DATABASE_LOGGER_LEVEL=error
DATABASE_LOGGER_FORMAT=console
```

Generate encryption keys with:

```bash
go run ./cmd/hatchet-admin keyset create-local-keys --key-dir ./keys
```

## Runtime Configuration

Variables marked with ⚠️ are conditionally required when specific features are enabled.

| Variable                                     | Description                             | Default Value           |
| -------------------------------------------- | --------------------------------------- | ----------------------- |
| `SERVER_PORT`                                | Port for the core server                | `8080`                  |
| `SERVER_URL`                                 | Full server URL, including protocol     | `http://localhost:8080` |
| `SERVER_GRPC_PORT`                           | Port for the GRPC service               | `7070`                  |
| `SERVER_GRPC_BIND_ADDRESS`                   | GRPC server bind address                | `127.0.0.1`             |
| `SERVER_GRPC_BROADCAST_ADDRESS`              | GRPC server broadcast address           | `127.0.0.1:7070`        |
| `SERVER_GRPC_INSECURE`                       | Controls if the GRPC server is insecure | `false`                 |
| `SERVER_SHUTDOWN_WAIT`                       | Shutdown wait duration                  | `20s`                   |
| `SERVER_ENFORCE_LIMITS`                      | Enforce tenant limits                   | `false`                 |
| `SERVER_ALLOW_SIGNUP`                        | Allow new tenant signups                | `true`                  |
| `SERVER_ALLOW_INVITES`                       | Allow new invites                       | `true`                  |
| `SERVER_ALLOW_CREATE_TENANT`                 | Allow tenant creation                   | `true`                  |
| `SERVER_ALLOW_CHANGE_PASSWORD`               | Allow password changes                  | `true`                  |
| `SERVER_HEALTHCHECK`                         | Enable healthcheck endpoint             | `true`                  |
| `SERVER_HEALTHCHECK_PORT`                    | Healthcheck port                        | `8733`                  |
| `SERVER_GRPC_MAX_MSG_SIZE`                   | gRPC max message size                   | `4194304`               |
| `SERVER_GRPC_RATE_LIMIT`                     | gRPC rate limit                         | `1000`                  |
| `SCHEDULER_CONCURRENCY_RATE_LIMIT`           | Scheduler concurrency rate limit        | `20`                    |
| `SCHEDULER_CONCURRENCY_POLLING_MIN_INTERVAL` | Minimum concurrency polling interval    | `500ms`                 |
| `SCHEDULER_CONCURRENCY_POLLING_MAX_INTERVAL` | Maximum concurrency polling interval    | `5s`                    |
| `SERVER_SERVICES`                            | Services to run                         | `["all"]`               |
| `SERVER_PAUSED_CONTROLLERS`                  | Paused controllers                      |                         |
| `SERVER_ENABLE_DATA_RETENTION`               | Enable data retention                   | `true`                  |
| `SERVER_ENABLE_WORKER_RETENTION`             | Enable worker retention                 | `false`                 |
| `SERVER_MAX_PENDING_INVITES`                 | Max pending invites                     | `100`                   |
| `SERVER_DISABLE_TENANT_PUBS`                 | Disable tenant pubsub                   |                         |
| `SERVER_MAX_INTERNAL_RETRY_COUNT`            | Max internal retry count                | `10`                    |
| `SERVER_PREVENT_TENANT_VERSION_UPGRADE`      | Prevent tenant version upgrades         | `false`                 |
| `SERVER_DEFAULT_ENGINE_VERSION`              | Default engine version                  | `V1`                    |
| `SERVER_REPLAY_ENABLED`                      | Enable task replay                      | `true`                  |

## Database Configuration

| Variable                      | Description                                                                | Default Value       |
| ----------------------------- | -------------------------------------------------------------------------- | ------------------- |
| `DATABASE_URL`                | PostgreSQL connection string                                               | `127.0.0.1`         |
| `DATABASE_POSTGRES_HOST`      | PostgreSQL host                                                            | `127.0.0.1`         |
| `DATABASE_POSTGRES_PORT`      | PostgreSQL port                                                            | `5431`              |
| `DATABASE_POSTGRES_USERNAME`  | PostgreSQL username                                                        | `hatchet`           |
| `DATABASE_POSTGRES_PASSWORD`  | PostgreSQL password                                                        | `hatchet`           |
| `DATABASE_POSTGRES_DB_NAME`   | PostgreSQL database name                                                   | `hatchet`           |
| `DATABASE_POSTGRES_SSL_MODE`  | PostgreSQL SSL mode                                                        | `disable`           |
| `DATABASE_MAX_CONNS`          | Max database connections                                                   | `50`                |
| `DATABASE_MIN_CONNS`          | Min database connections                                                   | `10`                |
| `DATABASE_MAX_QUEUE_CONNS`    | Max queue connections                                                      | `50`                |
| `DATABASE_MIN_QUEUE_CONNS`    | Min queue connections                                                      | `10`                |
| `DATABASE_MAX_CONN_LIFETIME`  | Max lifetime of a connection                                               | `15m`               |
| `DATABASE_MAX_CONN_IDLE_TIME` | Max time a connection can be idle before being closed                      | `1m`                |
| `DATABASE_LOG_QUERIES`        | Log database queries                                                       | `false`             |
| `DATABASE_PGBOUNCER_ENABLED`  | Enable pgbouncer support; requires `DATABASE_DIRECT_URL` to be set         | `false`             |
| `DATABASE_DIRECT_URL`         | Direct PostgreSQL connection string bypassing pgbouncer for DDL operations |                     |
| `DATABASE_DIRECT_MAX_CONNS`   | Max connections for the direct (non-pgbouncer) pool                        | `2`                 |
| `DATABASE_DIRECT_MIN_CONNS`   | Min connections for the direct (non-pgbouncer) pool                        | `1`                 |
| `CACHE_DURATION`              | Cache duration                                                             | `5s`                |
| `ADMIN_EMAIL`                 | Admin email for seeding                                                    | `admin@example.com` |
| `ADMIN_PASSWORD`              | Admin password for seeding                                                 | `Admin123!!`        |
| `ADMIN_NAME`                  | Admin name for seeding                                                     | `Admin`             |
| `DEFAULT_TENANT_NAME`         | Default tenant name                                                        | `Default`           |
| `DEFAULT_TENANT_SLUG`         | Default tenant slug                                                        | `default`           |
| `DEFAULT_TENANT_ID`           | Default tenant ID                                                          |                     |
| `SEED_DEVELOPMENT`            | Development seeding flag                                                   |                     |
| `READ_REPLICA_ENABLED`        | Enable read replica                                                        | `false`             |
| `READ_REPLICA_DATABASE_URL`   | Read replica database URL                                                  |                     |
| `READ_REPLICA_MAX_CONNS`      | Read replica max connections                                               | `50`                |
| `READ_REPLICA_MIN_CONNS`      | Read replica min connections                                               | `10`                |
| `DATABASE_LOGGER_LEVEL`       | Database logger level                                                      |                     |
| `DATABASE_LOGGER_FORMAT`      | Database logger format                                                     |                     |

## Security Check Configuration

| Variable                         | Description             | Default Value                  |
| -------------------------------- | ----------------------- | ------------------------------ |
| `SERVER_SECURITY_CHECK_ENABLED`  | Enable security check   | `true`                         |
| `SERVER_SECURITY_CHECK_ENDPOINT` | Security check endpoint | `https://security.hatchet.run` |

## Limit Configuration

| Variable                                        | Description                     | Default Value |
| ----------------------------------------------- | ------------------------------- | ------------- |
| `SERVER_LIMITS_DEFAULT_TENANT_RETENTION_PERIOD` | Default tenant retention period | `720h`        |
| `SERVER_LIMITS_DEFAULT_WORKER_LIMIT`            | Default worker limit            | `4`           |
| `SERVER_LIMITS_DEFAULT_WORKER_ALARM_LIMIT`      | Default worker alarm limit      | `2`           |
| `SERVER_LIMITS_DEFAULT_EVENT_LIMIT`             | Default event limit             | `1000`        |
| `SERVER_LIMITS_DEFAULT_EVENT_ALARM_LIMIT`       | Default event alarm limit       | `750`         |
| `SERVER_LIMITS_DEFAULT_EVENT_WINDOW`            | Default event window            | `24h`         |
| `SERVER_LIMITS_DEFAULT_CRON_LIMIT`              | Default cron limit              | `5`           |
| `SERVER_LIMITS_DEFAULT_CRON_ALARM_LIMIT`        | Default cron alarm limit        | `2`           |
| `SERVER_LIMITS_DEFAULT_SCHEDULE_LIMIT`          | Default schedule limit          | `1000`        |
| `SERVER_LIMITS_DEFAULT_SCHEDULE_ALARM_LIMIT`    | Default schedule alarm limit    | `750`         |
| `SERVER_LIMITS_DEFAULT_TASK_RUN_LIMIT`          | Default task run limit          | `2000`        |
| `SERVER_LIMITS_DEFAULT_TASK_RUN_ALARM_LIMIT`    | Default task run alarm limit    | `1500`        |
| `SERVER_LIMITS_DEFAULT_TASK_RUN_WINDOW`         | Default task run window         | `24h`         |
| `SERVER_LIMITS_DEFAULT_WORKER_SLOT_LIMIT`       | Default worker slot limit       | `4000`        |
| `SERVER_LIMITS_DEFAULT_WORKER_SLOT_ALARM_LIMIT` | Default worker slot alarm limit | `3000`        |

## Alerting Configuration

| Variable                               | Description                              | Default Value |
| -------------------------------------- | ---------------------------------------- | ------------- |
| `SERVER_ALERTING_SENTRY_ENABLED`       | Enable Sentry for alerting               |               |
| `SERVER_ALERTING_SENTRY_DSN`           | Sentry DSN                               |               |
| `SERVER_ALERTING_SENTRY_ENVIRONMENT`   | Sentry environment                       | `development` |
| `SERVER_ALERTING_SENTRY_SAMPLE_RATE`   | Sentry sample rate                       | `1.0`         |
| `SERVER_ANALYTICS_POSTHOG_ENABLED`     | Enable PostHog analytics                 |               |
| `SERVER_ANALYTICS_POSTHOG_API_KEY`     | PostHog API key                          |               |
| `SERVER_ANALYTICS_POSTHOG_ENDPOINT`    | PostHog endpoint                         |               |
| `SERVER_ANALYTICS_POSTHOG_FE_API_HOST` | PostHog frontend API host                |               |
| `SERVER_ANALYTICS_POSTHOG_FE_API_KEY`  | PostHog frontend API key                 |               |
| `SERVER_PYLON_ENABLED`                 | Enable Pylon                             |               |
| `SERVER_PYLON_APP_ID` ⚠️               | Pylon app ID (required if Pylon enabled) |               |
| `SERVER_PYLON_SECRET`                  | Pylon secret                             |               |

## Encryption Configuration

| Variable                                      | Description                                    | Default Value |
| --------------------------------------------- | ---------------------------------------------- | ------------- |
| `SERVER_ENCRYPTION_MASTER_KEYSET`             | Raw master keyset, base64-encoded JSON string  |               |
| `SERVER_ENCRYPTION_MASTER_KEYSET_FILE`        | Path to the master keyset file                 |               |
| `SERVER_ENCRYPTION_JWT_PUBLIC_KEYSET`         | Public JWT keyset, base64-encoded JSON string  |               |
| `SERVER_ENCRYPTION_JWT_PUBLIC_KEYSET_FILE`    | Path to the public JWT keyset file             |               |
| `SERVER_ENCRYPTION_JWT_PRIVATE_KEYSET`        | Private JWT keyset, base64-encoded JSON string |               |
| `SERVER_ENCRYPTION_JWT_PRIVATE_KEYSET_FILE`   | Path to the private JWT keyset file            |               |
| `SERVER_ENCRYPTION_CLOUDKMS_ENABLED`          | Whether Google Cloud KMS is enabled            | `false`       |
| `SERVER_ENCRYPTION_CLOUDKMS_KEY_URI`          | URI of the key in Google Cloud KMS             |               |
| `SERVER_ENCRYPTION_CLOUDKMS_CREDENTIALS_JSON` | JSON credentials for Google Cloud KMS          |               |

## Authentication Configuration

| Variable                               | Description                                                 | Default Value                    |
| -------------------------------------- | ----------------------------------------------------------- | -------------------------------- |
| `SERVER_AUTH_RESTRICTED_EMAIL_DOMAINS` | Restricted email domains                                    |                                  |
| `SERVER_AUTH_BASIC_AUTH_ENABLED`       | Whether basic auth is enabled                               | `true`                           |
| `SERVER_AUTH_SET_EMAIL_VERIFIED`       | Whether the user's email is set to verified automatically   | `false`                          |
| `SERVER_AUTH_COOKIE_NAME`              | Name of the cookie                                          | `hatchet`                        |
| `SERVER_AUTH_COOKIE_DOMAIN`            | Domain for the cookie                                       |                                  |
| `SERVER_AUTH_COOKIE_SECRETS`           | Cookie secrets                                              |                                  |
| `SERVER_AUTH_COOKIE_INSECURE`          | Whether the cookie is insecure                              | `false`                          |
| `SERVER_AUTH_GOOGLE_ENABLED`           | Whether Google auth is enabled                              | `false`                          |
| `SERVER_AUTH_GOOGLE_CLIENT_ID` ⚠️      | Google auth client ID (required if Google auth enabled)     |                                  |
| `SERVER_AUTH_GOOGLE_CLIENT_SECRET` ⚠️  | Google auth client secret (required if Google auth enabled) |                                  |
| `SERVER_AUTH_GOOGLE_SCOPES`            | Google auth scopes                                          | `["openid", "profile", "email"]` |
| `SERVER_AUTH_GITHUB_ENABLED`           | Whether GitHub auth is enabled                              | `false`                          |
| `SERVER_AUTH_GITHUB_CLIENT_ID` ⚠️      | GitHub auth client ID (required if GitHub auth enabled)     |                                  |
| `SERVER_AUTH_GITHUB_CLIENT_SECRET` ⚠️  | GitHub auth client secret (required if GitHub auth enabled) |                                  |
| `SERVER_AUTH_GITHUB_SCOPES`            | GitHub auth scopes                                          | `["read:user", "user:email"]`    |

## Task Queue Configuration

| Variable                          | Description              | Default Value |
| --------------------------------- | ------------------------ | ------------- |
| `SERVER_MSGQUEUE_KIND`            | Message queue kind       | `rabbitmq`    |
| `SERVER_MSGQUEUE_RABBITMQ_URL`    | RabbitMQ URL             |               |
| `SERVER_MSGQUEUE_RABBITMQ_QOS`    | RabbitMQ QoS             | `100`         |
| `SERVER_REQUEUE_LIMIT`            | Requeue limit            | `100`         |
| `SERVER_SINGLE_QUEUE_LIMIT`       | Single queue limit       | `100`         |
| `SERVER_UPDATE_HASH_FACTOR`       | Update hash factor       | `100`         |
| `SERVER_UPDATE_CONCURRENT_FACTOR` | Update concurrent factor | `10`          |

## TLS Configuration

| Variable                                                 | Description                      | Default Value |
| -------------------------------------------------------- | -------------------------------- | ------------- |
| `SERVER_TLS_STRATEGY`                                    | TLS strategy                     |               |
| `SERVER_TLS_CERT`                                        | TLS certificate                  |               |
| `SERVER_TLS_CERT_FILE`                                   | Path to the TLS certificate file |               |
| `SERVER_TLS_KEY`                                         | TLS key                          |               |
| `SERVER_TLS_KEY_FILE`                                    | Path to the TLS key file         |               |
| `SERVER_TLS_ROOT_CA`                                     | TLS root CA                      |               |
| `SERVER_TLS_ROOT_CA_FILE`                                | Path to the TLS root CA file     |               |
| `SERVER_TLS_SERVER_NAME`                                 | TLS server name                  |               |
| `SERVER_INTERNAL_CLIENT_BASE_STRATEGY`                   | Internal client TLS strategy     |               |
| `SERVER_INTERNAL_CLIENT_BASE_INHERIT_BASE`               | Inherit base TLS config          | `true`        |
| `SERVER_INTERNAL_CLIENT_TLS_BASE_CERT`                   | Internal client TLS cert         |               |
| `SERVER_INTERNAL_CLIENT_TLS_BASE_CERT_FILE`              | Internal client TLS cert file    |               |
| `SERVER_INTERNAL_CLIENT_TLS_BASE_KEY`                    | Internal client TLS key          |               |
| `SERVER_INTERNAL_CLIENT_TLS_BASE_KEY_FILE`               | Internal client TLS key file     |               |
| `SERVER_INTERNAL_CLIENT_TLS_BASE_ROOT_CA`                | Internal client TLS root CA      |               |
| `SERVER_INTERNAL_CLIENT_TLS_BASE_ROOT_CA_FILE`           | Internal client TLS root CA file |               |
| `SERVER_INTERNAL_CLIENT_TLS_SERVER_NAME`                 | Internal client TLS server name  |               |
| `SERVER_INTERNAL_CLIENT_INTERNAL_GRPC_BROADCAST_ADDRESS` | Internal gRPC broadcast address  |               |

## Logging Configuration

| Variable                                    | Description             | Default Value |
| ------------------------------------------- | ----------------------- | ------------- |
| `SERVER_LOGGER_LEVEL`                       | Logger level            |               |
| `SERVER_LOGGER_FORMAT`                      | Logger format           |               |
| `SERVER_LOG_INGESTION_ENABLED`              | Enable log ingestion    | `true`        |
| `SERVER_ADDITIONAL_LOGGERS_QUEUE_LEVEL`     | Queue logger level      |               |
| `SERVER_ADDITIONAL_LOGGERS_QUEUE_FORMAT`    | Queue logger format     |               |
| `SERVER_ADDITIONAL_LOGGERS_PGXSTATS_LEVEL`  | PGX stats logger level  |               |
| `SERVER_ADDITIONAL_LOGGERS_PGXSTATS_FORMAT` | PGX stats logger format |               |

## OpenTelemetry Configuration

| Variable                            | Description                                                | Default Value |
| ----------------------------------- | ---------------------------------------------------------- | ------------- |
| `SERVER_OTEL_SERVICE_NAME`          | Service name for OpenTelemetry                             |               |
| `SERVER_OTEL_COLLECTOR_URL`         | Collector URL for OpenTelemetry                            |               |
| `SERVER_OTEL_INSECURE`              | Whether to use an insecure connection to the collector URL |               |
| `SERVER_OTEL_TRACE_ID_RATIO`        | OpenTelemetry trace ID ratio                               |               |
| `SERVER_OTEL_COLLECTOR_AUTH`        | OpenTelemetry Collector Authorization header value         |               |
| `SERVER_OTEL_METRICS_ENABLED`       | Enable OpenTelemetry metrics collection                    | `false`       |
| `SERVER_PROMETHEUS_ENABLED`         | Enable Prometheus                                          | `false`       |
| `SERVER_PROMETHEUS_ADDRESS`         | Prometheus address                                         | `:9090`       |
| `SERVER_PROMETHEUS_PATH`            | Prometheus metrics path                                    | `/metrics`    |
| `SERVER_PROMETHEUS_SERVER_URL`      | Prometheus server URL                                      |               |
| `SERVER_PROMETHEUS_SERVER_USERNAME` | Prometheus server username                                 |               |
| `SERVER_PROMETHEUS_SERVER_PASSWORD` | Prometheus server password                                 |               |

## Tenant Alerting Configuration

| Variable                                     | Description                         | Default Value          |
| -------------------------------------------- | ----------------------------------- | ---------------------- |
| `SERVER_TENANT_ALERTING_SLACK_ENABLED`       | Enable Slack for tenant alerting    |                        |
| `SERVER_TENANT_ALERTING_SLACK_CLIENT_ID`     | Slack client ID                     |                        |
| `SERVER_TENANT_ALERTING_SLACK_CLIENT_SECRET` | Slack client secret                 |                        |
| `SERVER_TENANT_ALERTING_SLACK_SCOPES`        | Slack scopes                        | `["incoming-webhook"]` |
| `SERVER_EMAIL_KIND`                          | Email integration kind              | `postmark`             |
| `SERVER_EMAIL_POSTMARK_ENABLED`              | Enable Postmark                     |                        |
| `SERVER_EMAIL_POSTMARK_SERVER_KEY`           | Postmark server key                 |                        |
| `SERVER_EMAIL_POSTMARK_FROM_EMAIL`           | Postmark from email                 |                        |
| `SERVER_EMAIL_POSTMARK_FROM_NAME`            | Postmark from name                  | `Hatchet Support`      |
| `SERVER_EMAIL_POSTMARK_SUPPORT_EMAIL`        | Postmark support email              |                        |
| `SERVER_EMAIL_SMTP_ENABLED`                  | Enable SMTP                         |                        |
| `SERVER_EMAIL_SMTP_SERVER_ADDR`              | SMTP server address                 |                        |
| `SERVER_EMAIL_SMTP_FROM_EMAIL`               | SMTP from email                     |                        |
| `SERVER_EMAIL_SMTP_FROM_NAME`                | SMTP from name                      | `Hatchet Support`      |
| `SERVER_EMAIL_SMTP_SUPPORT_EMAIL`            | SMTP support email                  |                        |
| `SERVER_EMAIL_SMTP_AUTH_USERNAME`            | SMTP authentication username        |                        |
| `SERVER_EMAIL_SMTP_AUTH_PASSWORD`            | SMTP authentication password        |                        |
| `SERVER_MONITORING_ENABLED`                  | Enable monitoring                   | `true`                 |
| `SERVER_MONITORING_PERMITTED_TENANTS`        | Permitted tenants for monitoring    |                        |
| `SERVER_MONITORING_PROBE_TIMEOUT`            | Monitoring probe timeout            | `30s`                  |
| `SERVER_MONITORING_TLS_ROOT_CA_FILE`         | Monitoring TLS root CA file         |                        |
| `SERVER_SAMPLING_ENABLED`                    | Enable sampling                     | `false`                |
| `SERVER_SAMPLING_RATE`                       | Sampling rate                       | `1.0`                  |
| `SERVER_OPERATIONS_JITTER`                   | Operations jitter in milliseconds   | `0`                    |
| `SERVER_OPERATIONS_POLL_INTERVAL`            | Operations poll interval in seconds | `2`                    |

## Cron Operations Configuration

| Variable                                            | Description                                                           | Default Value |
| --------------------------------------------------- | --------------------------------------------------------------------- | ------------- |
| `SERVER_CRON_OPERATIONS_TASK_ANALYZE_CRON_INTERVAL` | Interval for running ANALYZE on task-related tables                   | `3h`          |
| `SERVER_CRON_OPERATIONS_OLAP_ANALYZE_CRON_INTERVAL` | Interval for running ANALYZE on OLAP/analytics tables                 | `3h`          |
| `SERVER_CRON_OPERATIONS_DB_HEALTH_METRICS_INTERVAL` | Interval for collecting database health metrics (OTel)                | `60s`         |
| `SERVER_CRON_OPERATIONS_OLAP_METRICS_INTERVAL`      | Interval for collecting OLAP metrics (OTel)                           | `5m`          |
| `SERVER_CRON_OPERATIONS_WORKER_METRICS_INTERVAL`    | Interval for collecting worker metrics (OTel)                         | `60s`         |
| `SERVER_CRON_OPERATIONS_YESTERDAY_RUN_COUNT_HOUR`   | Hour (0-23) at which to collect yesterday's workflow run count (OTel) | `0`           |
| `SERVER_CRON_OPERATIONS_YESTERDAY_RUN_COUNT_MINUTE` | Minute (0-59) at which to collect yesterday's workflow run count      | `5`           |
| `SERVER_WAIT_FOR_FLUSH`                             | Default wait for flush                                                | `1ms`         |
| `SERVER_MAX_CONCURRENT`                             | Default max concurrent                                                | `50`          |
| `SERVER_FLUSH_PERIOD_MILLISECONDS`                  | Default flush period                                                  | `10ms`        |
| `SERVER_FLUSH_ITEMS_THRESHOLD`                      | Default flush threshold                                               | `100`         |
| `SERVER_FLUSH_STRATEGY`                             | Default flush strategy                                                | `DYNAMIC`     |

## OLAP Database Configuration

| Variable                                          | Description                                      | Default Value |
| ------------------------------------------------- | ------------------------------------------------ | ------------- |
| `SERVER_OLAP_STATUS_UPDATE_DAG_BATCH_SIZE_LIMIT`  | Batch size limit for running DAG status updates  | `1000`        |
| `SERVER_OLAP_STATUS_UPDATE_TASK_BATCH_SIZE_LIMIT` | Batch size limit for running task status updates | `1000`        |


---

<!-- Source: https://docs.hatchet.run/self-hosting/prometheus-metrics -->

## Prometheus Metrics for Hatchet

> **Warning:** Only works with v1 tenants

This document provides an overview of the Prometheus metrics exposed by Hatchet, setup instructions for the metrics endpoint, and example PromQL queries to analyze them.

### Setup

To enable Prometheus metrics for your Hatchet instance, you can set the following environment variables. The corresponding configuration YAML values are mentioned in parantheses. If you are deploying [Hatchet in HA mode](/self-hosting/high-availability), these should be set on both the `controllers` as well as `scheduler` deployments.

- Required
  - **`SERVER_PROMETHEUS_ENABLED`** (`prometheus.enabled`)
    - Default: `false`
    - Description: Enables or disables the Prometheus metrics HTTP server.

- Optional
  - **`SERVER_PROMETHEUS_ADDRESS`** (`prometheus.address`)
    - Default: `":9090"`
    - Description: The network address and port to bind the Prometheus metrics server to.

  - **`SERVER_PROMETHEUS_PATH`** (`prometheus.path`)
    - Default: `"/metrics"`
    - Description: The HTTP path at which metrics will be exposed.

Once enabled, you can setup any scraper that supports ingesting Prometheus metrics.

#### Tenant metrics endpoint

> **Info:** This step requires communication with a service that scrapes Hatchet
>   Prometheus metrics.

To enable the [tenant API endpoint](/v1/prometheus-metrics) you can set the following environment variables:

- Required
  - **`SERVER_PROMETHEUS_SERVER_URL`** (`prometheus.prometheusServerURL`)
    - Description: The Prometheus server URL.

- Optional
  - **`SERVER_PROMETHEUS_SERVER_USERNAME`** (`prometheus.prometheusServerUsername`)
    - Description: The username to access the Prometheus instance via HTTP basic auth.

  - **`SERVER_PROMETHEUS_SERVER_PASSWORD`** (`prometheus.prometheusServerPassword`)
    - Description: The password to access the Prometheus instance via HTTP basic auth.

**Example environment setup:**

```bash
export SERVER_PROMETHEUS_ENABLED=true
export SERVER_PROMETHEUS_ADDRESS=":9999"
export SERVER_PROMETHEUS_PATH="/custom-metrics"
```

Restart your Hatchet server after setting these variables to apply the changes.

---

### Global Metrics

| Metric Name                          | Type      | Description                                                                       |
| ------------------------------------ | --------- | --------------------------------------------------------------------------------- |
| `hatchet_queue_invocations_total`    | Counter   | The total number of invocations of the queuer function                            |
| `hatchet_created_tasks_total`        | Counter   | The total number of tasks created                                                 |
| `hatchet_retried_tasks_total`        | Counter   | The total number of tasks retried                                                 |
| `hatchet_succeeded_tasks_total`      | Counter   | The total number of tasks that succeeded                                          |
| `hatchet_failed_tasks_total`         | Counter   | The total number of tasks that failed (in a final state, not including retries)   |
| `hatchet_skipped_tasks_total`        | Counter   | The total number of tasks that were skipped                                       |
| `hatchet_cancelled_tasks_total`      | Counter   | The total number of tasks cancelled                                               |
| `hatchet_assigned_tasks_total`       | Counter   | The total number of tasks assigned to a worker                                    |
| `hatchet_scheduling_timed_out_total` | Counter   | The total number of tasks that timed out while waiting to be scheduled            |
| `hatchet_rate_limited_total`         | Counter   | The total number of tasks that were rate limited                                  |
| `hatchet_queued_to_assigned_total`   | Counter   | The total number of unique tasks that were queued and later assigned to a worker  |
| `hatchet_queued_to_assigned_seconds` | Histogram | Buckets of time (in seconds) spent in the queue before being assigned to a worker |
| `hatchet_reassigned_tasks_total`     | Counter   | The total number of tasks that were reassigned to a worker                        |

#### Example PromQL Queries

##### 1. Rate of calls to the queuer method

```promql
rate(hatchet_queue_invocations_total[5m])
```

##### 2. Average queue time in milliseconds

```promql
# Calculates average queue time over the past 5 minutes, converted to ms
rate(hatchet_queued_to_assigned_seconds_sum[5m])
  / rate(hatchet_queued_to_assigned_seconds_count[5m])
  * 1e3
```

##### 3. Success and failure rates

```promql
rate(hatchet_succeeded_tasks_total[5m])
rate(hatchet_failed_tasks_total[5m])
```

##### 4. Queue time distribution (histogram)

```promql
sum by (le) (
  rate(hatchet_queued_to_assigned_seconds_bucket[5m])
)
```

##### 5. Rate of tasks created vs. retried

```promql
rate(hatchet_created_tasks_total[5m])
rate(hatchet_retried_tasks_total[5m])
```

##### 6. Task Assignment Rate

```promql
rate(hatchet_assigned_tasks_total[5m])
```

##### 7. Scheduling Timeout Rate

```promql
rate(hatchet_scheduling_timed_out_total[5m])
```

##### 8. Rate Limiting Impact

```promql
rate(hatchet_rate_limited_total[5m])
```

##### 9. Task Completion Ratio (Success vs Total)

```promql
rate(hatchet_succeeded_tasks_total[5m])
/
(rate(hatchet_succeeded_tasks_total[5m]) + rate(hatchet_failed_tasks_total[5m]))
```

##### 10. Task Cancellation Rate

```promql
rate(hatchet_cancelled_tasks_total[5m])
```

##### 11. Task Skip Rate

```promql
rate(hatchet_skipped_tasks_total[5m])
```

##### 12. Queue Processing Efficiency (Assigned vs Created)

```promql
rate(hatchet_assigned_tasks_total[5m]) / rate(hatchet_created_tasks_total[5m])
```

##### 13. Task Reassignment Rate

```promql
rate(hatchet_reassigned_tasks_total[5m])
```

### Tenant Metrics

| Metric Name                                      | Type      | Description                                                                          |
| ------------------------------------------------ | --------- | ------------------------------------------------------------------------------------ |
| `hatchet_tenant_workflow_duration_milliseconds`  | Histogram | Duration of workflow execution in milliseconds (DAGs and single tasks)               |
| `hatchet_tenant_queue_invocations_total`         | Counter   | The total number of invocations of the queuer function                               |
| `hatchet_tenant_created_tasks_total`             | Counter   | The total number of tasks created                                                    |
| `hatchet_tenant_retried_tasks_total`             | Counter   | The total number of tasks retried                                                    |
| `hatchet_tenant_succeeded_tasks_total`           | Counter   | The total number of tasks that succeeded                                             |
| `hatchet_tenant_failed_tasks_total`              | Counter   | The total number of tasks that failed (in a final state, not including retries)      |
| `hatchet_tenant_skipped_tasks_total`             | Counter   | The total number of tasks that were skipped                                          |
| `hatchet_tenant_cancelled_tasks_total`           | Counter   | The total number of tasks cancelled                                                  |
| `hatchet_tenant_assigned_tasks`                  | Counter   | The total number of tasks assigned to a worker                                       |
| `hatchet_tenant_scheduling_timed_out`            | Counter   | The total number of tasks that timed out while waiting to be scheduled               |
| `hatchet_tenant_rate_limited`                    | Counter   | The total number of tasks that were rate limited                                     |
| `hatchet_tenant_queued_to_assigned`              | Counter   | The total number of unique tasks that were queued and later got assigned to a worker |
| `hatchet_tenant_queued_to_assigned_time_seconds` | Histogram | Buckets of time in seconds spent in the queue before being assigned to a worker      |
| `hatchet_tenant_reassigned_tasks`                | Counter   | The total number of tasks that were reassigned to a worker                           |
| `hatchet_tenant_used_worker_slots`               | Gauge     | The current number of worker slots being used                                        |
| `hatchet_tenant_available_worker_slots`          | Gauge     | The current number of worker slots available (free)                                  |
| `hatchet_tenant_worker_slots`                    | Gauge     | The total number of worker slots (free + used)                                       |

#### Example PromQL Queries

##### 1. Workflow Duration by Tenant and Status

```promql
rate(hatchet_tenant_workflow_duration_milliseconds_sum[5m])
by (tenant_id, workflow_name, status)
/
rate(hatchet_tenant_workflow_duration_milliseconds_count[5m])
by (tenant_id, workflow_name, status)
```

##### 2. Tenant Queue Performance (95th percentile)

```promql
histogram_quantile(0.95,
  rate(hatchet_tenant_queued_to_assigned_time_seconds_bucket[5m])
) by (tenant_id)
```

##### 3. Tenant Error Rate by Workflow

```promql
rate(hatchet_tenant_failed_tasks_total[5m]) by (tenant_id)
/
rate(hatchet_tenant_created_tasks_total[5m]) by (tenant_id)
```

##### 4. Tenant Task Throughput

```promql
rate(hatchet_tenant_succeeded_tasks_total[5m]) by (tenant_id)
```

##### 5. Tenant Retry Rate

```promql
rate(hatchet_tenant_retried_tasks_total[5m]) by (tenant_id)
/
rate(hatchet_tenant_created_tasks_total[5m]) by (tenant_id)
```

##### 6. Workflow Duration Distribution by Tenant

```promql
sum by (tenant_id, le) (
  rate(hatchet_tenant_workflow_duration_milliseconds_bucket[5m])
)
```

##### 7. Tenant Rate Limiting Impact

```promql
rate(hatchet_tenant_rate_limited[5m]) by (tenant_id)
```

##### 8. Per-Tenant Queue Utilization

```promql
rate(hatchet_tenant_queue_invocations_total[5m]) by (tenant_id)
```

##### 9. Tenant Scheduling Timeouts

```promql
rate(hatchet_tenant_scheduling_timed_out[5m]) by (tenant_id)
```

##### 10. Tenant Task Assignment Success Rate

```promql
rate(hatchet_tenant_assigned_tasks[5m]) by (tenant_id)
/
rate(hatchet_tenant_created_tasks_total[5m]) by (tenant_id)
```

##### 11. Tenant Task Reassignment Rate

```promql
rate(hatchet_tenant_reassigned_tasks[5m]) by (tenant_id)
```

### Cross-Tenant Analysis

#### Example PromQL Queries

##### 1. Top 5 Tenants by Task Volume

```promql
topk(5,
  sum by (tenant_id) (
    rate(hatchet_tenant_created_tasks_total[1h])
  )
)
```

##### 2. Slowest Workflows Across All Tenants

```promql
topk(10,
  rate(hatchet_tenant_workflow_duration_milliseconds_sum[5m])
  /
  rate(hatchet_tenant_workflow_duration_milliseconds_count[5m])
) by (tenant_id, workflow_name)
```

##### 3. Tenant Resource Consumption Comparison

```promql
sum by (tenant_id) (
  rate(hatchet_tenant_workflow_duration_milliseconds_sum[1h])
)
/ 1000 / 60  # Convert to minutes
```

### Integration with Prometheus

This endpoint can be used to configure Prometheus to scrape tenant-specific metrics:

```yaml
scrape_configs:
  - job_name: "hatchet-tenant-metrics"
    static_configs:
      - targets: ["cloud.onhatchet.run"]
    metrics_path: "/api/v1/tenants/707d0855-80ab-4e1f-a156-f1c4546cbf52/prometheus-metrics"
    scheme: "https"
    authorization:
      credentials: "your-api-token-here"
```

**Note:** Replace `cloud.onhatchet.run` with the URL where your Hatchet instance is hosted.

This provides tenant-isolated metrics that can be scraped directly by Prometheus or consumed by other monitoring tools that support the Prometheus text format.


---

<!-- Source: https://docs.hatchet.run/self-hosting/worker-configuration-options -->

# Worker Configuration Options

The Hatchet worker can be configured via environment variables and programmatic options. This document contains a list of all available options.

## Basic Configuration

| Variable                                  | Description                         | Default Value           |
| ----------------------------------------- | ----------------------------------- | ----------------------- |
| `HATCHET_CLIENT_TOKEN`                    | Authentication token for the worker |                         |
| `HATCHET_CLIENT_HOST_PORT`                | GRPC server host and port           | \* Inherited from token |
| `HATCHET_CLIENT_API_URL` (TypeScript SDK) | API server host and port            | \* Inherited from token |
| `HATCHET_CLIENT_SERVER_URL` (Go SDK)      | API server host and port            | \* Inherited from token |
| `HATCHET_CLIENT_NAMESPACE`                | Namespace prefix for the worker     | \* Inherited from token |

## Worker Runtime Configuration

| Variable        | Description                                | Default Value |
| --------------- | ------------------------------------------ | ------------- |
| `name`          | Friendly name of the worker                |               |
| `slots`         | Maximum number of concurrent runs          | `100`         |
| `durable_slots` | Maximum number of concurrent durable tasks | `1000`        |

## Worker healthcheck server (Python SDK)

These variables enable a local HTTP server that exposes `/health` and `/metrics` for a running worker.

| Variable                                                               | Description                                                                                            | Default Value |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------- |
| `HATCHET_CLIENT_WORKER_HEALTHCHECK_ENABLED`                            | Enable the local worker healthcheck server                                                             | `false`       |
| `HATCHET_CLIENT_WORKER_HEALTHCHECK_PORT`                               | Port for the local worker healthcheck server                                                           | `8001`        |
| `HATCHET_CLIENT_WORKER_HEALTHCHECK_EVENT_LOOP_BLOCK_THRESHOLD_SECONDS` | If the worker listener process event loop is blocked longer than this threshold, `/health` returns 503 | `5.0`         |

## TLS Configuration

| Variable                          | Description                    | Default Value |
| --------------------------------- | ------------------------------ | ------------- |
| `HATCHET_CLIENT_TLS_STRATEGY`     | TLS strategy (tls, mtls, none) | `tls`         |
| `HATCHET_CLIENT_TLS_CERT_FILE`    | Path to TLS certificate file   |               |
| `HATCHET_CLIENT_TLS_KEY_FILE`     | Path to TLS key file           |               |
| `HATCHET_CLIENT_TLS_ROOT_CA_FILE` | Path to TLS root CA file       |               |
| `HATCHET_CLIENT_TLS_SERVER_NAME`  | TLS server name                |               |

## Logging Configuration

| Variable                                      | Description                                         | Default Value |
| --------------------------------------------- | --------------------------------------------------- | ------------- |
| `HATCHET_CLIENT_LOG_LEVEL`                    | Log level for the worker                            | `INFO`        |
| `HATCHET_CLIENT_GRPC_MAX_RECV_MESSAGE_LENGTH` | Maximum gRPC message receive size (Python SDK only) | `4MB`         |
| `HATCHET_CLIENT_GRPC_MAX_SEND_MESSAGE_LENGTH` | Maximum gRPC message send size (Python SDK only)    | `4MB`         |


---

<!-- Source: https://docs.hatchet.run/self-hosting/upgrading-downgrading -->

# Upgrading and Downgrading Hatchet

This guide covers how to safely upgrade and downgrade self-hosted Hatchet instances, with strategies for production-critical workloads.

## Overview

For production-critical deployments, we recommend the following workflow:

1. **Snapshot** your database before upgrading
2. **Upgrade** the Hatchet engine to the new version
3. **Verify** the upgrade is working as expected
4. If something goes wrong, **downgrade** by restoring the snapshot or running down migrations

## Step 1: Take a Database Snapshot

Before any version change, create a point-in-time snapshot of your database. This gives you a fast, reliable rollback path if the upgrade causes issues.

Refer to the backup and restore documentation for your database provider:

- **PostgreSQL (self-managed):** [Backup and Restore](https://www.postgresql.org/docs/current/backup.html)
- **AWS RDS:** [Backing Up and Restoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html)
- **Google Cloud SQL:** [Backup and Recovery](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups)
- **Azure Database for PostgreSQL:** [Backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-database-postgresql)

## Step 2: Upgrade Engine Versions

Once your snapshot is in place, upgrade the Hatchet engine.

> **Info:** Hatchet runs database migrations automatically on engine startup. No separate
>   migration step is required when upgrading.

### Docker Compose

Update the image tags in your `docker-compose.yml`:

```yaml
services:
  hatchet-engine:
    image: ghcr.io/hatchet-dev/hatchet/hatchet-engine:v0.78.26
    # ... rest of configuration

  hatchet-dashboard:
    image: ghcr.io/hatchet-dev/hatchet/hatchet-dashboard:v0.78.26
    # ... rest of configuration
```

Then redeploy:

> **Warning:** This can cause some downtime till the containers are back up.

```bash
docker-compose pull
docker-compose down
docker-compose up -d
```

### Kubernetes (Helm)

The Hatchet Helm charts use a `sharedConfig.image.tag` value that sets the image tag for all components (engine, API, frontend, migrations). Set this to the target Hatchet version:

```yaml
# values.yaml
sharedConfig:
  image:
    tag: "v0.78.26"
```

Then upgrade the release:

```bash
# hatchet-stack (standard deployment)
helm upgrade hatchet ./charts/hatchet-stack \
  --namespace hatchet \
  --values values.yaml

# hatchet-ha (high-availability deployment)
helm upgrade hatchet ./charts/hatchet-ha \
  --namespace hatchet \
  --values values.yaml
```

> **Info:** You can also override individual component tags (e.g., `engine.image.tag`,
>   `frontend.image.tag`), but `sharedConfig.image.tag` takes precedence when set.

### Verification

After upgrading, verify the deployment is healthy:

1. Check that the engine is running and accepting connections
2. Confirm the dashboard loads and shows the correct version
3. Run a test workflow to verify end-to-end functionality
4. Monitor logs for migration errors or unexpected warnings

```bash
# Docker Compose
docker-compose logs hatchet-engine | head -50

# Kubernetes
kubectl logs -n hatchet -l app=hatchet-engine --tail=50
```

## Step 3: Downgrade if Needed

If the upgrade causes issues, you have two options depending on your situation:

> **Warning:** Both the following options will result in data loss and some downtime.

### Option A: Restore from Database Snapshot (Recommended for Production)

This is the fastest and safest rollback path. It returns your database to the exact state before the upgrade, avoiding any risk of incomplete down migrations.


### Stop all Hatchet services

Shut down all Hatchet engine instances to prevent writes during the restore.

```bash
# Docker Compose
docker-compose down

# Kubernetes
kubectl scale deployment hatchet-engine -n hatchet --replicas=0
```

### Restore the database snapshot

Follow the restore procedure for your database provider (see [Step 1](#step-1-take-a-database-snapshot) for links to the relevant documentation).

### Deploy the previous Hatchet version

Update your deployment to use the previous version's image tags (see [Upgrade Engine Versions](#step-2-upgrade-engine-versions) for the relevant deployment method) and redeploy.

### Verify the rollback

Confirm the engine starts, the dashboard loads, and workflows execute correctly.


### Option B: Run Down Migrations (Manual)

If you don't have a database snapshot or prefer a more targeted rollback, you can run down migrations to revert schema changes. See the [Downgrading DB Schema Manually](/self-hosting/downgrading-db-schema-manually) guide for detailed instructions on:

- Finding the target migration version for your desired Hatchet version
- Running `hatchet-migrate --down <migration_version>`
- Deploying the older engine version

> **Warning:** Down migrations may not fully reverse all data changes (e.g., dropped columns
>   lose their data). For production-critical workloads, prefer restoring from a
>   snapshot when possible.


---

<!-- Source: https://docs.hatchet.run/self-hosting/downgrading-db-schema-manually -->

# Downgrading DB Schema Manually

This guide explains how to safely downgrade your Hatchet DB schema to a previous version.

> **Info:** For production-critical workloads, see the [Upgrading and
>   Downgrading](/self-hosting/upgrading-downgrading) guide which covers database
>   snapshots, upgrading, and safe rollback strategies.

> **Warning:** Downgrading may result in data loss. Always test downgrades in a
>   non-production environment first.

## Overview

Downgrading Hatchet involves two steps:

1. Running down migrations to revert database schema changes
2. Deploying the older Hatchet version

## Prerequisites

- **Critical:** Backup your database before downgrading
- Ensure the target version supports the current data in your database
- Have access to run `hatchet-migrate` command
- Verify that all migrations between your current version and target version have down migrations

## Finding the Target Migration Version

To downgrade to a specific Hatchet version, you need to identify the last migration that was included in that version.

Visit the Hatchet GitHub repository for your target version:

```
https://github.com/hatchet-dev/hatchet/tree/{GIT_TAG}/cmd/hatchet-migrate/migrate/migrations
```

Replace `{GIT_TAG}` with your target version (e.g., `v0.71.0`).

Find the last migration file in that directory - the timestamp at the beginning of the filename is your target migration version.

**Example:**

- Target Hatchet version: `v0.71.0`
- Last migration file: `20250813183355_v1_0_36.sql`
- Migration version: `20250813183355`

## Running Down Migrations

> **Info:** Use a stable release of the `hatchet-migrate` binary (avoid alpha tags) from
>   the [Hatchet releases page](https://github.com/hatchet-dev/hatchet/tags) to
>   ensure down migrations work correctly.

Once you have identified the target migration version, use the `hatchet-migrate` command with the `--down` flag:

```bash
hatchet-migrate --down 20241023223039
```

This will:

1. Connect to your database using the `DATABASE_URL` environment variable
2. Check the current migration version
3. Run all down migrations from the current version to the target version
4. Display progress and confirm when complete

## Deploying the Older Version

After successfully running the down migrations, deploy the older Hatchet version:

### Docker Compose

Update your `docker-compose.yml`:

```yaml
services:
  hatchet-engine:
    image: ghcr.io/hatchet-dev/hatchet/hatchet-engine:v0.71.0
    # ... rest of configuration

  hatchet-dashboard:
    image: ghcr.io/hatchet-dev/hatchet/hatchet-dashboard:v0.71.0
    # ... rest of configuration
```

Then restart:

```bash
docker-compose down
docker-compose up -d
```


---

<!-- Source: https://docs.hatchet.run/self-hosting/benchmarking -->

# Benchmarking Hatchet

This page provides example benchmarks for Hatchet throughput and latency on an 8 CPU database (Amazon RDS, `m7g.2xlarge` instance type). These benchmarks were all run against a v1 Hatchet engine running version `v0.55.26`. For more information on the setup, see the [Setup](#setup) section. Note that on better hardware, there will be significantly better performance: we have tested up to 10k/s on an `m7g.8xlarge` instance.

The best way to benchmark Hatchet is to run your own benchmarks in your own environment. The benchmarks below are provided as a reference point for what you might expect to see in a typical setup. To run your own benchmarks, see the [Running your own benchmarks](#running-your-own-benchmarks) section.

## Throughput

Below are summarized throughput benchmarks run at different incoming event rates. For each run, we note the database CPU utilization and estimated IOPS, which are the most relevant metrics for tracking performance on the database.

| Throughput (runs/s) | Database CPU | Database IOPs |
| ------------------- | ------------ | ------------- |
| 100                 | 15%          | 400           |
| 500                 | 60%          | 600           |
| 2000                | 83%          | 800           |

## Latency

Benchmarks run using event-based triggering: this approximately doubles the queueing time of a workflow. The average latency of events in Hatchet can be approximated by two measurements that Hatchet reports:

- **Average execution time per executed event**: The time from when the event starts execution to when it completes.
- **Average write time per event**: The acknowledgement time for Hatchet to write the event.

Below is a table summarizing these latencies:

| Throughput (runs/s) | Average Execution Time (ms) | Average Write Time (ms) |
| ------------------- | --------------------------- | ----------------------- |
| 100                 | ~40                         | ~2.5                    |
| 500                 | ~48                         | ~2.6                    |
| 2000                | ~220                        | ~5.7                    |

For workloads up to around 100-500 events per second, the latency remains relatively low. As throughput scales toward 2000 events per second, the overall average execution time increases (though the Hatchet engine remained stable throughout the tests).

## Running your own benchmarks

Hatchet publishes a public load testing container which can be used for benchmarking. This container is available at `ghcr.io/hatchet-dev/hatchet/hatchet-loadtest`. It acts as a Hatchet worker and event emitter, so it simply expects a `HATCHET_CLIENT_TOKEN` to be set in the environment.

For example, to run 100 events/second for 60 seconds, you can use the following command:

```bash
docker run -e HATCHET_CLIENT_TOKEN=your-token ghcr.io/hatchet-dev/hatchet/hatchet-loadtest -e "100" -d "60s" --level "warn" --slots "100"
```

The event emitter which is bundled into the container has difficulty emitting more than 2k events/s. As a result, to test higher throughputs, it is recommended to run multiple containers in parallel. Since each container manages its own workflows and worker, it is recommended to use the `HATCHET_CLIENT_NAMESPACE` environment variable to ensure that workflows are not duplicated across containers. For example:

```bash
# first container
docker run -e HATCHET_CLIENT_TOKEN=your-token -e HATCHET_CLIENT_NAMESPACE=loadtest1 ghcr.io/hatchet-dev/hatchet/hatchet-loadtest -e "2000" -d "60s" --level "warn" --slots "100"

# second container
docker run -e HATCHET_CLIENT_TOKEN=your-token -e HATCHET_CLIENT_NAMESPACE=loadtest2 ghcr.io/hatchet-dev/hatchet/hatchet-loadtest -e "2000" -d "60s" --level "warn" --slots "100"
```

### Reference

This container takes the following arguments:

```sh
Usage:
  loadtest [flags]

Flags:
  -c, --concurrency int        concurrency specifies the maximum events to run at the same time
  -D, --delay duration         delay specifies the time to wait in each event to simulate slow tasks
  -d, --duration duration      duration specifies the total time to run the load test (default 10s)
  -F, --eventFanout int        eventFanout specifies the number of events to fanout (default 1)
  -e, --events int             events per second (default 10)
  -f, --failureRate float32    failureRate specifies the rate of failure for the worker
  -h, --help                   help for loadtest
  -l, --level string           logLevel specifies the log level (debug, info, warn, error) (default "info")
  -P, --payloadSize string     payload specifies the size of the payload to send (default "0kb")
  -s, --slots int              slots specifies the number of slots to use in the worker
  -w, --wait duration          wait specifies the total time to wait until events complete (default 10s)
  -p, --workerDelay duration   workerDelay specifies the time to wait before starting the worker
```

### Running a benchmark on Kubernetes

You can use the following Pod manifest to run the load test on Kubernetes (make sure to fill in `HATCHET_CLIENT_TOKEN`):

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: loadtest1a
  namespace: staging
spec:
  restartPolicy: Never
  containers:
    - image: ghcr.io/hatchet-dev/hatchet/hatchet-loadtest:v0.56.0
      imagePullPolicy: Always
      name: loadtest
      command: ["/hatchet/hatchet-load-test"]
      args:
        - loadtest
        - --duration
        - "60s"
        - --events
        - "100"
        - --slots
        - "100"
        - --wait
        - "10s"
        - --level
        - warn
      env:
        - name: HATCHET_CLIENT_TOKEN
          value: "your-token"
        - name: HATCHET_CLIENT_NAMESPACE
          value: "loadtest1a"
      resources:
        limits:
          memory: 1Gi
        requests:
          cpu: 500m
          memory: 1Gi
```

## Setup

All tests were run on a Kubernetes cluster on AWS configured with:

- **Hatchet engine replicas:** 2 (using `c7i.4xlarge` instances to ensure CPU was not a bottleneck)
- **Database:** `m7g.2xlarge` instance type (Amazon RDS)
- **Hatchet version:** `v0.55.26`
- **AWS region:** `us-west-1`

The database configuration was chosen to avoid disk and CPU contention until higher throughputs were reached. We observed that up to around 2000 events/second, the chosen database instance size kept up without major performance degradation. The Hatchet engine was deployed with 2 replicas, and each engine instance had ample CPU headroom on `c7i.4xlarge` nodes.


---

<!-- Source: https://docs.hatchet.run/self-hosting/data-retention -->

# Data Retention

In Hatchet engine version `0.36.0` and above, you can configure the default data retention per tenant for workflow runs and events. The default value is set to 30 days, which means that all workflow runs which were created over 30 days ago and are in a final state (i.e. completed or failed), and all events which were created over 30 days ago, will be deleted.

This can be configured by setting the following environment variable to a Go duration string:

```sh
SERVER_LIMITS_DEFAULT_TENANT_RETENTION_PERIOD=720h # 30 days
```


---

<!-- Source: https://docs.hatchet.run/self-hosting/improving-performance -->

# Tuning Hatchet for Performance

Generally, with a reasonable database instance (4 CPU, 8GB RAM) and small payload sizes, Hatchet can handle hundreds of events and workflow runs per second. However, as throughput increases, you will start to see performance degradation. The most common causes of performance degradation are listed below.

## Database Connection Pooling

The default max connection pool size is 50 per engine instance. If you have a high throughput, you may need to increase this value. This value can be set via the `DATABASE_MAX_CONNS` environment variable on the engine. Note that if you increase this value, you will need to increase the [`max_connections`](https://www.postgresql.org/docs/current/runtime-config-connection.html) value on your Postgres instance as well.

## High Database CPU

Due to the nature of Hatchet workloads, the first bottleneck you will typically see on the database is CPU. If you have access to database query performance metrics, it is worth checking the cause of high CPU. If there is high lock contention on a query, please let the Hatchet team know, as we are looking to reduce lock contention in future releases. Otherwise, if you are seeing high CPU usage without any lock contention, you should increase the number of cores on your database instance.

If you are performing a high number of inserts, particularly in a short period of time, and this correlates with high CPU usage, you can improve performance in several ways by using bulk endpoints or tuning the buffer settings.

### Using bulk endpoints

There are two main ways to initiate workflows, by sending events to Hatchet and by starting workflows directly. In most example workflows, we push a single event or workflow at a time, but it is possible to send multiple events or workflows in one request.

#### Events

 #### Python

```python
hatchet.event.bulk_push(
    events=[
        BulkPushEventWithMetadata(
            key="user:create",
            payload={"userId": str(i), "should_skip": False},
        )
        for i in range(10)
    ]
)
```

#### Typescript

```typescript
const events = [
  {
    payload: { test: 'test1' },
    additionalMetadata: { user_id: 'user1', source: 'test' },
  },
  {
    payload: { test: 'test2' },
    additionalMetadata: { user_id: 'user2', source: 'test' },
  },
  {
    payload: { test: 'test3' },
    additionalMetadata: { user_id: 'user3', source: 'test' },
  },
];

await hatchet.events.bulkPush('user:create', events);
```

#### Go

```go
c, err := client.New(
  client.WithHostPort("127.0.0.1", 7077),
)

if err != nil {
  panic(err)
}

events := []client.EventWithMetadata{
  {
    Event: &events.TestEvent{
      Name: "testing",
    },
    AdditionalMetadata: map[string]string{"hello": "world1"},
    Key: "user:create",
  },
  {
    Event: &events.TestEvent{
      Name: "testing2",
    },
    AdditionalMetadata: map[string]string{"hello": "world2"},
    Key: "user:create",
  },
}

c.Event().BulkPush(
  context.Background(),
  events,
)
```

> **Warning:** There is a maximum limit of 1000 events per request.

#### Workflows

#### Python

```python
@bulk_parent_wf.task(execution_timeout=timedelta(minutes=5))
async def spawn(input: ParentInput, ctx: Context) -> dict[str, list[dict[str, Any]]]:
    # 👀 Create each workflow run to spawn
    child_workflow_runs = [
        bulk_child_wf.create_bulk_run_item(
            input=ChildInput(a=str(i)),
            key=f"child{i}",
            options=TriggerWorkflowOptions(additional_metadata={"hello": "earth"}),
        )
        for i in range(input.n)
    ]

    # 👀 Run workflows in bulk to improve performance
    spawn_results = await bulk_child_wf.aio_run_many(child_workflow_runs)

    return {"results": spawn_results}
```

#### Typescript

```typescript
const parent = hatchet.task({
  name: 'simple',
  fn: async (input: SimpleInput, ctx) => {
    // Bulk run two tasks in parallel
    const child = await ctx.bulkRunChildren([
      {
        workflow: simple,
        input: {
          Message: 'Hello, World!',
        },
      },
      {
        workflow: simple,
        input: {
          Message: 'Hello, Moon!',
        },
      },
    ]);

    return {
      TransformedMessage: `${child[0].TransformedMessage} ${child[1].TransformedMessage}`,
    };
  },
});
```

#### Go

```go
w.RegisterWorkflow(
    &worker.WorkflowJob{
        Name: "parent-workflow",
        On: worker.Event("fanout:create"),
        Description: "Example workflow for spawning child workflows.",
        Steps: []*worker.WorkflowStep{
            worker.Fn(func(ctx worker.HatchetContext) error {
                // Prepare the batch of workflows to spawn
                childWorkflows := make([]*worker.SpawnWorkflowsOpts, 10)

                for i := 0; i < 10; i++ {
                    childInput := "child-input-" + strconv.Itoa(i)
                    childWorkflows[i] = &worker.SpawnWorkflowsOpts{
                        WorkflowName: "child-workflow",
                        Input:        childInput,
                        Key:          "child-key-" + strconv.Itoa(i),
                    }
                }

                // Spawn all workflows in bulk using SpawnWorkflows
                createdWorkflows, err := ctx.SpawnWorkflows(childWorkflows)
                if err != nil {
                    return err
                }

                return nil
            }),
        },
    },
)

```

> **Warning:** There is a maximum limit of 1000 workflows per bulk request.

### Tuning Buffer Settings

Hatchet has configurable write buffers which enable it to reduce the total number of database queries by batching DB writes. This speeds up throughput dramatically at the expense of a slight increase in latency. In general, increasing the buffer size and reducing the buffer flush frequency reduces the CPU load on the DB.

The two most important configurable settings for the buffers are

1. **Flush Period:** The amount of milliseconds to wait between subsequent writes to the database

2. **Max Buffer Size:** The maximum size of the internal buffer writing to the database.

The following environment variables are all configurable:

```sh
# Default values if the values below are not set
SERVER_FLUSH_PERIOD_MILLISECONDS
SERVER_FLUSH_ITEMS_THRESHOLD

# Settings for writing workflow runs to the database
SERVER_WORKFLOWRUNBUFFER_FLUSH_PERIOD_MILLISECONDS
SERVER_WORKFLOWRUNBUFFER_FLUSH_ITEMS_THRESHOLD

# Settings for writing events to the database
SERVER_EVENTBUFFER_FLUSH_PERIOD_MILLISECONDS
SERVER_EVENTBUFFER_FLUSH_ITEMS_THRESHOLD

# Settings for releasing slots for workers
SERVER_RELEASESEMAPHOREBUFFER_FLUSH_PERIOD_MILLISECONDS
SERVER_RELEASESEMAPHOREBUFFER_FLUSH_ITEMS_THRESHOLD

# Settings for writing queue items to the database
SERVER_QUEUESTEPRUNBUFFER_FLUSH_PERIOD_MILLISECONDS
SERVER_QUEUESTEPRUNBUFFER_FLUSH_ITEMS_THRESHOLD
```

A buffer configuration for higher throughput might look like the following:

```sh

# Default values if the values below are not set
SERVER_FLUSH_PERIOD_MILLISECONDS=250
SERVER_FLUSH_ITEMS_THRESHOLD=1000

# Settings for writing workflow runs to the database
SERVER_WORKFLOWRUNBUFFER_FLUSH_PERIOD_MILLISECONDS=100
SERVER_WORKFLOWRUNBUFFER_FLUSH_ITEMS_THRESHOLD=500

# Settings for writing events to the database
SERVER_EVENTBUFFER_FLUSH_PERIOD_MILLISECONDS=1000
SERVER_EVENTBUFFER_FLUSH_ITEMS_THRESHOLD=1000

# Settings for releasing slots for workers
SERVER_RELEASESEMAPHOREBUFFER_FLUSH_PERIOD_MILLISECONDS=100
SERVER_RELEASESEMAPHOREBUFFER_FLUSH_ITEMS_THRESHOLD=200

# Settings for writing queue items to the database
SERVER_QUEUESTEPRUNBUFFER_FLUSH_PERIOD_MILLISECONDS=100
SERVER_QUEUESTEPRUNBUFFER_FLUSH_ITEMS_THRESHOLD=500

```

Benchmarking and tuning on your own infrastructure is recommended to find the optimal values for your workload and use case.

## Slow Time to Start

With higher throughput, you may see a slower time to start for each step run in a workflow. The reason for this is typically that each step run needs to be processed in an internal message queue before getting sent to the worker. You can increase the throughput of this internal queue by setting the following environment variable (default value of `100`):

```
SERVER_MSGQUEUE_RABBITMQ_QOS=200
```

Note that this refers to the number of messages that can be processed in parallel, and each message typically corresponds to at least one database write, so it will not improve performance if this value is significantly higher than the `DATABASE_MAX_CONNS` value. If you are seeing warnings in the engine logs that you are saturating connections, consider decreasing this value.

## Database Settings and Autovacuum

There are several scenarios where Postgres flags may need to be modified to improve performance. By default, every workflow run and step run are stored for 30 days in the Postgres instance. Without tuning autovacuum settings, you may see high table bloat across many tables. If you are storing > 500 GB of workflow run or step run data, we recommend the following autovacuum settings to autovacuum more aggressively:

```
autovacuum_max_workers=10
autovacuum_vacuum_scale_factor=0.1
autovacuum_analyze_scale_factor=0.05
autovacuum_vacuum_threshold=25
autovacuum_analyze_threshold=25
autovacuum_vacuum_cost_delay=10
autovacuum_vacuum_cost_limit=1000
```

If your database has enough memory capacity, you may need to increase the `work_mem` or `maintenance_work_mem` value. For example, on database instances with a large amount of memory available, we typically set the following settings:

```
maintenance_work_mem=2147483647
work_mem=125828
```

Additionally, if there is enough disk capacity, you may see improved performance setting the following flag:

```
max_wal_size=15040
```

## Scaling the Hatchet Engine

By default, the Hatchet engine runs all internal services on a single instance. The internal services on the Hatchet engine are as follows:

- **grpc-api**: the gRPC endpoint for the Hatchet engine. This is the primary endpoint for Hatchet workers. Not to be confused with the Hatchet REST API, which is a separate service that we typically refer to as `api`.
- **controllers**: the internal service that manages the lifecycle of workflow runs, step runs, and events. This service is write-heavy on the database and read-heavy from the message queue.
- **scheduler**: the internal service that schedules step runs to workers. This service is both read-heavy and write-heavy on the database.

It is possible to horizontally scale the Hatchet engine by running multiple instances of the engine. However, if you are seeing a large number of warnings from the scheduler when running the other services in the same engine instance, we recommend running the scheduler on a separate instance. See the [high availability](./high-availability) documentation for more information on how to run the scheduler on a separate instance.


---

<!-- Source: https://docs.hatchet.run/self-hosting/read-replicas -->

# Read Replica Support

For high-throughput production deployments, Hatchet supports database read replicas to distribute database load and improve read performance. This feature allows you to direct read queries to a separate database instance while continuing to send write operations to the primary database. **This can significantly improve performance in read-heavy workloads without requiring application changes.**

You can enable read replica support by setting the following environment variables:

```bash
READ_REPLICA_ENABLED=true
READ_REPLICA_DATABASE_URL='postgresql://hatchet:hatchet@127.0.0.1:5432/hatchet'
READ_REPLICA_MAX_CONNS=200
READ_REPLICA_MIN_CONNS=50
```

## Configuration Options

- `READ_REPLICA_ENABLED`: Set to `true` to enable read replica support
- `READ_REPLICA_DATABASE_URL`: Connection string for the read replica database
- `READ_REPLICA_MAX_CONNS`: Maximum number of connections in the read replica connection pool
- `READ_REPLICA_MIN_CONNS`: Minimum number of connections to maintain in the read replica connection pool

## Limitations

- Replication lag may result in slightly stale or missing data being returned from read operations
- The read replica is only utilized by analytical queries (to load workflow runs, task runs, and metrics in the UI)


---

<!-- Source: https://docs.hatchet.run/self-hosting/sampling -->

# Trace Sampling

For a very high-volume setup, it may be desirable to sample results for the dashboard for the purpose of limiting the amount of data stored in the Hatchet database. **This does not impact the behavior of the Hatchet engine and all tasks will still be processed.** This can be done by setting the following environment variables:

```bash
SERVER_SAMPLING_ENABLED=t
SERVER_SAMPLING_RATE=0.1 # only 10% of results will be sampled
```

Sampling is done at the workflow run level, so all tasks within the same workflow will be sampled, along with all of their events. Sampling has the following limitations:

- Parent tasks which spawn child tasks are not guaranteed to be sampled, even if their children are. This means that the child task may be shown in the dashboard without a corresponding parent task, and vice versa.
- There is no way to configure sampling to ensure that failure events are sampled.
- Only tasks which are sampled can be cancelled or replayed via the REST APIs: do not use this feature if dependent on programmatic cancellations and replays.


---

<!-- Source: https://docs.hatchet.run/self-hosting/smtp-server -->

# SMTP Server

Configure email delivery for tenant invites and Hatchet alerts using any standard SMTP provider (Gmail, SendGrid, AWS SES, etc).

## Prerequisites

- An SMTP provider that supports [PLAIN](https://datatracker.ietf.org/doc/html/rfc4616/) authentication with a username and password.

## Configuration

Set the following environment variables:

```bash
# Enable SMTP
export SERVER_EMAIL_KIND=smtp
export SERVER_EMAIL_SMTP_ENABLED=true

# Connection Settings
export SERVER_EMAIL_SMTP_SERVER_ADDR=smtp.gmail.com:587            # Host and port
export SERVER_EMAIL_SMTP_AUTH_USERNAME=your-email@yourdomain.com   # Username or API Key ID
export SERVER_EMAIL_SMTP_AUTH_PASSWORD=your-password               # Password or API Secret Key

# Sender Identity
export SERVER_EMAIL_SMTP_FROM_EMAIL=noreply@yourdomain.com         # Sender email address
export SERVER_EMAIL_SMTP_SUPPORT_EMAIL=support@yourdomain.com      # Support contact email
export SERVER_EMAIL_SMTP_FROM_NAME="Hatchet"                       # (Optional) Display name
```

## Provider Reference

Common configuration values for major providers:

| Provider                                                                                                                  | Server Address                           | Username     | Password                                                  |
| ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------ | --------------------------------------------------------- |
| **[Gmail](https://support.google.com/mail/answer/185833?hl=en)**                                                          | `smtp.gmail.com:587`                     | Your Email   | [App Password](https://myaccount.google.com/apppasswords) |
| **[SendGrid](https://docs.sendgrid.com/for-developers/sending-email/integrating-with-the-smtp-api)**                      | `smtp.sendgrid.net:587`                  | `apikey`     | Your API Key                                              |
| **[AWS SES](https://docs.aws.amazon.com/ses/latest/dg/send-email-smtp.html)**                                             | `email-smtp.us-east-1.amazonaws.com:587` | IAM Username | IAM Secret                                                |
| **[Outlook](https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-8361e398-8af4-4e97-b147-6c6c4ac95353)** | `smtp.office365.com:587`                 | Your Email   | Your Password                                             |

> **Info:** To request another provider or SMTP authentication protocol, open a feature
>   request on
>   [GitHub](https://github.com/hatchet-dev/hatchet/issues/new?template=feature_request.md).


---

<!-- Source: https://docs.hatchet.run/reference/python/client -->

# Hatchet Python SDK Reference

This is the Python SDK reference, documenting methods available for interacting with Hatchet resources. Check out the [user guide](../../home) for an introduction for getting your first tasks running.

## The Hatchet Python Client

Main client for interacting with the Hatchet SDK.

This class provides access to various client interfaces and utility methods for working with Hatchet workers, workflows, tasks, and our various feature clients.

Methods:

| Name           | Description                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------- |
| `worker`       | Create a Hatchet worker on which to run workflows.                                                            |
| `workflow`     | Define a Hatchet workflow, which can then declare `task`s and be `run`, `schedule`d, and so on.               |
| `task`         | A decorator to transform a function into a standalone Hatchet task that runs as part of a workflow.           |
| `durable_task` | A decorator to transform a function into a standalone Hatchet _durable_ task that runs as part of a workflow. |

### Attributes

#### `cron`

The cron client is a client for managing cron workflows within Hatchet.

#### `event`

The event client, which you can use to push events to Hatchet.

#### `logs`

The logs client is a client for interacting with Hatchet's logs API.

#### `metrics`

The metrics client is a client for reading metrics out of Hatchet's metrics API.

#### `rate_limits`

The rate limits client is a wrapper for Hatchet's gRPC API that makes it easier to work with rate limits in Hatchet.

#### `runs`

The runs client is a client for interacting with task and workflow runs within Hatchet.

#### `scheduled`

The scheduled client is a client for managing scheduled workflows within Hatchet.

#### `workers`

The workers client is a client for managing workers programmatically within Hatchet.

#### `workflows`

The workflows client is a client for managing workflows programmatically within Hatchet.

Note that workflows are the declaration, _not_ the individual runs. If you're looking for runs, use the `RunsClient` instead.

#### `tenant_id`

The tenant id you're operating in.

#### `namespace`

The current namespace you're interacting with.

### Functions

#### `worker`

Create a Hatchet worker on which to run workflows.

Parameters:

| Name            | Type                              | Description                                                                                                                                                | Default    |
| --------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| `name`          | `str`                             | The name of the worker.                                                                                                                                    | _required_ |
| `slots`         | `int \| None`                     | slot count for standard tasks.                                                                                                                             | `None`     |
| `durable_slots` | `int \| None`                     | slot count for durable tasks.                                                                                                                              | `None`     |
| `labels`        | `dict[str, str \| int] \| None`   | A dictionary of labels to assign to the worker. For more details, view examples on affinity and worker labels.                                             | `None`     |
| `workflows`     | `list[BaseWorkflow[Any]] \| None` | A list of workflows to register on the worker, as a shorthand for calling `register_workflow` on each or `register_workflows` on all of them.              | `None`     |
| `lifespan`      | `LifespanFn \| None`              | A lifespan function to run on the worker. This function will be called when the worker is started, and can be used to perform any setup or teardown tasks. | `None`     |

Returns:

| Type     | Description                                                                                                    |
| -------- | -------------------------------------------------------------------------------------------------------------- |
| `Worker` | The created `Worker` object, which exposes an instance method `start` which can be called to start the worker. |

#### `workflow`

Define a Hatchet workflow, which can then declare `task`s and be `run`, `schedule`d, and so on.

Parameters:

| Name                          | Type                                                                  | Description                                                                                                                                                                                                                                                                       | Default          |
| ----------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `name`                        | `str`                                                                 | The name of the workflow.                                                                                                                                                                                                                                                         | _required_       |
| `description`                 | `str \| None`                                                         | A description for the workflow                                                                                                                                                                                                                                                    | `None`           |
| `input_validator`             | `type[TWorkflowInput] \| None`                                        | A Pydantic model to use as a validator for the `input` to the tasks in the workflow. If no validator is provided, defaults to an `EmptyModel` under the hood. The `EmptyModel` is a Pydantic model with no fields specified, and with the `extra` config option set to `"allow"`. | `None`           |
| `on_events`                   | `list[str] \| None`                                                   | A list of event triggers for the workflow - events which cause the workflow to be run.                                                                                                                                                                                            | `None`           |
| `on_crons`                    | `list[str] \| None`                                                   | A list of cron triggers for the workflow.                                                                                                                                                                                                                                         | `None`           |
| `version`                     | `str \| None`                                                         | A version for the workflow                                                                                                                                                                                                                                                        | `None`           |
| `sticky`                      | `StickyStrategy \| None`                                              | A sticky strategy for the workflow                                                                                                                                                                                                                                                | `None`           |
| `default_priority`            | `int`                                                                 | The priority of the workflow. Higher values will cause this workflow to have priority in scheduling over other, lower priority ones.                                                                                                                                              | `1`              |
| `concurrency`                 | `int \| ConcurrencyExpression \| list[ConcurrencyExpression] \| None` | A concurrency object controlling the concurrency settings for this workflow. If an integer is provided, it is treated as a constant concurrency limit with a `GROUP_ROUND_ROBIN` strategy, which means that only `N` runs of the task may execute at any given time.              | `None`           |
| `task_defaults`               | `TaskDefaults`                                                        | A `TaskDefaults` object controlling the default task settings for this workflow.                                                                                                                                                                                                  | `TaskDefaults()` |
| `default_filters`             | `list[DefaultFilter] \| None`                                         | A list of filters to create with the workflow is created. Note that this is a helper to allow you to create filters "declaratively" without needing to make a separate API call once the workflow is created to create them.                                                      | `None`           |
| `default_additional_metadata` | `JSONSerializableMapping \| None`                                     | A dictionary of additional metadata to attach to each run of this workflow by default.                                                                                                                                                                                            | `None`           |

Returns:

| Type                                               | Description                                                                                     |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `Workflow[EmptyModel] \| Workflow[TWorkflowInput]` | The created `Workflow` object, which can be used to declare tasks, run the workflow, and so on. |

#### `task`

A decorator to transform a function into a standalone Hatchet task that runs as part of a workflow.

Parameters:

| Name                          | Type                                                                  | Description                                                                                                                                                                                                                                                      | Default                 |
| ----------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `name`                        | `str \| None`                                                         | The name of the task. If not specified, defaults to the name of the function being wrapped by the `task` decorator.                                                                                                                                              | `None`                  |
| `description`                 | `str \| None`                                                         | An optional description for the task.                                                                                                                                                                                                                            | `None`                  |
| `input_validator`             | `type[TWorkflowInput] \| None`                                        | A Pydantic model to use as a validator for the input to the task. If no validator is provided, defaults to an `EmptyModel`.                                                                                                                                      | `None`                  |
| `on_events`                   | `list[str] \| None`                                                   | A list of event triggers for the task - events which cause the task to be run.                                                                                                                                                                                   | `None`                  |
| `on_crons`                    | `list[str] \| None`                                                   | A list of cron triggers for the task.                                                                                                                                                                                                                            | `None`                  |
| `version`                     | `str \| None`                                                         | A version for the task.                                                                                                                                                                                                                                          | `None`                  |
| `sticky`                      | `StickyStrategy \| None`                                              | A sticky strategy for the task.                                                                                                                                                                                                                                  | `None`                  |
| `default_priority`            | `int`                                                                 | The priority of the task. Higher values will cause this task to have priority in scheduling.                                                                                                                                                                     | `1`                     |
| `concurrency`                 | `int \| ConcurrencyExpression \| list[ConcurrencyExpression] \| None` | A concurrency object controlling the concurrency settings for this task. If an integer is provided, it is treated as a constant concurrency limit with a `GROUP_ROUND_ROBIN` strategy, which means that only `N` runs of the task may execute at any given time. | `None`                  |
| `schedule_timeout`            | `Duration`                                                            | The maximum time allowed for scheduling the task.                                                                                                                                                                                                                | `timedelta(minutes=5)`  |
| `execution_timeout`           | `Duration`                                                            | The maximum time allowed for executing the task.                                                                                                                                                                                                                 | `timedelta(seconds=60)` |
| `retries`                     | `int`                                                                 | The number of times to retry the task before failing.                                                                                                                                                                                                            | `0`                     |
| `rate_limits`                 | `list[RateLimit] \| None`                                             | A list of rate limit configurations for the task.                                                                                                                                                                                                                | `None`                  |
| `desired_worker_labels`       | `dict[str, DesiredWorkerLabel] \| None`                               | A dictionary of desired worker labels that determine to which worker the task should be assigned.                                                                                                                                                                | `None`                  |
| `backoff_factor`              | `float \| None`                                                       | The backoff factor for controlling exponential backoff in retries.                                                                                                                                                                                               | `None`                  |
| `backoff_max_seconds`         | `int \| None`                                                         | The maximum number of seconds to allow retries with exponential backoff to continue.                                                                                                                                                                             | `None`                  |
| `default_filters`             | `list[DefaultFilter] \| None`                                         | A list of filters to create with the task is created. Note that this is a helper to allow you to create filters "declaratively" without needing to make a separate API call once the task is created to create them.                                             | `None`                  |
| `default_additional_metadata` | `JSONSerializableMapping \| None`                                     | A dictionary of additional metadata to attach to each run of this task by default.                                                                                                                                                                               | `None`                  |

Returns:

| Type                                                                                                                                                                                                                                 | Description                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| `Callable[[Callable[Concatenate[EmptyModel, Context, P], R \| CoroutineLike[R]]], Standalone[EmptyModel, R]] \| Callable[[Callable[Concatenate[TWorkflowInput, Context, P], R \| CoroutineLike[R]]], Standalone[TWorkflowInput, R]]` | A decorator which creates a `Standalone` task object. |

#### `durable_task`

A decorator to transform a function into a standalone Hatchet _durable_ task that runs as part of a workflow.

Parameters:

| Name                          | Type                                                                  | Description                                                                                                                                                                                                                                                      | Default                 |
| ----------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `name`                        | `str \| None`                                                         | The name of the task. If not specified, defaults to the name of the function being wrapped by the `task` decorator.                                                                                                                                              | `None`                  |
| `description`                 | `str \| None`                                                         | An optional description for the task.                                                                                                                                                                                                                            | `None`                  |
| `input_validator`             | `type[TWorkflowInput] \| None`                                        | A Pydantic model to use as a validator for the input to the task. If no validator is provided, defaults to an `EmptyModel`.                                                                                                                                      | `None`                  |
| `on_events`                   | `list[str] \| None`                                                   | A list of event triggers for the task - events which cause the task to be run.                                                                                                                                                                                   | `None`                  |
| `on_crons`                    | `list[str] \| None`                                                   | A list of cron triggers for the task.                                                                                                                                                                                                                            | `None`                  |
| `version`                     | `str \| None`                                                         | A version for the task.                                                                                                                                                                                                                                          | `None`                  |
| `sticky`                      | `StickyStrategy \| None`                                              | A sticky strategy for the task.                                                                                                                                                                                                                                  | `None`                  |
| `default_priority`            | `int`                                                                 | The priority of the task. Higher values will cause this task to have priority in scheduling.                                                                                                                                                                     | `1`                     |
| `concurrency`                 | `int \| ConcurrencyExpression \| list[ConcurrencyExpression] \| None` | A concurrency object controlling the concurrency settings for this task. If an integer is provided, it is treated as a constant concurrency limit with a `GROUP_ROUND_ROBIN` strategy, which means that only `N` runs of the task may execute at any given time. | `None`                  |
| `schedule_timeout`            | `Duration`                                                            | The maximum time allowed for scheduling the task.                                                                                                                                                                                                                | `timedelta(minutes=5)`  |
| `execution_timeout`           | `Duration`                                                            | The maximum time allowed for executing the task.                                                                                                                                                                                                                 | `timedelta(seconds=60)` |
| `retries`                     | `int`                                                                 | The number of times to retry the task before failing.                                                                                                                                                                                                            | `0`                     |
| `rate_limits`                 | `list[RateLimit] \| None`                                             | A list of rate limit configurations for the task.                                                                                                                                                                                                                | `None`                  |
| `desired_worker_labels`       | `dict[str, DesiredWorkerLabel] \| None`                               | A dictionary of desired worker labels that determine to which worker the task should be assigned.                                                                                                                                                                | `None`                  |
| `backoff_factor`              | `float \| None`                                                       | The backoff factor for controlling exponential backoff in retries.                                                                                                                                                                                               | `None`                  |
| `backoff_max_seconds`         | `int \| None`                                                         | The maximum number of seconds to allow retries with exponential backoff to continue.                                                                                                                                                                             | `None`                  |
| `default_filters`             | `list[DefaultFilter] \| None`                                         | A list of filters to create with the task is created. Note that this is a helper to allow you to create filters "declaratively" without needing to make a separate API call once the task is created to create them.                                             | `None`                  |
| `default_additional_metadata` | `JSONSerializableMapping \| None`                                     | A dictionary of additional metadata to attach to each run of this task by default.                                                                                                                                                                               | `None`                  |

Returns:

| Type                                                                                                                                                                                                                                               | Description                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `Callable[[Callable[Concatenate[EmptyModel, DurableContext, P], R \| CoroutineLike[R]]], Standalone[EmptyModel, R]] \| Callable[[Callable[Concatenate[TWorkflowInput, DurableContext, P], R \| CoroutineLike[R]]], Standalone[TWorkflowInput, R]]` | A decorator which creates a `Standalone` task object. |


---

<!-- Source: https://docs.hatchet.run/reference/python/context -->

# Context

The Hatchet Context class provides helper methods and useful data to tasks at runtime. It is passed as the second argument to all tasks and durable tasks.

There are two types of context classes you'll encounter:

- `Context` - The standard context for regular tasks with methods for logging, task output retrieval, cancellation, and more
- `DurableContext` - An extended context for durable tasks that includes additional methods for durable execution like `aio_wait_for` and `aio_sleep_for`

## Context

Methods:

| Name                   | Description                                                                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `was_skipped`          | Check if a given task was skipped. You can read about skipping in [the docs](/v1/conditions#checking-if-a-task-was-skipped).                                             |
| `task_output`          | Get the output of a parent task in a DAG.                                                                                                                                |
| `cancel`               | Cancel the current task run. This will call the Hatchet API to cancel the step run and set the exit flag to True.                                                        |
| `aio_cancel`           | Cancel the current task run. This will call the Hatchet API to cancel the step run and set the exit flag to True.                                                        |
| `done`                 | Check if the current task run has been cancelled.                                                                                                                        |
| `log`                  | Log a line to the Hatchet API. This will send the log line to the Hatchet API and return immediately.                                                                    |
| `release_slot`         | Manually release the slot for the current step run to free up a slot on the worker. Note that this is an advanced feature and should be used with caution.               |
| `put_stream`           | Put a stream event to the Hatchet API. This will send the data to the Hatchet API and return immediately. You can then subscribe to the stream from a separate consumer. |
| `refresh_timeout`      | Refresh the timeout for the current task run. You can read about refreshing timeouts in [the docs](../../home/timeouts#refreshing-timeouts).                             |
| `fetch_task_run_error` | **DEPRECATED**: Use `get_task_run_error` instead.                                                                                                                        |

### Attributes

#### `was_triggered_by_event`

A property that indicates whether the workflow was triggered by an event.

Returns:

| Type   | Description                                                      |
| ------ | ---------------------------------------------------------------- |
| `bool` | True if the workflow was triggered by an event, False otherwise. |

#### `workflow_input`

The input to the workflow, as a dictionary. It's recommended to use the `input` parameter to the task (the first argument passed into the task at runtime) instead of this property.

Returns:

| Type                      | Description                |
| ------------------------- | -------------------------- |
| `JSONSerializableMapping` | The input to the workflow. |

#### `lifespan`

The worker lifespan, if it exists. You can read about lifespans in [the docs](../../home/lifespans).

**Note: You'll need to cast the return type of this property to the type returned by your lifespan generator.**

#### `workflow_run_id`

The id of the current workflow run.

Returns:

| Type  | Description                         |
| ----- | ----------------------------------- |
| `str` | The id of the current workflow run. |

#### `retry_count`

The retry count of the current task run, which corresponds to the number of times the task has been retried.

Returns:

| Type  | Description                              |
| ----- | ---------------------------------------- |
| `int` | The retry count of the current task run. |

#### `attempt_number`

The attempt number of the current task run, which corresponds to the number of times the task has been attempted, including the initial attempt. This is one more than the retry count.

Returns:

| Type  | Description                                 |
| ----- | ------------------------------------------- |
| `int` | The attempt number of the current task run. |

#### `additional_metadata`

The additional metadata sent with the current task run.

Returns:

| Type                      | Description                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------------------- |
| `JSONSerializableMapping` | The additional metadata sent with the current task run, or None if no additional metadata was sent. |

#### `parent_workflow_run_id`

The parent workflow run id of the current task run, if it exists. This is useful for knowing which workflow run spawned this run as a child.

Returns:

| Type          | Description                                                                       |
| ------------- | --------------------------------------------------------------------------------- |
| `str \| None` | The parent workflow run id of the current task run, or None if it does not exist. |

#### `priority`

The priority that the current task was run with.

Returns:

| Type          | Description                                                           |
| ------------- | --------------------------------------------------------------------- |
| `int \| None` | The priority of the current task run, or None if no priority was set. |

#### `workflow_id`

The id of the workflow that this task belongs to.

Returns:

| Type          | Description                                       |
| ------------- | ------------------------------------------------- |
| `str \| None` | The id of the workflow that this task belongs to. |

#### `workflow_version_id`

The id of the workflow version that this task belongs to.

Returns:

| Type          | Description                                               |
| ------------- | --------------------------------------------------------- |
| `str \| None` | The id of the workflow version that this task belongs to. |

#### `task_run_errors`

A helper intended to be used in an on-failure step to retrieve the errors that occurred in upstream task runs.

Returns:

| Type             | Description                                              |
| ---------------- | -------------------------------------------------------- |
| `dict[str, str]` | A dictionary mapping task names to their error messages. |

### Functions

#### `was_skipped`

Check if a given task was skipped. You can read about skipping in [the docs](/v1/conditions#checking-if-a-task-was-skipped).

Parameters:

| Name   | Type                      | Description                                       | Default    |
| ------ | ------------------------- | ------------------------------------------------- | ---------- |
| `task` | `Task[TWorkflowInput, R]` | The task to check the status of (skipped or not). | _required_ |

Returns:

| Type   | Description                                    |
| ------ | ---------------------------------------------- |
| `bool` | True if the task was skipped, False otherwise. |

#### `task_output`

Get the output of a parent task in a DAG.

Parameters:

| Name   | Type                      | Description                                 | Default    |
| ------ | ------------------------- | ------------------------------------------- | ---------- |
| `task` | `Task[TWorkflowInput, R]` | The task whose output you want to retrieve. | _required_ |

Returns:

| Type | Description                                                             |
| ---- | ----------------------------------------------------------------------- |
| `R`  | The output of the parent task, validated against the task's validators. |

Raises:

| Type         | Description                                                              |
| ------------ | ------------------------------------------------------------------------ |
| `ValueError` | If the task was skipped or if the step output for the task is not found. |

#### `cancel`

Cancel the current task run. This will call the Hatchet API to cancel the step run and set the exit flag to True.

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `aio_cancel`

Cancel the current task run. This will call the Hatchet API to cancel the step run and set the exit flag to True.

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `done`

Check if the current task run has been cancelled.

Returns:

| Type   | Description                                               |
| ------ | --------------------------------------------------------- |
| `bool` | True if the task run has been cancelled, False otherwise. |

#### `log`

Log a line to the Hatchet API. This will send the log line to the Hatchet API and return immediately.

Parameters:

| Name             | Type                             | Description                                                           | Default    |
| ---------------- | -------------------------------- | --------------------------------------------------------------------- | ---------- |
| `line`           | `str \| JSONSerializableMapping` | The line to log. Can be a string or a JSON serializable mapping.      | _required_ |
| `raise_on_error` | `bool`                           | If True, will raise an exception if the log fails. Defaults to False. | `False`    |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `release_slot`

Manually release the slot for the current step run to free up a slot on the worker. Note that this is an advanced feature and should be used with caution.

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `put_stream`

Put a stream event to the Hatchet API. This will send the data to the Hatchet API and return immediately. You can then subscribe to the stream from a separate consumer.

Parameters:

| Name   | Type           | Description                                                    | Default    |
| ------ | -------------- | -------------------------------------------------------------- | ---------- |
| `data` | `str \| bytes` | The data to send to the Hatchet API. Can be a string or bytes. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `refresh_timeout`

Refresh the timeout for the current task run. You can read about refreshing timeouts in [the docs](../../home/timeouts#refreshing-timeouts).

Parameters:

| Name           | Type               | Description                                                                                        | Default    |
| -------------- | ------------------ | -------------------------------------------------------------------------------------------------- | ---------- |
| `increment_by` | `str \| timedelta` | The amount of time to increment the timeout by. Can be a string (e.g. "5m") or a timedelta object. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `fetch_task_run_error`

**DEPRECATED**: Use `get_task_run_error` instead.

A helper intended to be used in an on-failure step to retrieve the error that occurred in a specific upstream task run.

Parameters:

| Name   | Type                      | Description                                | Default    |
| ------ | ------------------------- | ------------------------------------------ | ---------- |
| `task` | `Task[TWorkflowInput, R]` | The task whose error you want to retrieve. | _required_ |

Returns:

| Type          | Description                                                      |
| ------------- | ---------------------------------------------------------------- |
| `str \| None` | The error message of the task run, or None if no error occurred. |

## DurableContext

Bases: `Context`

Methods:

| Name            | Description                                                                                                                |
| --------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `aio_wait_for`  | Durably wait for either a sleep or an event.                                                                               |
| `aio_sleep_for` | Lightweight wrapper for durable sleep. Allows for shorthand usage of `ctx.aio_wait_for` when specifying a sleep condition. |

### Functions

#### `aio_wait_for`

Durably wait for either a sleep or an event.

Parameters:

| Name          | Type                                              | Description                                                                                  | Default    |
| ------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------- | ---------- |
| `signal_key`  | `str`                                             | The key to use for the durable event. This is used to identify the event in the Hatchet API. | _required_ |
| `*conditions` | `SleepCondition \| UserEventCondition \| OrGroup` | The conditions to wait for. Can be a SleepCondition or UserEventCondition.                   | `()`       |

Returns:

| Type             | Description                                      |
| ---------------- | ------------------------------------------------ |
| `dict[str, Any]` | A dictionary containing the results of the wait. |

Raises:

| Type         | Description                                     |
| ------------ | ----------------------------------------------- |
| `ValueError` | If the durable event listener is not available. |

#### `aio_sleep_for`

Lightweight wrapper for durable sleep. Allows for shorthand usage of `ctx.aio_wait_for` when specifying a sleep condition.

For more complicated conditions, use `ctx.aio_wait_for` directly.


---

<!-- Source: https://docs.hatchet.run/reference/python/feature-clients/cron -->

# Cron Client

Bases: `BaseRestClient`

The cron client is a client for managing cron workflows within Hatchet.

Methods:

| Name         | Description                                                          |
| ------------ | -------------------------------------------------------------------- |
| `aio_create` | Create a new workflow cron trigger.                                  |
| `aio_delete` | Delete a workflow cron trigger.                                      |
| `aio_get`    | Retrieve a specific workflow cron trigger by ID.                     |
| `aio_list`   | Retrieve a list of all workflow cron triggers matching the criteria. |
| `create`     | Create a new workflow cron trigger.                                  |
| `delete`     | Delete a workflow cron trigger.                                      |
| `get`        | Retrieve a specific workflow cron trigger by ID.                     |
| `list`       | Retrieve a list of all workflow cron triggers matching the criteria. |

### Functions

#### `aio_create`

Create a new workflow cron trigger.

Parameters:

| Name                  | Type                      | Description                                           | Default    |
| --------------------- | ------------------------- | ----------------------------------------------------- | ---------- |
| `workflow_name`       | `str`                     | The name of the workflow to trigger.                  | _required_ |
| `cron_name`           | `str`                     | The name of the cron trigger.                         | _required_ |
| `expression`          | `str`                     | The cron expression defining the schedule.            | _required_ |
| `input`               | `JSONSerializableMapping` | The input data for the cron workflow.                 | _required_ |
| `additional_metadata` | `JSONSerializableMapping` | Additional metadata associated with the cron trigger. | _required_ |
| `priority`            | `int \| None`             | The priority of the cron workflow trigger.            | `None`     |

Returns:

| Type            | Description                         |
| --------------- | ----------------------------------- |
| `CronWorkflows` | The created cron workflow instance. |

#### `aio_delete`

Delete a workflow cron trigger.

Parameters:

| Name      | Type  | Description                           | Default    |
| --------- | ----- | ------------------------------------- | ---------- |
| `cron_id` | `str` | The ID of the cron trigger to delete. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `aio_get`

Retrieve a specific workflow cron trigger by ID.

Parameters:

| Name      | Type  | Description                                                | Default    |
| --------- | ----- | ---------------------------------------------------------- | ---------- |
| `cron_id` | `str` | The cron trigger ID or CronWorkflows instance to retrieve. | _required_ |

Returns:

| Type            | Description                           |
| --------------- | ------------------------------------- |
| `CronWorkflows` | The requested cron workflow instance. |

#### `aio_list`

Retrieve a list of all workflow cron triggers matching the criteria.

Parameters:

| Name                  | Type                                  | Description                                | Default |
| --------------------- | ------------------------------------- | ------------------------------------------ | ------- |
| `offset`              | `int \| None`                         | The offset to start the list from.         | `None`  |
| `limit`               | `int \| None`                         | The maximum number of items to return.     | `None`  |
| `workflow_id`         | `str \| None`                         | The ID of the workflow to filter by.       | `None`  |
| `additional_metadata` | `JSONSerializableMapping \| None`     | Filter by additional metadata keys.        | `None`  |
| `order_by_field`      | `CronWorkflowsOrderByField \| None`   | The field to order the list by.            | `None`  |
| `order_by_direction`  | `WorkflowRunOrderByDirection \| None` | The direction to order the list by.        | `None`  |
| `workflow_name`       | `str \| None`                         | The name of the workflow to filter by.     | `None`  |
| `cron_name`           | `str \| None`                         | The name of the cron trigger to filter by. | `None`  |

Returns:

| Type                | Description               |
| ------------------- | ------------------------- |
| `CronWorkflowsList` | A list of cron workflows. |

#### `create`

Create a new workflow cron trigger.

Parameters:

| Name                  | Type                      | Description                                           | Default    |
| --------------------- | ------------------------- | ----------------------------------------------------- | ---------- |
| `workflow_name`       | `str`                     | The name of the workflow to trigger.                  | _required_ |
| `cron_name`           | `str`                     | The name of the cron trigger.                         | _required_ |
| `expression`          | `str`                     | The cron expression defining the schedule.            | _required_ |
| `input`               | `JSONSerializableMapping` | The input data for the cron workflow.                 | _required_ |
| `additional_metadata` | `JSONSerializableMapping` | Additional metadata associated with the cron trigger. | _required_ |
| `priority`            | `int \| None`             | The priority of the cron workflow trigger.            | `None`     |

Returns:

| Type            | Description                         |
| --------------- | ----------------------------------- |
| `CronWorkflows` | The created cron workflow instance. |

#### `delete`

Delete a workflow cron trigger.

Parameters:

| Name      | Type  | Description                           | Default    |
| --------- | ----- | ------------------------------------- | ---------- |
| `cron_id` | `str` | The ID of the cron trigger to delete. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `get`

Retrieve a specific workflow cron trigger by ID.

Parameters:

| Name      | Type  | Description                                                | Default    |
| --------- | ----- | ---------------------------------------------------------- | ---------- |
| `cron_id` | `str` | The cron trigger ID or CronWorkflows instance to retrieve. | _required_ |

Returns:

| Type            | Description                           |
| --------------- | ------------------------------------- |
| `CronWorkflows` | The requested cron workflow instance. |

#### `list`

Retrieve a list of all workflow cron triggers matching the criteria.

Parameters:

| Name                  | Type                                  | Description                                | Default |
| --------------------- | ------------------------------------- | ------------------------------------------ | ------- |
| `offset`              | `int \| None`                         | The offset to start the list from.         | `None`  |
| `limit`               | `int \| None`                         | The maximum number of items to return.     | `None`  |
| `workflow_id`         | `str \| None`                         | The ID of the workflow to filter by.       | `None`  |
| `additional_metadata` | `JSONSerializableMapping \| None`     | Filter by additional metadata keys.        | `None`  |
| `order_by_field`      | `CronWorkflowsOrderByField \| None`   | The field to order the list by.            | `None`  |
| `order_by_direction`  | `WorkflowRunOrderByDirection \| None` | The direction to order the list by.        | `None`  |
| `workflow_name`       | `str \| None`                         | The name of the workflow to filter by.     | `None`  |
| `cron_name`           | `str \| None`                         | The name of the cron trigger to filter by. | `None`  |

Returns:

| Type                | Description               |
| ------------------- | ------------------------- |
| `CronWorkflowsList` | A list of cron workflows. |


---

<!-- Source: https://docs.hatchet.run/reference/python/feature-clients/filters -->

# Filters Client

Bases: `BaseRestClient`

The filters client is a client for interacting with Hatchet's filters API.

Methods:

| Name         | Description                      |
| ------------ | -------------------------------- |
| `aio_create` | Create a new filter.             |
| `aio_delete` | Delete a filter by its ID.       |
| `aio_get`    | Get a filter by its ID.          |
| `aio_list`   | List filters for a given tenant. |
| `aio_update` | Update a filter by its ID.       |
| `create`     | Create a new filter.             |
| `delete`     | Delete a filter by its ID.       |
| `get`        | Get a filter by its ID.          |
| `list`       | List filters for a given tenant. |
| `update`     | Update a filter by its ID.       |

### Functions

#### `aio_create`

Create a new filter.

Parameters:

| Name          | Type                              | Description                                          | Default    |
| ------------- | --------------------------------- | ---------------------------------------------------- | ---------- |
| `workflow_id` | `str`                             | The ID of the workflow to associate with the filter. | _required_ |
| `expression`  | `str`                             | The expression to evaluate for the filter.           | _required_ |
| `scope`       | `str`                             | The scope for the filter.                            | _required_ |
| `payload`     | `JSONSerializableMapping \| None` | The payload to send with the filter.                 | `None`     |

Returns:

| Type       | Description         |
| ---------- | ------------------- |
| `V1Filter` | The created filter. |

#### `aio_delete`

Delete a filter by its ID.

Parameters:

| Name        | Type  | Description                     | Default    |
| ----------- | ----- | ------------------------------- | ---------- |
| `filter_id` | `str` | The ID of the filter to delete. | _required_ |

Returns:

| Type       | Description         |
| ---------- | ------------------- |
| `V1Filter` | The deleted filter. |

#### `aio_get`

Get a filter by its ID.

Parameters:

| Name        | Type  | Description                       | Default    |
| ----------- | ----- | --------------------------------- | ---------- |
| `filter_id` | `str` | The ID of the filter to retrieve. | _required_ |

Returns:

| Type       | Description                       |
| ---------- | --------------------------------- |
| `V1Filter` | The filter with the specified ID. |

#### `aio_list`

List filters for a given tenant.

Parameters:

| Name           | Type                | Description                                                              | Default |
| -------------- | ------------------- | ------------------------------------------------------------------------ | ------- |
| `limit`        | `int \| None`       | The maximum number of filters to return.                                 | `None`  |
| `offset`       | `int \| None`       | The number of filters to skip before starting to collect the result set. | `None`  |
| `workflow_ids` | `list[str] \| None` | A list of workflow IDs to filter by.                                     | `None`  |
| `scopes`       | `list[str] \| None` | A list of scopes to filter by.                                           | `None`  |

Returns:

| Type           | Description                                        |
| -------------- | -------------------------------------------------- |
| `V1FilterList` | A list of filters matching the specified criteria. |

#### `aio_update`

Update a filter by its ID.

Parameters:

| Name        | Type                    | Description                         | Default    |
| ----------- | ----------------------- | ----------------------------------- | ---------- |
| `filter_id` | `str`                   | The ID of the filter to update.     | _required_ |
| `updates`   | `V1UpdateFilterRequest` | The updates to apply to the filter. | _required_ |

Returns:

| Type       | Description         |
| ---------- | ------------------- |
| `V1Filter` | The updated filter. |

#### `create`

Create a new filter.

Parameters:

| Name          | Type                              | Description                                          | Default    |
| ------------- | --------------------------------- | ---------------------------------------------------- | ---------- |
| `workflow_id` | `str`                             | The ID of the workflow to associate with the filter. | _required_ |
| `expression`  | `str`                             | The expression to evaluate for the filter.           | _required_ |
| `scope`       | `str`                             | The scope for the filter.                            | _required_ |
| `payload`     | `JSONSerializableMapping \| None` | The payload to send with the filter.                 | `None`     |

Returns:

| Type       | Description         |
| ---------- | ------------------- |
| `V1Filter` | The created filter. |

#### `delete`

Delete a filter by its ID.

Parameters:

| Name        | Type  | Description                     | Default    |
| ----------- | ----- | ------------------------------- | ---------- |
| `filter_id` | `str` | The ID of the filter to delete. | _required_ |

Returns:

| Type       | Description         |
| ---------- | ------------------- |
| `V1Filter` | The deleted filter. |

#### `get`

Get a filter by its ID.

Parameters:

| Name        | Type  | Description                       | Default    |
| ----------- | ----- | --------------------------------- | ---------- |
| `filter_id` | `str` | The ID of the filter to retrieve. | _required_ |

Returns:

| Type       | Description                       |
| ---------- | --------------------------------- |
| `V1Filter` | The filter with the specified ID. |

#### `list`

List filters for a given tenant.

Parameters:

| Name           | Type                | Description                                                              | Default |
| -------------- | ------------------- | ------------------------------------------------------------------------ | ------- |
| `limit`        | `int \| None`       | The maximum number of filters to return.                                 | `None`  |
| `offset`       | `int \| None`       | The number of filters to skip before starting to collect the result set. | `None`  |
| `workflow_ids` | `list[str] \| None` | A list of workflow IDs to filter by.                                     | `None`  |
| `scopes`       | `list[str] \| None` | A list of scopes to filter by.                                           | `None`  |

Returns:

| Type           | Description                                        |
| -------------- | -------------------------------------------------- |
| `V1FilterList` | A list of filters matching the specified criteria. |

#### `update`

Update a filter by its ID.

Parameters:

| Name        | Type                    | Description                         | Default    |
| ----------- | ----------------------- | ----------------------------------- | ---------- |
| `filter_id` | `str`                   | The ID of the filter to update.     | _required_ |
| `updates`   | `V1UpdateFilterRequest` | The updates to apply to the filter. | _required_ |

Returns:

| Type       | Description         |
| ---------- | ------------------- |
| `V1Filter` | The updated filter. |


---

<!-- Source: https://docs.hatchet.run/reference/python/feature-clients/logs -->

# Logs Client

Bases: `BaseRestClient`

The logs client is a client for interacting with Hatchet's logs API.

Methods:

| Name       | Description                          |
| ---------- | ------------------------------------ |
| `aio_list` | List log lines for a given task run. |
| `list`     | List log lines for a given task run. |

### Functions

#### `aio_list`

List log lines for a given task run.

Parameters:

| Name          | Type               | Description                                            | Default    |
| ------------- | ------------------ | ------------------------------------------------------ | ---------- |
| `task_run_id` | `str`              | The ID of the task run to list logs for.               | _required_ |
| `limit`       | `int`              | Maximum number of log lines to return (default: 1000). | `1000`     |
| `since`       | `datetime \| None` | The start time to get logs for.                        | `None`     |
| `until`       | `datetime \| None` | The end time to get logs for.                          | `None`     |

Returns:

| Type            | Description                                     |
| --------------- | ----------------------------------------------- |
| `V1LogLineList` | A list of log lines for the specified task run. |

#### `list`

List log lines for a given task run.

Parameters:

| Name          | Type               | Description                                            | Default    |
| ------------- | ------------------ | ------------------------------------------------------ | ---------- |
| `task_run_id` | `str`              | The ID of the task run to list logs for.               | _required_ |
| `limit`       | `int`              | Maximum number of log lines to return (default: 1000). | `1000`     |
| `since`       | `datetime \| None` | The start time to get logs for.                        | `None`     |
| `until`       | `datetime \| None` | The end time to get logs for.                          | `None`     |

Returns:

| Type            | Description                                     |
| --------------- | ----------------------------------------------- |
| `V1LogLineList` | A list of log lines for the specified task run. |


---

<!-- Source: https://docs.hatchet.run/reference/python/feature-clients/metrics -->

# Metrics Client

Bases: `BaseRestClient`

The metrics client is a client for reading metrics out of Hatchet's metrics API.

Methods:

| Name                                   | Description                                                                               |
| -------------------------------------- | ----------------------------------------------------------------------------------------- |
| `aio_get_queue_metrics`                | Retrieve the current queue metrics for the tenant.                                        |
| `aio_get_task_metrics`                 | Retrieve task metrics, grouped by status (queued, running, completed, failed, cancelled). |
| `aio_get_task_stats`                   | Get task statistics for the tenant.                                                       |
| `aio_scrape_tenant_prometheus_metrics` | Scrape Prometheus metrics for the tenant. Returns the metrics in Prometheus text format.  |
| `get_queue_metrics`                    | Retrieve the current queue metrics for the tenant.                                        |
| `get_task_metrics`                     | Retrieve task metrics, grouped by status (queued, running, completed, failed, cancelled). |
| `get_task_stats`                       | Get task statistics for the tenant.                                                       |
| `scrape_tenant_prometheus_metrics`     | Scrape Prometheus metrics for the tenant. Returns the metrics in Prometheus text format.  |

### Functions

#### `aio_get_queue_metrics`

Retrieve the current queue metrics for the tenant.

Returns:

| Type             | Description               |
| ---------------- | ------------------------- |
| `dict[str, Any]` | The current queue metrics |

#### `aio_get_task_metrics`

Retrieve task metrics, grouped by status (queued, running, completed, failed, cancelled).

Parameters:

| Name                           | Type                | Description                                                                                                          | Default |
| ------------------------------ | ------------------- | -------------------------------------------------------------------------------------------------------------------- | ------- |
| `since`                        | `datetime \| None`  | Start time for the metrics query (defaults to the past day if unset)                                                 | `None`  |
| `until`                        | `datetime \| None`  | End time for the metrics query                                                                                       | `None`  |
| `workflow_ids`                 | `list[str] \| None` | List of workflow IDs to filter the metrics by                                                                        | `None`  |
| `parent_task_external_id`      | `str \| None`       | ID of the parent task to filter by (note that parent task here refers to the task that spawned this task as a child) | `None`  |
| `triggering_event_external_id` | `str \| None`       | ID of the triggering event to filter by                                                                              | `None`  |

Returns:

| Type          | Description  |
| ------------- | ------------ |
| `TaskMetrics` | Task metrics |

#### `aio_get_task_stats`

Get task statistics for the tenant.

Returns:

| Type                  | Description                                          |
| --------------------- | ---------------------------------------------------- |
| `dict[str, TaskStat]` | A dictionary mapping task names to their statistics. |

#### `aio_scrape_tenant_prometheus_metrics`

Scrape Prometheus metrics for the tenant. Returns the metrics in Prometheus text format.

Returns:

| Type  | Description                                     |
| ----- | ----------------------------------------------- |
| `str` | The metrics, returned in Prometheus text format |

#### `get_queue_metrics`

Retrieve the current queue metrics for the tenant.

Returns:

| Type             | Description               |
| ---------------- | ------------------------- |
| `dict[str, Any]` | The current queue metrics |

#### `get_task_metrics`

Retrieve task metrics, grouped by status (queued, running, completed, failed, cancelled).

Parameters:

| Name                           | Type                | Description                                                                                                          | Default |
| ------------------------------ | ------------------- | -------------------------------------------------------------------------------------------------------------------- | ------- |
| `since`                        | `datetime \| None`  | Start time for the metrics query (defaults to the past day if unset)                                                 | `None`  |
| `until`                        | `datetime \| None`  | End time for the metrics query                                                                                       | `None`  |
| `workflow_ids`                 | `list[str] \| None` | List of workflow IDs to filter the metrics by                                                                        | `None`  |
| `parent_task_external_id`      | `str \| None`       | ID of the parent task to filter by (note that parent task here refers to the task that spawned this task as a child) | `None`  |
| `triggering_event_external_id` | `str \| None`       | ID of the triggering event to filter by                                                                              | `None`  |

Returns:

| Type          | Description  |
| ------------- | ------------ |
| `TaskMetrics` | Task metrics |

#### `get_task_stats`

Get task statistics for the tenant.

Returns:

| Type                  | Description                                          |
| --------------------- | ---------------------------------------------------- |
| `dict[str, TaskStat]` | A dictionary mapping task names to their statistics. |

#### `scrape_tenant_prometheus_metrics`

Scrape Prometheus metrics for the tenant. Returns the metrics in Prometheus text format.

Returns:

| Type  | Description                                     |
| ----- | ----------------------------------------------- |
| `str` | The metrics, returned in Prometheus text format |


---

<!-- Source: https://docs.hatchet.run/reference/python/feature-clients/rate_limits -->

# Rate Limits Client

Bases: `BaseRestClient`

The rate limits client is a wrapper for Hatchet's gRPC API that makes it easier to work with rate limits in Hatchet.

Methods:

| Name      | Description                       |
| --------- | --------------------------------- |
| `aio_put` | Put a rate limit for a given key. |
| `put`     | Put a rate limit for a given key. |

### Functions

#### `aio_put`

Put a rate limit for a given key.

Parameters:

| Name       | Type                | Description                        | Default    |
| ---------- | ------------------- | ---------------------------------- | ---------- |
| `key`      | `str`               | The key to set the rate limit for. | _required_ |
| `limit`    | `int`               | The rate limit to set.             | _required_ |
| `duration` | `RateLimitDuration` | The duration of the rate limit.    | `SECOND`   |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `put`

Put a rate limit for a given key.

Parameters:

| Name       | Type                | Description                        | Default    |
| ---------- | ------------------- | ---------------------------------- | ---------- |
| `key`      | `str`               | The key to set the rate limit for. | _required_ |
| `limit`    | `int`               | The rate limit to set.             | _required_ |
| `duration` | `RateLimitDuration` | The duration of the rate limit.    | `SECOND`   |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |


---

<!-- Source: https://docs.hatchet.run/reference/python/feature-clients/runs -->

# Runs Client

Bases: `BaseRestClient`

The runs client is a client for interacting with task and workflow runs within Hatchet.

Methods:

| Name                                         | Description                                                          |
| -------------------------------------------- | -------------------------------------------------------------------- |
| `get`                                        | Get workflow run details for a given workflow run ID.                |
| `aio_get`                                    | Get workflow run details for a given workflow run ID.                |
| `get_status`                                 | Get workflow run status for a given workflow run ID.                 |
| `aio_get_status`                             | Get workflow run status for a given workflow run ID.                 |
| `list`                                       | List task runs according to a set of filters.                        |
| `aio_list`                                   | List task runs according to a set of filters.                        |
| `create`                                     | Trigger a new workflow run.                                          |
| `aio_create`                                 | Trigger a new workflow run.                                          |
| `replay`                                     | Replay a task or workflow run.                                       |
| `aio_replay`                                 | Replay a task or workflow run.                                       |
| `bulk_replay`                                | Replay task or workflow runs in bulk, according to a set of filters. |
| `aio_bulk_replay`                            | Replay task or workflow runs in bulk, according to a set of filters. |
| `cancel`                                     | Cancel a task or workflow run.                                       |
| `aio_cancel`                                 | Cancel a task or workflow run.                                       |
| `bulk_cancel`                                | Cancel task or workflow runs in bulk, according to a set of filters. |
| `aio_bulk_cancel`                            | Cancel task or workflow runs in bulk, according to a set of filters. |
| `get_result`                                 | Get the result of a workflow run by its external ID.                 |
| `aio_get_result`                             | Get the result of a workflow run by its external ID.                 |
| `get_run_ref`                                | Get a reference to a workflow run.                                   |
| `get_task_run`                               | Get task run details for a given task run ID.                        |
| `aio_get_task_run`                           | Get task run details for a given task run ID.                        |
| `bulk_cancel_by_filters_with_pagination`     | Cancel runs matching the specified filters in chunks.                |
| `bulk_replay_by_filters_with_pagination`     | Replay runs matching the specified filters in chunks.                |
| `aio_bulk_cancel_by_filters_with_pagination` | Cancel runs matching the specified filters in chunks.                |
| `aio_bulk_replay_by_filters_with_pagination` | Replay runs matching the specified filters in chunks.                |
| `subscribe_to_stream`                        |                                                                      |

### Functions

#### `get`

Get workflow run details for a given workflow run ID.

Parameters:

| Name              | Type  | Description                                         | Default    |
| ----------------- | ----- | --------------------------------------------------- | ---------- |
| `workflow_run_id` | `str` | The ID of the workflow run to retrieve details for. | _required_ |

Returns:

| Type                   | Description                                             |
| ---------------------- | ------------------------------------------------------- |
| `V1WorkflowRunDetails` | Workflow run details for the specified workflow run ID. |

#### `aio_get`

Get workflow run details for a given workflow run ID.

Parameters:

| Name              | Type  | Description                                         | Default    |
| ----------------- | ----- | --------------------------------------------------- | ---------- |
| `workflow_run_id` | `str` | The ID of the workflow run to retrieve details for. | _required_ |

Returns:

| Type                   | Description                                             |
| ---------------------- | ------------------------------------------------------- |
| `V1WorkflowRunDetails` | Workflow run details for the specified workflow run ID. |

#### `get_status`

Get workflow run status for a given workflow run ID.

Parameters:

| Name              | Type  | Description                                         | Default    |
| ----------------- | ----- | --------------------------------------------------- | ---------- |
| `workflow_run_id` | `str` | The ID of the workflow run to retrieve details for. | _required_ |

Returns:

| Type           | Description     |
| -------------- | --------------- |
| `V1TaskStatus` | The task status |

#### `aio_get_status`

Get workflow run status for a given workflow run ID.

Parameters:

| Name              | Type  | Description                                         | Default    |
| ----------------- | ----- | --------------------------------------------------- | ---------- |
| `workflow_run_id` | `str` | The ID of the workflow run to retrieve details for. | _required_ |

Returns:

| Type           | Description     |
| -------------- | --------------- |
| `V1TaskStatus` | The task status |

#### `list`

List task runs according to a set of filters.

Parameters:

| Name                           | Type                         | Description                                         | Default |
| ------------------------------ | ---------------------------- | --------------------------------------------------- | ------- |
| `since`                        | `datetime \| None`           | The start time for filtering task runs.             | `None`  |
| `only_tasks`                   | `bool`                       | Whether to only list task runs.                     | `False` |
| `offset`                       | `int \| None`                | The offset for pagination.                          | `None`  |
| `limit`                        | `int \| None`                | The maximum number of task runs to return.          | `None`  |
| `statuses`                     | `list[V1TaskStatus] \| None` | The statuses to filter task runs by.                | `None`  |
| `until`                        | `datetime \| None`           | The end time for filtering task runs.               | `None`  |
| `additional_metadata`          | `dict[str, str] \| None`     | Additional metadata to filter task runs by.         | `None`  |
| `workflow_ids`                 | `list[str] \| None`          | The workflow IDs to filter task runs by.            | `None`  |
| `worker_id`                    | `str \| None`                | The worker ID to filter task runs by.               | `None`  |
| `parent_task_external_id`      | `str \| None`                | The parent task external ID to filter task runs by. | `None`  |
| `triggering_event_external_id` | `str \| None`                | The event id that triggered the task run.           | `None`  |
| `include_payloads`             | `bool`                       | Whether to include payloads in the response.        | `True`  |

Returns:

| Type                | Description                                         |
| ------------------- | --------------------------------------------------- |
| `V1TaskSummaryList` | A list of task runs matching the specified filters. |

#### `aio_list`

List task runs according to a set of filters.

Parameters:

| Name                           | Type                         | Description                                         | Default |
| ------------------------------ | ---------------------------- | --------------------------------------------------- | ------- |
| `since`                        | `datetime \| None`           | The start time for filtering task runs.             | `None`  |
| `only_tasks`                   | `bool`                       | Whether to only list task runs.                     | `False` |
| `offset`                       | `int \| None`                | The offset for pagination.                          | `None`  |
| `limit`                        | `int \| None`                | The maximum number of task runs to return.          | `None`  |
| `statuses`                     | `list[V1TaskStatus] \| None` | The statuses to filter task runs by.                | `None`  |
| `until`                        | `datetime \| None`           | The end time for filtering task runs.               | `None`  |
| `additional_metadata`          | `dict[str, str] \| None`     | Additional metadata to filter task runs by.         | `None`  |
| `workflow_ids`                 | `list[str] \| None`          | The workflow IDs to filter task runs by.            | `None`  |
| `worker_id`                    | `str \| None`                | The worker ID to filter task runs by.               | `None`  |
| `parent_task_external_id`      | `str \| None`                | The parent task external ID to filter task runs by. | `None`  |
| `triggering_event_external_id` | `str \| None`                | The event id that triggered the task run.           | `None`  |
| `include_payloads`             | `bool`                       | Whether to include payloads in the response.        | `True`  |

Returns:

| Type                | Description                                         |
| ------------------- | --------------------------------------------------- |
| `V1TaskSummaryList` | A list of task runs matching the specified filters. |

#### `create`

Trigger a new workflow run.

IMPORTANT: It's preferable to use `Workflow.run` (and similar) to trigger workflows if possible. This method is intended to be an escape hatch. For more details, see [the documentation](../../../sdk/python/runnables#workflow).

Parameters:

| Name                  | Type                              | Description                                           | Default    |
| --------------------- | --------------------------------- | ----------------------------------------------------- | ---------- |
| `workflow_name`       | `str`                             | The name of the workflow to trigger.                  | _required_ |
| `input`               | `JSONSerializableMapping`         | The input data for the workflow run.                  | _required_ |
| `additional_metadata` | `JSONSerializableMapping \| None` | Additional metadata associated with the workflow run. | `None`     |
| `priority`            | `int \| None`                     | The priority of the workflow run.                     | `None`     |

Returns:

| Type                   | Description                                |
| ---------------------- | ------------------------------------------ |
| `V1WorkflowRunDetails` | The details of the triggered workflow run. |

#### `aio_create`

Trigger a new workflow run.

IMPORTANT: It's preferable to use `Workflow.run` (and similar) to trigger workflows if possible. This method is intended to be an escape hatch. For more details, see [the documentation](../../../sdk/python/runnables#workflow).

Parameters:

| Name                  | Type                              | Description                                           | Default    |
| --------------------- | --------------------------------- | ----------------------------------------------------- | ---------- |
| `workflow_name`       | `str`                             | The name of the workflow to trigger.                  | _required_ |
| `input`               | `JSONSerializableMapping`         | The input data for the workflow run.                  | _required_ |
| `additional_metadata` | `JSONSerializableMapping \| None` | Additional metadata associated with the workflow run. | `None`     |
| `priority`            | `int \| None`                     | The priority of the workflow run.                     | `None`     |

Returns:

| Type                   | Description                                |
| ---------------------- | ------------------------------------------ |
| `V1WorkflowRunDetails` | The details of the triggered workflow run. |

#### `replay`

Replay a task or workflow run.

Parameters:

| Name     | Type  | Description                                            | Default    |
| -------- | ----- | ------------------------------------------------------ | ---------- |
| `run_id` | `str` | The external ID of the task or workflow run to replay. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `aio_replay`

Replay a task or workflow run.

Parameters:

| Name     | Type  | Description                                            | Default    |
| -------- | ----- | ------------------------------------------------------ | ---------- |
| `run_id` | `str` | The external ID of the task or workflow run to replay. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `bulk_replay`

Replay task or workflow runs in bulk, according to a set of filters.

Parameters:

| Name   | Type                   | Description                                         | Default    |
| ------ | ---------------------- | --------------------------------------------------- | ---------- |
| `opts` | `BulkCancelReplayOpts` | Options for bulk replay, including filters and IDs. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `aio_bulk_replay`

Replay task or workflow runs in bulk, according to a set of filters.

Parameters:

| Name   | Type                   | Description                                         | Default    |
| ------ | ---------------------- | --------------------------------------------------- | ---------- |
| `opts` | `BulkCancelReplayOpts` | Options for bulk replay, including filters and IDs. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `cancel`

Cancel a task or workflow run.

Parameters:

| Name     | Type  | Description                                            | Default    |
| -------- | ----- | ------------------------------------------------------ | ---------- |
| `run_id` | `str` | The external ID of the task or workflow run to cancel. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `aio_cancel`

Cancel a task or workflow run.

Parameters:

| Name     | Type  | Description                                            | Default    |
| -------- | ----- | ------------------------------------------------------ | ---------- |
| `run_id` | `str` | The external ID of the task or workflow run to cancel. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `bulk_cancel`

Cancel task or workflow runs in bulk, according to a set of filters.

Parameters:

| Name   | Type                   | Description                                         | Default    |
| ------ | ---------------------- | --------------------------------------------------- | ---------- |
| `opts` | `BulkCancelReplayOpts` | Options for bulk cancel, including filters and IDs. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `aio_bulk_cancel`

Cancel task or workflow runs in bulk, according to a set of filters.

Parameters:

| Name   | Type                   | Description                                         | Default    |
| ------ | ---------------------- | --------------------------------------------------- | ---------- |
| `opts` | `BulkCancelReplayOpts` | Options for bulk cancel, including filters and IDs. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `get_result`

Get the result of a workflow run by its external ID.

Parameters:

| Name     | Type  | Description                                                     | Default    |
| -------- | ----- | --------------------------------------------------------------- | ---------- |
| `run_id` | `str` | The external ID of the workflow run to retrieve the result for. | _required_ |

Returns:

| Type                      | Description                     |
| ------------------------- | ------------------------------- |
| `JSONSerializableMapping` | The result of the workflow run. |

#### `aio_get_result`

Get the result of a workflow run by its external ID.

Parameters:

| Name     | Type  | Description                                                     | Default    |
| -------- | ----- | --------------------------------------------------------------- | ---------- |
| `run_id` | `str` | The external ID of the workflow run to retrieve the result for. | _required_ |

Returns:

| Type                      | Description                     |
| ------------------------- | ------------------------------- |
| `JSONSerializableMapping` | The result of the workflow run. |

#### `get_run_ref`

Get a reference to a workflow run.

Parameters:

| Name              | Type  | Description                                       | Default    |
| ----------------- | ----- | ------------------------------------------------- | ---------- |
| `workflow_run_id` | `str` | The ID of the workflow run to get a reference to. | _required_ |

Returns:

| Type             | Description                                |
| ---------------- | ------------------------------------------ |
| `WorkflowRunRef` | A reference to the specified workflow run. |

#### `get_task_run`

Get task run details for a given task run ID.

Parameters:

| Name          | Type  | Description                                     | Default    |
| ------------- | ----- | ----------------------------------------------- | ---------- |
| `task_run_id` | `str` | The ID of the task run to retrieve details for. | _required_ |

Returns:

| Type            | Description                                     |
| --------------- | ----------------------------------------------- |
| `V1TaskSummary` | Task run details for the specified task run ID. |

#### `aio_get_task_run`

Get task run details for a given task run ID.

Parameters:

| Name          | Type  | Description                                     | Default    |
| ------------- | ----- | ----------------------------------------------- | ---------- |
| `task_run_id` | `str` | The ID of the task run to retrieve details for. | _required_ |

Returns:

| Type            | Description                                     |
| --------------- | ----------------------------------------------- |
| `V1TaskSummary` | Task run details for the specified task run ID. |

#### `bulk_cancel_by_filters_with_pagination`

Cancel runs matching the specified filters in chunks.

The motivation for this method is to provide an easy way to perform bulk operations by filters over a larger number of runs than the API would normally be able to handle, with automatic pagination and chunking to help limit the pressure on the API.

This method first pulls the IDs of the runs from the API, and then feeds them back to the API in chunks.

Parameters:

| Name                  | Type                         | Description                                              | Default |
| --------------------- | ---------------------------- | -------------------------------------------------------- | ------- |
| `sleep_time`          | `int`                        | The time to sleep between processing chunks, in seconds. | `3`     |
| `chunk_size`          | `int`                        | The maximum number of run IDs to process in each chunk.  | `500`   |
| `since`               | `datetime \| None`           | The start time for filtering runs.                       | `None`  |
| `until`               | `datetime \| None`           | The end time for filtering runs.                         | `None`  |
| `statuses`            | `list[V1TaskStatus] \| None` | The statuses to filter runs by.                          | `None`  |
| `additional_metadata` | `dict[str, str] \| None`     | Additional metadata to filter runs by.                   | `None`  |
| `workflow_ids`        | `list[str] \| None`          | The workflow IDs to filter runs by.                      | `None`  |

#### `bulk_replay_by_filters_with_pagination`

Replay runs matching the specified filters in chunks.

The motivation for this method is to provide an easy way to perform bulk operations by filters over a larger number of runs than the API would normally be able to handle, with automatic pagination and chunking to help limit the pressure on the API.

This method first pulls the IDs of the runs from the API, and then feeds them back to the API in chunks.

Parameters:

| Name                  | Type                         | Description                                              | Default |
| --------------------- | ---------------------------- | -------------------------------------------------------- | ------- |
| `sleep_time`          | `int`                        | The time to sleep between processing chunks, in seconds. | `3`     |
| `chunk_size`          | `int`                        | The maximum number of run IDs to process in each chunk.  | `500`   |
| `since`               | `datetime \| None`           | The start time for filtering runs.                       | `None`  |
| `until`               | `datetime \| None`           | The end time for filtering runs.                         | `None`  |
| `statuses`            | `list[V1TaskStatus] \| None` | The statuses to filter runs by.                          | `None`  |
| `additional_metadata` | `dict[str, str] \| None`     | Additional metadata to filter runs by.                   | `None`  |
| `workflow_ids`        | `list[str] \| None`          | The workflow IDs to filter runs by.                      | `None`  |

#### `aio_bulk_cancel_by_filters_with_pagination`

Cancel runs matching the specified filters in chunks.

The motivation for this method is to provide an easy way to perform bulk operations by filters over a larger number of runs than the API would normally be able to handle, with automatic pagination and chunking to help limit the pressure on the API.

This method first pulls the IDs of the runs from the API, and then feeds them back to the API in chunks.

Parameters:

| Name                  | Type                         | Description                                              | Default |
| --------------------- | ---------------------------- | -------------------------------------------------------- | ------- |
| `sleep_time`          | `int`                        | The time to sleep between processing chunks, in seconds. | `3`     |
| `chunk_size`          | `int`                        | The maximum number of run IDs to process in each chunk.  | `500`   |
| `since`               | `datetime \| None`           | The start time for filtering runs.                       | `None`  |
| `until`               | `datetime \| None`           | The end time for filtering runs.                         | `None`  |
| `statuses`            | `list[V1TaskStatus] \| None` | The statuses to filter runs by.                          | `None`  |
| `additional_metadata` | `dict[str, str] \| None`     | Additional metadata to filter runs by.                   | `None`  |
| `workflow_ids`        | `list[str] \| None`          | The workflow IDs to filter runs by.                      | `None`  |

#### `aio_bulk_replay_by_filters_with_pagination`

Replay runs matching the specified filters in chunks.

The motivation for this method is to provide an easy way to perform bulk operations by filters over a larger number of runs than the API would normally be able to handle, with automatic pagination and chunking to help limit the pressure on the API.

This method first pulls the IDs of the runs from the API, and then feeds them back to the API in chunks.

Parameters:

| Name                  | Type                         | Description                                              | Default |
| --------------------- | ---------------------------- | -------------------------------------------------------- | ------- |
| `sleep_time`          | `int`                        | The time to sleep between processing chunks, in seconds. | `3`     |
| `chunk_size`          | `int`                        | The maximum number of run IDs to process in each chunk.  | `500`   |
| `since`               | `datetime \| None`           | The start time for filtering runs.                       | `None`  |
| `until`               | `datetime \| None`           | The end time for filtering runs.                         | `None`  |
| `statuses`            | `list[V1TaskStatus] \| None` | The statuses to filter runs by.                          | `None`  |
| `additional_metadata` | `dict[str, str] \| None`     | Additional metadata to filter runs by.                   | `None`  |
| `workflow_ids`        | `list[str] \| None`          | The workflow IDs to filter runs by.                      | `None`  |

#### `subscribe_to_stream`


---

<!-- Source: https://docs.hatchet.run/reference/python/feature-clients/scheduled -->

# Scheduled Client

Bases: `BaseRestClient`

The scheduled client is a client for managing scheduled workflows within Hatchet.

Methods:

| Name              | Description                                                          |
| ----------------- | -------------------------------------------------------------------- |
| `aio_bulk_delete` | Bulk delete scheduled workflow runs.                                 |
| `aio_bulk_update` | Bulk reschedule scheduled workflow runs.                             |
| `aio_create`      | Creates a new scheduled workflow run.                                |
| `aio_delete`      | Deletes a scheduled workflow run by its ID.                          |
| `aio_get`         | Retrieves a specific scheduled workflow by scheduled run trigger ID. |
| `aio_list`        | Retrieves a list of scheduled workflows based on provided filters.   |
| `aio_update`      | Reschedule a scheduled workflow run by its ID.                       |
| `bulk_delete`     | Bulk delete scheduled workflow runs.                                 |
| `bulk_update`     | Bulk reschedule scheduled workflow runs.                             |
| `create`          | Creates a new scheduled workflow run.                                |
| `delete`          | Deletes a scheduled workflow run by its ID.                          |
| `get`             | Retrieves a specific scheduled workflow by scheduled run trigger ID. |
| `list`            | Retrieves a list of scheduled workflows based on provided filters.   |
| `update`          | Reschedule a scheduled workflow run by its ID.                       |

### Functions

#### `aio_bulk_delete`

Bulk delete scheduled workflow runs.

Parameters:

| Name                     | Type                               | Description                                            | Default |
| ------------------------ | ---------------------------------- | ------------------------------------------------------ | ------- |
| `scheduled_ids`          | `list[str] \| None`                | Explicit list of scheduled workflow run IDs to delete. | `None`  |
| `workflow_id`            | `str \| None`                      | Filter by workflow ID.                                 | `None`  |
| `parent_workflow_run_id` | `str \| None`                      | Filter by parent workflow run ID.                      | `None`  |
| `parent_step_run_id`     | `str \| None`                      | Filter by parent step run ID.                          | `None`  |
| `statuses`               | `list[ScheduledRunStatus] \| None` | Filter by scheduled run statuses.                      | `None`  |
| `additional_metadata`    | `JSONSerializableMapping \| None`  | Filter by additional metadata key/value pairs.         | `None`  |

Returns:

| Type                                   | Description                                                          |
| -------------------------------------- | -------------------------------------------------------------------- |
| `ScheduledWorkflowsBulkDeleteResponse` | The bulk delete response containing deleted IDs and per-item errors. |

Raises:

| Type         | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| `ValueError` | If neither `scheduled_ids` nor any filter field is provided. |

#### `aio_bulk_update`

Bulk reschedule scheduled workflow runs.

See `bulk_update` for parameter details.

#### `aio_create`

Creates a new scheduled workflow run.

IMPORTANT: It's preferable to use `Workflow.run` (and similar) to trigger workflows if possible. This method is intended to be an escape hatch. For more details, see [the documentation](../../../sdk/python/runnables#workflow).

Parameters:

| Name                  | Type                      | Description                                                             | Default    |
| --------------------- | ------------------------- | ----------------------------------------------------------------------- | ---------- |
| `workflow_name`       | `str`                     | The name of the workflow to schedule.                                   | _required_ |
| `trigger_at`          | `datetime`                | The datetime when the run should be triggered.                          | _required_ |
| `input`               | `JSONSerializableMapping` | The input data for the scheduled workflow.                              | _required_ |
| `additional_metadata` | `JSONSerializableMapping` | Additional metadata associated with the future run as a key-value pair. | _required_ |

Returns:

| Type                 | Description                              |
| -------------------- | ---------------------------------------- |
| `ScheduledWorkflows` | The created scheduled workflow instance. |

#### `aio_delete`

Deletes a scheduled workflow run by its ID.

Parameters:

| Name           | Type  | Description                                     | Default    |
| -------------- | ----- | ----------------------------------------------- | ---------- |
| `scheduled_id` | `str` | The ID of the scheduled workflow run to delete. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `aio_get`

Retrieves a specific scheduled workflow by scheduled run trigger ID.

Parameters:

| Name           | Type  | Description                                    | Default    |
| -------------- | ----- | ---------------------------------------------- | ---------- |
| `scheduled_id` | `str` | The scheduled workflow trigger ID to retrieve. | _required_ |

Returns:

| Type                 | Description                                |
| -------------------- | ------------------------------------------ |
| `ScheduledWorkflows` | The requested scheduled workflow instance. |

#### `aio_list`

Retrieves a list of scheduled workflows based on provided filters.

Parameters:

| Name                     | Type                                     | Description                                          | Default |
| ------------------------ | ---------------------------------------- | ---------------------------------------------------- | ------- |
| `offset`                 | `int \| None`                            | The offset to use in pagination.                     | `None`  |
| `limit`                  | `int \| None`                            | The maximum number of scheduled workflows to return. | `None`  |
| `workflow_id`            | `str \| None`                            | The ID of the workflow to filter by.                 | `None`  |
| `parent_workflow_run_id` | `str \| None`                            | The ID of the parent workflow run to filter by.      | `None`  |
| `statuses`               | `list[ScheduledRunStatus] \| None`       | A list of statuses to filter by.                     | `None`  |
| `additional_metadata`    | `JSONSerializableMapping \| None`        | Additional metadata to filter by.                    | `None`  |
| `order_by_field`         | `ScheduledWorkflowsOrderByField \| None` | The field to order the results by.                   | `None`  |
| `order_by_direction`     | `WorkflowRunOrderByDirection \| None`    | The direction to order the results by.               | `None`  |

Returns:

| Type                     | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| `ScheduledWorkflowsList` | A list of scheduled workflows matching the provided filters. |

#### `aio_update`

Reschedule a scheduled workflow run by its ID.

Parameters:

| Name           | Type       | Description                                         | Default    |
| -------------- | ---------- | --------------------------------------------------- | ---------- |
| `scheduled_id` | `str`      | The ID of the scheduled workflow run to reschedule. | _required_ |
| `trigger_at`   | `datetime` | The datetime when the run should be triggered.      | _required_ |

Returns:

| Type                 | Description                              |
| -------------------- | ---------------------------------------- |
| `ScheduledWorkflows` | The updated scheduled workflow instance. |

#### `bulk_delete`

Bulk delete scheduled workflow runs.

Provide either:

- `scheduled_ids` (explicit list of scheduled run IDs), or
- one or more filter fields (`workflow_id`, `parent_workflow_run_id`, `parent_step_run_id`, `statuses`, `additional_metadata`)

Parameters:

| Name                     | Type                               | Description                                            | Default |
| ------------------------ | ---------------------------------- | ------------------------------------------------------ | ------- |
| `scheduled_ids`          | `list[str] \| None`                | Explicit list of scheduled workflow run IDs to delete. | `None`  |
| `workflow_id`            | `str \| None`                      | Filter by workflow ID.                                 | `None`  |
| `parent_workflow_run_id` | `str \| None`                      | Filter by parent workflow run ID.                      | `None`  |
| `parent_step_run_id`     | `str \| None`                      | Filter by parent step run ID.                          | `None`  |
| `statuses`               | `list[ScheduledRunStatus] \| None` | Filter by scheduled run statuses.                      | `None`  |
| `additional_metadata`    | `JSONSerializableMapping \| None`  | Filter by additional metadata key/value pairs.         | `None`  |

Returns:

| Type                                   | Description                                                          |
| -------------------------------------- | -------------------------------------------------------------------- |
| `ScheduledWorkflowsBulkDeleteResponse` | The bulk delete response containing deleted IDs and per-item errors. |

Raises:

| Type         | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| `ValueError` | If neither `scheduled_ids` nor any filter field is provided. |

#### `bulk_update`

Bulk reschedule scheduled workflow runs.

Parameters:

| Name      | Type                                                                   | Description                                                                                                        | Default    |
| --------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---------- |
| `updates` | `list[ScheduledWorkflowsBulkUpdateItem] \| list[tuple[str, datetime]]` | Either: - a list of `(scheduled_id, trigger_at)` tuples, or - a list of `ScheduledWorkflowsBulkUpdateItem` objects | _required_ |

Returns:

| Type                                   | Description                                                          |
| -------------------------------------- | -------------------------------------------------------------------- |
| `ScheduledWorkflowsBulkUpdateResponse` | The bulk update response containing updated IDs and per-item errors. |

#### `create`

Creates a new scheduled workflow run.

IMPORTANT: It's preferable to use `Workflow.run` (and similar) to trigger workflows if possible. This method is intended to be an escape hatch. For more details, see [the documentation](../../../sdk/python/runnables#workflow).

Parameters:

| Name                  | Type                      | Description                                                             | Default    |
| --------------------- | ------------------------- | ----------------------------------------------------------------------- | ---------- |
| `workflow_name`       | `str`                     | The name of the workflow to schedule.                                   | _required_ |
| `trigger_at`          | `datetime`                | The datetime when the run should be triggered.                          | _required_ |
| `input`               | `JSONSerializableMapping` | The input data for the scheduled workflow.                              | _required_ |
| `additional_metadata` | `JSONSerializableMapping` | Additional metadata associated with the future run as a key-value pair. | _required_ |

Returns:

| Type                 | Description                              |
| -------------------- | ---------------------------------------- |
| `ScheduledWorkflows` | The created scheduled workflow instance. |

#### `delete`

Deletes a scheduled workflow run by its ID.

Parameters:

| Name           | Type  | Description                                     | Default    |
| -------------- | ----- | ----------------------------------------------- | ---------- |
| `scheduled_id` | `str` | The ID of the scheduled workflow run to delete. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `get`

Retrieves a specific scheduled workflow by scheduled run trigger ID.

Parameters:

| Name           | Type  | Description                                    | Default    |
| -------------- | ----- | ---------------------------------------------- | ---------- |
| `scheduled_id` | `str` | The scheduled workflow trigger ID to retrieve. | _required_ |

Returns:

| Type                 | Description                                |
| -------------------- | ------------------------------------------ |
| `ScheduledWorkflows` | The requested scheduled workflow instance. |

#### `list`

Retrieves a list of scheduled workflows based on provided filters.

Parameters:

| Name                     | Type                                     | Description                                          | Default |
| ------------------------ | ---------------------------------------- | ---------------------------------------------------- | ------- |
| `offset`                 | `int \| None`                            | The offset to use in pagination.                     | `None`  |
| `limit`                  | `int \| None`                            | The maximum number of scheduled workflows to return. | `None`  |
| `workflow_id`            | `str \| None`                            | The ID of the workflow to filter by.                 | `None`  |
| `parent_workflow_run_id` | `str \| None`                            | The ID of the parent workflow run to filter by.      | `None`  |
| `statuses`               | `list[ScheduledRunStatus] \| None`       | A list of statuses to filter by.                     | `None`  |
| `additional_metadata`    | `JSONSerializableMapping \| None`        | Additional metadata to filter by.                    | `None`  |
| `order_by_field`         | `ScheduledWorkflowsOrderByField \| None` | The field to order the results by.                   | `None`  |
| `order_by_direction`     | `WorkflowRunOrderByDirection \| None`    | The direction to order the results by.               | `None`  |

Returns:

| Type                     | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| `ScheduledWorkflowsList` | A list of scheduled workflows matching the provided filters. |

#### `update`

Reschedule a scheduled workflow run by its ID.

Note: the server may reject rescheduling if the scheduled run has already
triggered, or if it was created via code definition (not via API).

Parameters:

| Name           | Type       | Description                                         | Default    |
| -------------- | ---------- | --------------------------------------------------- | ---------- |
| `scheduled_id` | `str`      | The ID of the scheduled workflow run to reschedule. | _required_ |
| `trigger_at`   | `datetime` | The datetime when the run should be triggered.      | _required_ |

Returns:

| Type                 | Description                              |
| -------------------- | ---------------------------------------- |
| `ScheduledWorkflows` | The updated scheduled workflow instance. |


---

<!-- Source: https://docs.hatchet.run/reference/python/feature-clients/webhooks -->

# Webhooks Client

Bases: `BaseRestClient`

The webhooks client provides methods for managing incoming webhooks in Hatchet.

Webhooks allow external systems to trigger Hatchet workflows by sending HTTP requests to dedicated endpoints. This enables real-time integration with third-party services like GitHub, Stripe, Slack, or any system that can send webhook events.

Methods:

| Name         | Description                       |
| ------------ | --------------------------------- |
| `aio_create` | Create a new webhook.             |
| `aio_delete` | Delete a webhook by its name.     |
| `aio_get`    | Get a webhook by its name.        |
| `aio_list`   | List webhooks for a given tenant. |
| `aio_update` | Update a webhook by its name.     |
| `create`     | Create a new webhook.             |
| `delete`     | Delete a webhook by its name.     |
| `get`        | Get a webhook by its name.        |
| `list`       | List webhooks for a given tenant. |
| `update`     | Update a webhook by its name.     |

### Functions

#### `aio_create`

Create a new webhook.

Parameters:

| Name                   | Type                                                             | Description                                                                      | Default    |
| ---------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------- | ---------- |
| `source_name`          | `V1WebhookSourceName`                                            | The source name identifying the external system sending webhook events.          | _required_ |
| `name`                 | `str`                                                            | The name of the webhook.                                                         | _required_ |
| `event_key_expression` | `str`                                                            | A CEL expression used to extract the event key from the incoming payload.        | _required_ |
| `auth`                 | `V1WebhookBasicAuth \| V1WebhookAPIKeyAuth \| V1WebhookHMACAuth` | The authentication configuration for the webhook (basic auth, API key, or HMAC). | _required_ |
| `scope_expression`     | `str \| None`                                                    | An optional CEL expression used to extract the scope from the incoming payload.  | `None`     |
| `static_payload`       | `dict[str, Any] \| None`                                         | An optional static payload to merge into every triggered event.                  | `None`     |

Returns:

| Type        | Description          |
| ----------- | -------------------- |
| `V1Webhook` | The created webhook. |

#### `aio_delete`

Delete a webhook by its name.

Parameters:

| Name           | Type  | Description                        | Default    |
| -------------- | ----- | ---------------------------------- | ---------- |
| `webhook_name` | `str` | The name of the webhook to delete. | _required_ |

Returns:

| Type        | Description          |
| ----------- | -------------------- |
| `V1Webhook` | The deleted webhook. |

#### `aio_get`

Get a webhook by its name.

Parameters:

| Name           | Type  | Description                          | Default    |
| -------------- | ----- | ------------------------------------ | ---------- |
| `webhook_name` | `str` | The name of the webhook to retrieve. | _required_ |

Returns:

| Type        | Description                          |
| ----------- | ------------------------------------ |
| `V1Webhook` | The webhook with the specified name. |

#### `aio_list`

List webhooks for a given tenant.

Parameters:

| Name            | Type                                | Description                                                               | Default |
| --------------- | ----------------------------------- | ------------------------------------------------------------------------- | ------- |
| `limit`         | `int \| None`                       | The maximum number of webhooks to return.                                 | `None`  |
| `offset`        | `int \| None`                       | The number of webhooks to skip before starting to collect the result set. | `None`  |
| `webhook_names` | `list[str] \| None`                 | A list of webhook names to filter by.                                     | `None`  |
| `source_names`  | `list[V1WebhookSourceName] \| None` | A list of source names to filter by.                                      | `None`  |

Returns:

| Type            | Description                                         |
| --------------- | --------------------------------------------------- |
| `V1WebhookList` | A list of webhooks matching the specified criteria. |

#### `aio_update`

Update a webhook by its name.

Parameters:

| Name                   | Type                     | Description                                                                        | Default    |
| ---------------------- | ------------------------ | ---------------------------------------------------------------------------------- | ---------- |
| `webhook_name`         | `str`                    | The name of the webhook to update.                                                 | _required_ |
| `event_key_expression` | `str \| None`            | An updated CEL expression used to extract the event key from the incoming payload. | `None`     |
| `scope_expression`     | `str \| None`            | An updated CEL expression used to extract the scope from the incoming payload.     | `None`     |
| `static_payload`       | `dict[str, Any] \| None` | An updated static payload to merge into every triggered event.                     | `None`     |

Returns:

| Type        | Description          |
| ----------- | -------------------- |
| `V1Webhook` | The updated webhook. |

#### `create`

Create a new webhook.

Parameters:

| Name                   | Type                                                             | Description                                                                      | Default    |
| ---------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------- | ---------- |
| `source_name`          | `V1WebhookSourceName`                                            | The source name identifying the external system sending webhook events.          | _required_ |
| `name`                 | `str`                                                            | The name of the webhook.                                                         | _required_ |
| `event_key_expression` | `str`                                                            | A CEL expression used to extract the event key from the incoming payload.        | _required_ |
| `auth`                 | `V1WebhookBasicAuth \| V1WebhookAPIKeyAuth \| V1WebhookHMACAuth` | The authentication configuration for the webhook (basic auth, API key, or HMAC). | _required_ |
| `scope_expression`     | `str \| None`                                                    | An optional CEL expression used to extract the scope from the incoming payload.  | `None`     |
| `static_payload`       | `dict[str, Any] \| None`                                         | An optional static payload to merge into every triggered event.                  | `None`     |

Returns:

| Type        | Description          |
| ----------- | -------------------- |
| `V1Webhook` | The created webhook. |

#### `delete`

Delete a webhook by its name.

Parameters:

| Name           | Type  | Description                        | Default    |
| -------------- | ----- | ---------------------------------- | ---------- |
| `webhook_name` | `str` | The name of the webhook to delete. | _required_ |

Returns:

| Type        | Description          |
| ----------- | -------------------- |
| `V1Webhook` | The deleted webhook. |

#### `get`

Get a webhook by its name.

Parameters:

| Name           | Type  | Description                          | Default    |
| -------------- | ----- | ------------------------------------ | ---------- |
| `webhook_name` | `str` | The name of the webhook to retrieve. | _required_ |

Returns:

| Type        | Description                          |
| ----------- | ------------------------------------ |
| `V1Webhook` | The webhook with the specified name. |

#### `list`

List webhooks for a given tenant.

Parameters:

| Name            | Type                                | Description                                                               | Default |
| --------------- | ----------------------------------- | ------------------------------------------------------------------------- | ------- |
| `limit`         | `int \| None`                       | The maximum number of webhooks to return.                                 | `None`  |
| `offset`        | `int \| None`                       | The number of webhooks to skip before starting to collect the result set. | `None`  |
| `webhook_names` | `list[str] \| None`                 | A list of webhook names to filter by.                                     | `None`  |
| `source_names`  | `list[V1WebhookSourceName] \| None` | A list of source names to filter by.                                      | `None`  |

Returns:

| Type            | Description                                         |
| --------------- | --------------------------------------------------- |
| `V1WebhookList` | A list of webhooks matching the specified criteria. |

#### `update`

Update a webhook by its name.

Parameters:

| Name                   | Type                     | Description                                                                        | Default    |
| ---------------------- | ------------------------ | ---------------------------------------------------------------------------------- | ---------- |
| `webhook_name`         | `str`                    | The name of the webhook to update.                                                 | _required_ |
| `event_key_expression` | `str \| None`            | An updated CEL expression used to extract the event key from the incoming payload. | `None`     |
| `scope_expression`     | `str \| None`            | An updated CEL expression used to extract the scope from the incoming payload.     | `None`     |
| `static_payload`       | `dict[str, Any] \| None` | An updated static payload to merge into every triggered event.                     | `None`     |

Returns:

| Type        | Description          |
| ----------- | -------------------- |
| `V1Webhook` | The updated webhook. |


---

<!-- Source: https://docs.hatchet.run/reference/python/feature-clients/workers -->

# Workers Client

Bases: `BaseRestClient`

The workers client is a client for managing workers programmatically within Hatchet.

Methods:

| Name         | Description                                                     |
| ------------ | --------------------------------------------------------------- |
| `aio_get`    | Get a worker by its ID.                                         |
| `aio_list`   | List all workers in the tenant determined by the client config. |
| `aio_update` | Update a worker by its ID.                                      |
| `get`        | Get a worker by its ID.                                         |
| `list`       | List all workers in the tenant determined by the client config. |
| `update`     | Update a worker by its ID.                                      |

### Functions

#### `aio_get`

Get a worker by its ID.

Parameters:

| Name        | Type  | Description                       | Default    |
| ----------- | ----- | --------------------------------- | ---------- |
| `worker_id` | `str` | The ID of the worker to retrieve. | _required_ |

Returns:

| Type     | Description |
| -------- | ----------- |
| `Worker` | The worker. |

#### `aio_list`

List all workers in the tenant determined by the client config.

Returns:

| Type         | Description        |
| ------------ | ------------------ |
| `WorkerList` | A list of workers. |

#### `aio_update`

Update a worker by its ID.

Parameters:

| Name        | Type                  | Description                     | Default    |
| ----------- | --------------------- | ------------------------------- | ---------- |
| `worker_id` | `str`                 | The ID of the worker to update. | _required_ |
| `opts`      | `UpdateWorkerRequest` | The update options.             | _required_ |

Returns:

| Type     | Description         |
| -------- | ------------------- |
| `Worker` | The updated worker. |

#### `get`

Get a worker by its ID.

Parameters:

| Name        | Type  | Description                       | Default    |
| ----------- | ----- | --------------------------------- | ---------- |
| `worker_id` | `str` | The ID of the worker to retrieve. | _required_ |

Returns:

| Type     | Description |
| -------- | ----------- |
| `Worker` | The worker. |

#### `list`

List all workers in the tenant determined by the client config.

Returns:

| Type         | Description        |
| ------------ | ------------------ |
| `WorkerList` | A list of workers. |

#### `update`

Update a worker by its ID.

Parameters:

| Name        | Type                  | Description                     | Default    |
| ----------- | --------------------- | ------------------------------- | ---------- |
| `worker_id` | `str`                 | The ID of the worker to update. | _required_ |
| `opts`      | `UpdateWorkerRequest` | The update options.             | _required_ |

Returns:

| Type     | Description         |
| -------- | ------------------- |
| `Worker` | The updated worker. |


---

<!-- Source: https://docs.hatchet.run/reference/python/feature-clients/workflows -->

# Workflows Client

Bases: `BaseRestClient`

The workflows client is a client for managing workflows programmatically within Hatchet.

Note that workflows are the declaration, _not_ the individual runs. If you're looking for runs, use the `RunsClient` instead.

Methods:

| Name              | Description                                                                                   |
| ----------------- | --------------------------------------------------------------------------------------------- |
| `aio_delete`      | Permanently delete a workflow.                                                                |
| `aio_get`         | Get a workflow by its ID.                                                                     |
| `aio_get_version` | Get a workflow version by the workflow ID and an optional version.                            |
| `aio_list`        | List all workflows in the tenant determined by the client config that match optional filters. |
| `delete`          | Permanently delete a workflow.                                                                |
| `get`             | Get a workflow by its ID.                                                                     |
| `get_version`     | Get a workflow version by the workflow ID and an optional version.                            |
| `list`            | List all workflows in the tenant determined by the client config that match optional filters. |

### Functions

#### `aio_delete`

Permanently delete a workflow.

**DANGEROUS: This will delete a workflow and all of its data**

Parameters:

| Name          | Type  | Description                       | Default    |
| ------------- | ----- | --------------------------------- | ---------- |
| `workflow_id` | `str` | The ID of the workflow to delete. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `aio_get`

Get a workflow by its ID.

Parameters:

| Name          | Type  | Description                         | Default    |
| ------------- | ----- | ----------------------------------- | ---------- |
| `workflow_id` | `str` | The ID of the workflow to retrieve. | _required_ |

Returns:

| Type       | Description   |
| ---------- | ------------- |
| `Workflow` | The workflow. |

#### `aio_get_version`

Get a workflow version by the workflow ID and an optional version.

Parameters:

| Name          | Type          | Description                                                                       | Default    |
| ------------- | ------------- | --------------------------------------------------------------------------------- | ---------- |
| `workflow_id` | `str`         | The ID of the workflow to retrieve the version for.                               | _required_ |
| `version`     | `str \| None` | The version of the workflow to retrieve. If None, the latest version is returned. | `None`     |

Returns:

| Type              | Description           |
| ----------------- | --------------------- |
| `WorkflowVersion` | The workflow version. |

#### `aio_list`

List all workflows in the tenant determined by the client config that match optional filters.

Parameters:

| Name            | Type          | Description                            | Default |
| --------------- | ------------- | -------------------------------------- | ------- |
| `workflow_name` | `str \| None` | The name of the workflow to filter by. | `None`  |
| `limit`         | `int \| None` | The maximum number of items to return. | `None`  |
| `offset`        | `int \| None` | The offset to start the list from.     | `None`  |

Returns:

| Type           | Description          |
| -------------- | -------------------- |
| `WorkflowList` | A list of workflows. |

#### `delete`

Permanently delete a workflow.

**DANGEROUS: This will delete a workflow and all of its data**

Parameters:

| Name          | Type  | Description                       | Default    |
| ------------- | ----- | --------------------------------- | ---------- |
| `workflow_id` | `str` | The ID of the workflow to delete. | _required_ |

Returns:

| Type   | Description |
| ------ | ----------- |
| `None` | None        |

#### `get`

Get a workflow by its ID.

Parameters:

| Name          | Type  | Description                         | Default    |
| ------------- | ----- | ----------------------------------- | ---------- |
| `workflow_id` | `str` | The ID of the workflow to retrieve. | _required_ |

Returns:

| Type       | Description   |
| ---------- | ------------- |
| `Workflow` | The workflow. |

#### `get_version`

Get a workflow version by the workflow ID and an optional version.

Parameters:

| Name          | Type          | Description                                                                       | Default    |
| ------------- | ------------- | --------------------------------------------------------------------------------- | ---------- |
| `workflow_id` | `str`         | The ID of the workflow to retrieve the version for.                               | _required_ |
| `version`     | `str \| None` | The version of the workflow to retrieve. If None, the latest version is returned. | `None`     |

Returns:

| Type              | Description           |
| ----------------- | --------------------- |
| `WorkflowVersion` | The workflow version. |

#### `list`

List all workflows in the tenant determined by the client config that match optional filters.

Parameters:

| Name            | Type          | Description                            | Default |
| --------------- | ------------- | -------------------------------------- | ------- |
| `workflow_name` | `str \| None` | The name of the workflow to filter by. | `None`  |
| `limit`         | `int \| None` | The maximum number of items to return. | `None`  |
| `offset`        | `int \| None` | The offset to start the list from.     | `None`  |

Returns:

| Type           | Description          |
| -------------- | -------------------- |
| `WorkflowList` | A list of workflows. |


---

<!-- Source: https://docs.hatchet.run/reference/python/runnables -->

# Runnables

`Runnables` in the Hatchet SDK are things that can be run, namely tasks and workflows. The two main types of runnables you'll encounter are:

- `Workflow`, which lets you define tasks and call all of the run, schedule, etc. methods
- `Standalone`, which is a single task that's returned by `hatchet.task` and can be run, scheduled, etc.

## Workflow

Bases: `BaseWorkflow[TWorkflowInput]`

A Hatchet workflow, which allows you to define tasks to be run and perform actions on the workflow.

Workflows in Hatchet represent coordinated units of work that can be triggered, scheduled, or run on a cron schedule. Each workflow can contain multiple tasks that can be arranged in dependencies (DAGs), have customized retry behavior, timeouts, concurrency controls, and more.

Example:

```python
from pydantic import BaseModel
from hatchet_sdk import Hatchet

class MyInput(BaseModel):
    name: str

hatchet = Hatchet()
workflow = hatchet.workflow("my-workflow", input_type=MyInput)

@workflow.task()
def greet(input, ctx):
    return f"Hello, {input.name}!"

# Run the workflow
result = workflow.run(MyInput(name="World"))
```

Workflows support various execution patterns including:

- One-time execution with `run()` or `aio_run()`
- Scheduled execution with `schedule()`
- Cron-based recurring execution with `create_cron()`
- Bulk operations with `run_many()`

Tasks within workflows can be defined with `@workflow.task()` or `@workflow.durable_task()` decorators and can be arranged into complex dependency patterns.

Methods:

| Name                   | Description                                                                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `task`                 | A decorator to transform a function into a Hatchet task that runs as part of a workflow.                                                         |
| `durable_task`         | A decorator to transform a function into a durable Hatchet task that runs as part of a workflow.                                                 |
| `on_failure_task`      | A decorator to transform a function into a Hatchet on-failure task that runs as the last step in a workflow that had at least one task fail.     |
| `on_success_task`      | A decorator to transform a function into a Hatchet on-success task that runs as the last step in a workflow that had all upstream tasks succeed. |
| `run`                  | Run the workflow synchronously and wait for it to complete.                                                                                      |
| `aio_run`              | Run the workflow asynchronously and wait for it to complete.                                                                                     |
| `run_no_wait`          | Synchronously trigger a workflow run without waiting for it to complete.                                                                         |
| `aio_run_no_wait`      | Asynchronously trigger a workflow run without waiting for it to complete.                                                                        |
| `run_many`             | Run a workflow in bulk and wait for all runs to complete.                                                                                        |
| `aio_run_many`         | Run a workflow in bulk and wait for all runs to complete.                                                                                        |
| `run_many_no_wait`     | Run a workflow in bulk without waiting for all runs to complete.                                                                                 |
| `aio_run_many_no_wait` | Run a workflow in bulk without waiting for all runs to complete.                                                                                 |
| `schedule`             | Schedule a workflow to run at a specific time.                                                                                                   |
| `aio_schedule`         | Schedule a workflow to run at a specific time.                                                                                                   |
| `create_cron`          | Create a cron job for the workflow.                                                                                                              |
| `aio_create_cron`      | Create a cron job for the workflow.                                                                                                              |
| `create_bulk_run_item` | Create a bulk run item for the workflow. This is intended to be used in conjunction with the various `run_many` methods.                         |
| `list_runs`            | List runs of the workflow.                                                                                                                       |
| `aio_list_runs`        | List runs of the workflow.                                                                                                                       |
| `create_filter`        | Create a new filter.                                                                                                                             |
| `aio_create_filter`    | Create a new filter.                                                                                                                             |

### Attributes

#### `name`

The (namespaced) name of the workflow.

#### `tasks`

#### `id`

`cached`

Get the ID of the workflow.

Returns:

| Type  | Description             |
| ----- | ----------------------- |
| `str` | The ID of the workflow. |

Raises:

| Type         | Description                                       |
| ------------ | ------------------------------------------------- |
| `ValueError` | If no workflow ID is found for the workflow name. |

### Functions

#### `task`

A decorator to transform a function into a Hatchet task that runs as part of a workflow.

Parameters:

| Name                    | Type                                         | Description                                                                                                                                                                                                                             | Default                 |
| ----------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `name`                  | `str \| None`                                | The name of the task. If not specified, defaults to the name of the function being wrapped by the `task` decorator.                                                                                                                     | `None`                  |
| `schedule_timeout`      | `Duration`                                   | The maximum time to wait for the task to be scheduled. The run will be canceled if the task does not begin within this time.                                                                                                            | `timedelta(minutes=5)`  |
| `execution_timeout`     | `Duration`                                   | The maximum time to wait for the task to complete. The run will be canceled if the task does not complete within this time.                                                                                                             | `timedelta(seconds=60)` |
| `parents`               | `list[Task[TWorkflowInput, Any]] \| None`    | A list of tasks that are parents of the task. Note: Parents must be defined before their children.                                                                                                                                      | `None`                  |
| `retries`               | `int`                                        | The number of times to retry the task before failing.                                                                                                                                                                                   | `0`                     |
| `rate_limits`           | `list[RateLimit] \| None`                    | A list of rate limit configurations for the task.                                                                                                                                                                                       | `None`                  |
| `desired_worker_labels` | `dict[str, DesiredWorkerLabel] \| None`      | A dictionary of desired worker labels that determine to which worker the task should be assigned. See documentation and examples on affinity and worker labels for more details.                                                        | `None`                  |
| `backoff_factor`        | `float \| None`                              | The backoff factor for controlling exponential backoff in retries.                                                                                                                                                                      | `None`                  |
| `backoff_max_seconds`   | `int \| None`                                | The maximum number of seconds to allow retries with exponential backoff to continue.                                                                                                                                                    | `None`                  |
| `concurrency`           | `int \| list[ConcurrencyExpression] \| None` | A list of concurrency expressions for the task. If an integer is provided, it is treated as a constant concurrency limit with a `GROUP_ROUND_ROBIN` strategy, which means that only `N` runs of the task may execute at any given time. | `None`                  |
| `wait_for`              | `list[Condition \| OrGroup] \| None`         | A list of conditions that must be met before the task can run.                                                                                                                                                                          | `None`                  |
| `skip_if`               | `list[Condition \| OrGroup] \| None`         | A list of conditions that, if met, will cause the task to be skipped.                                                                                                                                                                   | `None`                  |
| `cancel_if`             | `list[Condition \| OrGroup] \| None`         | A list of conditions that, if met, will cause the task to be canceled.                                                                                                                                                                  | `None`                  |

Returns:

| Type                                                                                                            | Description                                |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| `Callable[[Callable[Concatenate[TWorkflowInput, Context, P], R \| CoroutineLike[R]]], Task[TWorkflowInput, R]]` | A decorator which creates a `Task` object. |

#### `durable_task`

A decorator to transform a function into a durable Hatchet task that runs as part of a workflow.

**IMPORTANT:** This decorator creates a _durable_ task, which works using Hatchet's durable execution capabilities. This is an advanced feature of Hatchet.

See the Hatchet docs for more information on durable execution to decide if this is right for you.

Parameters:

| Name                    | Type                                         | Description                                                                                                                                                                                                                             | Default                 |
| ----------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `name`                  | `str \| None`                                | The name of the task. If not specified, defaults to the name of the function being wrapped by the `task` decorator.                                                                                                                     | `None`                  |
| `schedule_timeout`      | `Duration`                                   | The maximum time to wait for the task to be scheduled. The run will be canceled if the task does not begin within this time.                                                                                                            | `timedelta(minutes=5)`  |
| `execution_timeout`     | `Duration`                                   | The maximum time to wait for the task to complete. The run will be canceled if the task does not complete within this time.                                                                                                             | `timedelta(seconds=60)` |
| `parents`               | `list[Task[TWorkflowInput, Any]] \| None`    | A list of tasks that are parents of the task. Note: Parents must be defined before their children.                                                                                                                                      | `None`                  |
| `retries`               | `int`                                        | The number of times to retry the task before failing.                                                                                                                                                                                   | `0`                     |
| `rate_limits`           | `list[RateLimit] \| None`                    | A list of rate limit configurations for the task.                                                                                                                                                                                       | `None`                  |
| `desired_worker_labels` | `dict[str, DesiredWorkerLabel] \| None`      | A dictionary of desired worker labels that determine to which worker the task should be assigned. See documentation and examples on affinity and worker labels for more details.                                                        | `None`                  |
| `backoff_factor`        | `float \| None`                              | The backoff factor for controlling exponential backoff in retries.                                                                                                                                                                      | `None`                  |
| `backoff_max_seconds`   | `int \| None`                                | The maximum number of seconds to allow retries with exponential backoff to continue.                                                                                                                                                    | `None`                  |
| `concurrency`           | `int \| list[ConcurrencyExpression] \| None` | A list of concurrency expressions for the task. If an integer is provided, it is treated as a constant concurrency limit with a `GROUP_ROUND_ROBIN` strategy, which means that only `N` runs of the task may execute at any given time. | `None`                  |
| `wait_for`              | `list[Condition \| OrGroup] \| None`         | A list of conditions that must be met before the task can run.                                                                                                                                                                          | `None`                  |
| `skip_if`               | `list[Condition \| OrGroup] \| None`         | A list of conditions that, if met, will cause the task to be skipped.                                                                                                                                                                   | `None`                  |
| `cancel_if`             | `list[Condition \| OrGroup] \| None`         | A list of conditions that, if met, will cause the task to be canceled.                                                                                                                                                                  | `None`                  |

Returns:

| Type                                                                                                                   | Description                                |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| `Callable[[Callable[Concatenate[TWorkflowInput, DurableContext, P], R \| CoroutineLike[R]]], Task[TWorkflowInput, R]]` | A decorator which creates a `Task` object. |

#### `on_failure_task`

A decorator to transform a function into a Hatchet on-failure task that runs as the last step in a workflow that had at least one task fail.

Parameters:

| Name                  | Type                                         | Description                                                                                                                                                                                                                                        | Default                 |
| --------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `name`                | `str \| None`                                | The name of the on-failure task. If not specified, defaults to the name of the function being wrapped by the `on_failure_task` decorator.                                                                                                          | `None`                  |
| `schedule_timeout`    | `Duration`                                   | The maximum time to wait for the task to be scheduled. The run will be canceled if the task does not begin within this time.                                                                                                                       | `timedelta(minutes=5)`  |
| `execution_timeout`   | `Duration`                                   | The maximum time to wait for the task to complete. The run will be canceled if the task does not complete within this time.                                                                                                                        | `timedelta(seconds=60)` |
| `retries`             | `int`                                        | The number of times to retry the on-failure task before failing.                                                                                                                                                                                   | `0`                     |
| `rate_limits`         | `list[RateLimit] \| None`                    | A list of rate limit configurations for the on-failure task.                                                                                                                                                                                       | `None`                  |
| `backoff_factor`      | `float \| None`                              | The backoff factor for controlling exponential backoff in retries.                                                                                                                                                                                 | `None`                  |
| `backoff_max_seconds` | `int \| None`                                | The maximum number of seconds to allow retries with exponential backoff to continue.                                                                                                                                                               | `None`                  |
| `concurrency`         | `int \| list[ConcurrencyExpression] \| None` | A list of concurrency expressions for the on-failure task. If an integer is provided, it is treated as a constant concurrency limit with a `GROUP_ROUND_ROBIN` strategy, which means that only `N` runs of the task may execute at any given time. | `None`                  |

Returns:

| Type                                                                                                            | Description                                |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| `Callable[[Callable[Concatenate[TWorkflowInput, Context, P], R \| CoroutineLike[R]]], Task[TWorkflowInput, R]]` | A decorator which creates a `Task` object. |

#### `on_success_task`

A decorator to transform a function into a Hatchet on-success task that runs as the last step in a workflow that had all upstream tasks succeed.

Parameters:

| Name                  | Type                                         | Description                                                                                                                                                                                                                                        | Default                 |
| --------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `name`                | `str \| None`                                | The name of the on-success task. If not specified, defaults to the name of the function being wrapped by the `on_success_task` decorator.                                                                                                          | `None`                  |
| `schedule_timeout`    | `Duration`                                   | The maximum time to wait for the task to be scheduled. The run will be canceled if the task does not begin within this time.                                                                                                                       | `timedelta(minutes=5)`  |
| `execution_timeout`   | `Duration`                                   | The maximum time to wait for the task to complete. The run will be canceled if the task does not complete within this time.                                                                                                                        | `timedelta(seconds=60)` |
| `retries`             | `int`                                        | The number of times to retry the on-success task before failing                                                                                                                                                                                    | `0`                     |
| `rate_limits`         | `list[RateLimit] \| None`                    | A list of rate limit configurations for the on-success task.                                                                                                                                                                                       | `None`                  |
| `backoff_factor`      | `float \| None`                              | The backoff factor for controlling exponential backoff in retries.                                                                                                                                                                                 | `None`                  |
| `backoff_max_seconds` | `int \| None`                                | The maximum number of seconds to allow retries with exponential backoff to continue.                                                                                                                                                               | `None`                  |
| `concurrency`         | `int \| list[ConcurrencyExpression] \| None` | A list of concurrency expressions for the on-success task. If an integer is provided, it is treated as a constant concurrency limit with a `GROUP_ROUND_ROBIN` strategy, which means that only `N` runs of the task may execute at any given time. | `None`                  |

Returns:

| Type                                                                                                            | Description                              |
| --------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `Callable[[Callable[Concatenate[TWorkflowInput, Context, P], R \| CoroutineLike[R]]], Task[TWorkflowInput, R]]` | A decorator which creates a Task object. |

#### `run`

Run the workflow synchronously and wait for it to complete.

This method triggers a workflow run, blocks until completion, and returns the final result.

Parameters:

| Name      | Type                     | Description                                                                     | Default                              |
| --------- | ------------------------ | ------------------------------------------------------------------------------- | ------------------------------------ |
| `input`   | `TWorkflowInput`         | The input data for the workflow, must match the workflow's input type.          | `cast(TWorkflowInput, EmptyModel())` |
| `options` | `TriggerWorkflowOptions` | Additional options for workflow execution like metadata and parent workflow ID. | `TriggerWorkflowOptions()`           |

Returns:

| Type             | Description                                           |
| ---------------- | ----------------------------------------------------- |
| `dict[str, Any]` | The result of the workflow execution as a dictionary. |

#### `aio_run`

Run the workflow asynchronously and wait for it to complete.

This method triggers a workflow run, awaits until completion, and returns the final result.

Parameters:

| Name      | Type                     | Description                                                                     | Default                              |
| --------- | ------------------------ | ------------------------------------------------------------------------------- | ------------------------------------ |
| `input`   | `TWorkflowInput`         | The input data for the workflow, must match the workflow's input type.          | `cast(TWorkflowInput, EmptyModel())` |
| `options` | `TriggerWorkflowOptions` | Additional options for workflow execution like metadata and parent workflow ID. | `TriggerWorkflowOptions()`           |

Returns:

| Type             | Description                                           |
| ---------------- | ----------------------------------------------------- |
| `dict[str, Any]` | The result of the workflow execution as a dictionary. |

#### `run_no_wait`

Synchronously trigger a workflow run without waiting for it to complete. This method is useful for starting a workflow run and immediately returning a reference to the run without blocking while the workflow runs.

Parameters:

| Name      | Type                     | Description                                | Default                              |
| --------- | ------------------------ | ------------------------------------------ | ------------------------------------ |
| `input`   | `TWorkflowInput`         | The input data for the workflow.           | `cast(TWorkflowInput, EmptyModel())` |
| `options` | `TriggerWorkflowOptions` | Additional options for workflow execution. | `TriggerWorkflowOptions()`           |

Returns:

| Type             | Description                                                               |
| ---------------- | ------------------------------------------------------------------------- |
| `WorkflowRunRef` | A `WorkflowRunRef` object representing the reference to the workflow run. |

#### `aio_run_no_wait`

Asynchronously trigger a workflow run without waiting for it to complete. This method is useful for starting a workflow run and immediately returning a reference to the run without blocking while the workflow runs.

Parameters:

| Name      | Type                     | Description                                | Default                              |
| --------- | ------------------------ | ------------------------------------------ | ------------------------------------ |
| `input`   | `TWorkflowInput`         | The input data for the workflow.           | `cast(TWorkflowInput, EmptyModel())` |
| `options` | `TriggerWorkflowOptions` | Additional options for workflow execution. | `TriggerWorkflowOptions()`           |

Returns:

| Type             | Description                                                               |
| ---------------- | ------------------------------------------------------------------------- |
| `WorkflowRunRef` | A `WorkflowRunRef` object representing the reference to the workflow run. |

#### `run_many`

Run a workflow in bulk and wait for all runs to complete. This method triggers multiple workflow runs, blocks until all of them complete, and returns the final results.

Parameters:

| Name                | Type                             | Description                                                                                     | Default    |
| ------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------- | ---------- |
| `workflows`         | `list[WorkflowRunTriggerConfig]` | A list of `WorkflowRunTriggerConfig` objects, each representing a workflow run to be triggered. | _required_ |
| `return_exceptions` | `bool`                           | If `True`, exceptions will be returned as part of the results instead of raising them.          | `False`    |

Returns:

| Type                                                            | Description                              |
| --------------------------------------------------------------- | ---------------------------------------- |
| `list[dict[str, Any]] \| list[dict[str, Any] \| BaseException]` | A list of results for each workflow run. |

#### `aio_run_many`

Run a workflow in bulk and wait for all runs to complete. This method triggers multiple workflow runs, blocks until all of them complete, and returns the final results.

Parameters:

| Name                | Type                             | Description                                                                                     | Default    |
| ------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------- | ---------- |
| `workflows`         | `list[WorkflowRunTriggerConfig]` | A list of `WorkflowRunTriggerConfig` objects, each representing a workflow run to be triggered. | _required_ |
| `return_exceptions` | `bool`                           | If `True`, exceptions will be returned as part of the results instead of raising them.          | `False`    |

Returns:

| Type                                                            | Description                              |
| --------------------------------------------------------------- | ---------------------------------------- |
| `list[dict[str, Any]] \| list[dict[str, Any] \| BaseException]` | A list of results for each workflow run. |

#### `run_many_no_wait`

Run a workflow in bulk without waiting for all runs to complete.

This method triggers multiple workflow runs and immediately returns a list of references to the runs without blocking while the workflows run.

Parameters:

| Name        | Type                             | Description                                                                                     | Default    |
| ----------- | -------------------------------- | ----------------------------------------------------------------------------------------------- | ---------- |
| `workflows` | `list[WorkflowRunTriggerConfig]` | A list of `WorkflowRunTriggerConfig` objects, each representing a workflow run to be triggered. | _required_ |

Returns:

| Type                   | Description                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------ |
| `list[WorkflowRunRef]` | A list of `WorkflowRunRef` objects, each representing a reference to a workflow run. |

#### `aio_run_many_no_wait`

Run a workflow in bulk without waiting for all runs to complete.

This method triggers multiple workflow runs and immediately returns a list of references to the runs without blocking while the workflows run.

Parameters:

| Name        | Type                             | Description                                                                                     | Default    |
| ----------- | -------------------------------- | ----------------------------------------------------------------------------------------------- | ---------- |
| `workflows` | `list[WorkflowRunTriggerConfig]` | A list of `WorkflowRunTriggerConfig` objects, each representing a workflow run to be triggered. | _required_ |

Returns:

| Type                   | Description                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------ |
| `list[WorkflowRunRef]` | A list of `WorkflowRunRef` objects, each representing a reference to a workflow run. |

#### `schedule`

Schedule a workflow to run at a specific time.

Parameters:

| Name      | Type                             | Description                                 | Default                              |
| --------- | -------------------------------- | ------------------------------------------- | ------------------------------------ |
| `run_at`  | `datetime`                       | The time at which to schedule the workflow. | _required_                           |
| `input`   | `TWorkflowInput`                 | The input data for the workflow.            | `cast(TWorkflowInput, EmptyModel())` |
| `options` | `ScheduleTriggerWorkflowOptions` | Additional options for workflow execution.  | `ScheduleTriggerWorkflowOptions()`   |

Returns:

| Type              | Description                                                     |
| ----------------- | --------------------------------------------------------------- |
| `WorkflowVersion` | A `WorkflowVersion` object representing the scheduled workflow. |

#### `aio_schedule`

Schedule a workflow to run at a specific time.

Parameters:

| Name      | Type                             | Description                                 | Default                              |
| --------- | -------------------------------- | ------------------------------------------- | ------------------------------------ |
| `run_at`  | `datetime`                       | The time at which to schedule the workflow. | _required_                           |
| `input`   | `TWorkflowInput`                 | The input data for the workflow.            | `cast(TWorkflowInput, EmptyModel())` |
| `options` | `ScheduleTriggerWorkflowOptions` | Additional options for workflow execution.  | `ScheduleTriggerWorkflowOptions()`   |

Returns:

| Type              | Description                                                     |
| ----------------- | --------------------------------------------------------------- |
| `WorkflowVersion` | A `WorkflowVersion` object representing the scheduled workflow. |

#### `create_cron`

Create a cron job for the workflow.

Parameters:

| Name                  | Type                              | Description                                                       | Default                              |
| --------------------- | --------------------------------- | ----------------------------------------------------------------- | ------------------------------------ |
| `cron_name`           | `str`                             | The name of the cron job.                                         | _required_                           |
| `expression`          | `str`                             | The cron expression that defines the schedule for the cron job.   | _required_                           |
| `input`               | `TWorkflowInput`                  | The input data for the workflow.                                  | `cast(TWorkflowInput, EmptyModel())` |
| `additional_metadata` | `JSONSerializableMapping \| None` | Additional metadata for the cron job.                             | `None`                               |
| `priority`            | `int \| None`                     | The priority of the cron job. Must be between 1 and 3, inclusive. | `None`                               |

Returns:

| Type            | Description                                                 |
| --------------- | ----------------------------------------------------------- |
| `CronWorkflows` | A `CronWorkflows` object representing the created cron job. |

#### `aio_create_cron`

Create a cron job for the workflow.

Parameters:

| Name                  | Type                              | Description                                                       | Default                              |
| --------------------- | --------------------------------- | ----------------------------------------------------------------- | ------------------------------------ |
| `cron_name`           | `str`                             | The name of the cron job.                                         | _required_                           |
| `expression`          | `str`                             | The cron expression that defines the schedule for the cron job.   | _required_                           |
| `input`               | `TWorkflowInput`                  | The input data for the workflow.                                  | `cast(TWorkflowInput, EmptyModel())` |
| `additional_metadata` | `JSONSerializableMapping \| None` | Additional metadata for the cron job.                             | `None`                               |
| `priority`            | `int \| None`                     | The priority of the cron job. Must be between 1 and 3, inclusive. | `None`                               |

Returns:

| Type            | Description                                                 |
| --------------- | ----------------------------------------------------------- |
| `CronWorkflows` | A `CronWorkflows` object representing the created cron job. |

#### `create_bulk_run_item`

Create a bulk run item for the workflow. This is intended to be used in conjunction with the various `run_many` methods.

Parameters:

| Name      | Type                     | Description                                                                                                 | Default                              |
| --------- | ------------------------ | ----------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| `input`   | `TWorkflowInput`         | The input data for the workflow.                                                                            | `cast(TWorkflowInput, EmptyModel())` |
| `key`     | `str \| None`            | The key for the workflow run. This is used to identify the run in the bulk operation and for deduplication. | `None`                               |
| `options` | `TriggerWorkflowOptions` | Additional options for the workflow run.                                                                    | `TriggerWorkflowOptions()`           |

Returns:

| Type                       | Description                                                                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `WorkflowRunTriggerConfig` | A `WorkflowRunTriggerConfig` object that can be used to trigger the workflow run, which you then pass into the `run_many` methods. |

#### `list_runs`

List runs of the workflow.

Parameters:

| Name                           | Type                         | Description                                 | Default |
| ------------------------------ | ---------------------------- | ------------------------------------------- | ------- |
| `since`                        | `datetime \| None`           | The start time for the runs to be listed.   | `None`  |
| `until`                        | `datetime \| None`           | The end time for the runs to be listed.     | `None`  |
| `limit`                        | `int`                        | The maximum number of runs to be listed.    | `100`   |
| `offset`                       | `int \| None`                | The offset for pagination.                  | `None`  |
| `statuses`                     | `list[V1TaskStatus] \| None` | The statuses of the runs to be listed.      | `None`  |
| `additional_metadata`          | `dict[str, str] \| None`     | Additional metadata for filtering the runs. | `None`  |
| `worker_id`                    | `str \| None`                | The ID of the worker that ran the tasks.    | `None`  |
| `parent_task_external_id`      | `str \| None`                | The external ID of the parent task.         | `None`  |
| `only_tasks`                   | `bool`                       | Whether to list only task runs.             | `False` |
| `triggering_event_external_id` | `str \| None`                | The event id that triggered the task run.   | `None`  |

Returns:

| Type                  | Description                                                              |
| --------------------- | ------------------------------------------------------------------------ |
| `list[V1TaskSummary]` | A list of `V1TaskSummary` objects representing the runs of the workflow. |

#### `aio_list_runs`

List runs of the workflow.

Parameters:

| Name                           | Type                         | Description                                 | Default |
| ------------------------------ | ---------------------------- | ------------------------------------------- | ------- |
| `since`                        | `datetime \| None`           | The start time for the runs to be listed.   | `None`  |
| `until`                        | `datetime \| None`           | The end time for the runs to be listed.     | `None`  |
| `limit`                        | `int`                        | The maximum number of runs to be listed.    | `100`   |
| `offset`                       | `int \| None`                | The offset for pagination.                  | `None`  |
| `statuses`                     | `list[V1TaskStatus] \| None` | The statuses of the runs to be listed.      | `None`  |
| `additional_metadata`          | `dict[str, str] \| None`     | Additional metadata for filtering the runs. | `None`  |
| `worker_id`                    | `str \| None`                | The ID of the worker that ran the tasks.    | `None`  |
| `parent_task_external_id`      | `str \| None`                | The external ID of the parent task.         | `None`  |
| `only_tasks`                   | `bool`                       | Whether to list only task runs.             | `False` |
| `triggering_event_external_id` | `str \| None`                | The event id that triggered the task run.   | `None`  |

Returns:

| Type                  | Description                                                              |
| --------------------- | ------------------------------------------------------------------------ |
| `list[V1TaskSummary]` | A list of `V1TaskSummary` objects representing the runs of the workflow. |

#### `create_filter`

Create a new filter.

Parameters:

| Name         | Type                              | Description                                | Default    |
| ------------ | --------------------------------- | ------------------------------------------ | ---------- |
| `expression` | `str`                             | The expression to evaluate for the filter. | _required_ |
| `scope`      | `str`                             | The scope for the filter.                  | _required_ |
| `payload`    | `JSONSerializableMapping \| None` | The payload to send with the filter.       | `None`     |

Returns:

| Type       | Description         |
| ---------- | ------------------- |
| `V1Filter` | The created filter. |

#### `aio_create_filter`

Create a new filter.

Parameters:

| Name         | Type                              | Description                                | Default    |
| ------------ | --------------------------------- | ------------------------------------------ | ---------- |
| `expression` | `str`                             | The expression to evaluate for the filter. | _required_ |
| `scope`      | `str`                             | The scope for the filter.                  | _required_ |
| `payload`    | `JSONSerializableMapping \| None` | The payload to send with the filter.       | `None`     |

Returns:

| Type       | Description         |
| ---------- | ------------------- |
| `V1Filter` | The created filter. |

## Task

Bases: `Generic[TWorkflowInput, R]`

Methods:

| Name           | Description                                                                    |
| -------------- | ------------------------------------------------------------------------------ |
| `mock_run`     | Mimic the execution of a task. This method is intended to be used to unit test |
| `aio_mock_run` | Mimic the execution of a task. This method is intended to be used to unit test |

### Functions

#### `mock_run`

Mimic the execution of a task. This method is intended to be used to unit test tasks without needing to interact with the Hatchet engine. Use `mock_run` for sync tasks and `aio_mock_run` for async tasks.

Parameters:

| Name                  | Type                                         | Description                                                                                                                                                                                                                                                                                                                                                                                               | Default |
| --------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `input`               | `TWorkflowInput \| None`                     | The input to the task.                                                                                                                                                                                                                                                                                                                                                                                    | `None`  |
| `additional_metadata` | `JSONSerializableMapping \| None`            | Additional metadata to attach to the task.                                                                                                                                                                                                                                                                                                                                                                | `None`  |
| `parent_outputs`      | `dict[str, JSONSerializableMapping] \| None` | Outputs from parent tasks, if any. This is useful for mimicking DAG functionality. For instance, if you have a task `step_2` that has a `parent` which is `step_1`, you can pass `parent_outputs={"step_1": {"result": "Hello, world!"}}` to `step_2.mock_run()` to be able to access `ctx.task_output(step_1)` in `step_2`.                                                                              | `None`  |
| `retry_count`         | `int`                                        | The number of times the task has been retried.                                                                                                                                                                                                                                                                                                                                                            | `0`     |
| `lifespan`            | `Any`                                        | The lifespan to be used in the task, which is useful if one was set on the worker. This will allow you to access `ctx.lifespan` inside of your task.                                                                                                                                                                                                                                                      | `None`  |
| `dependencies`        | `dict[str, Any] \| None`                     | Dependencies to be injected into the task. This is useful for tasks that have dependencies defined using `Depends`. **IMPORTANT**: You must pass the dependencies _directly_, **not** the `Depends` objects themselves. For example, if you have a task that has a dependency `config: Annotated[str, Depends(get_config)]`, you should pass `dependencies={"config": "config_value"}` to `aio_mock_run`. | `None`  |

Returns:

| Type | Description             |
| ---- | ----------------------- |
| `R`  | The output of the task. |

Raises:

| Type        | Description                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------- |
| `TypeError` | If the task is an async function and `mock_run` is called, or if the task is a sync function and `aio_mock_run` is called. |

#### `aio_mock_run`

Mimic the execution of a task. This method is intended to be used to unit test tasks without needing to interact with the Hatchet engine. Use `mock_run` for sync tasks and `aio_mock_run` for async tasks.

Parameters:

| Name                  | Type                                         | Description                                                                                                                                                                                                                                                                                                                                                                                               | Default |
| --------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `input`               | `TWorkflowInput \| None`                     | The input to the task.                                                                                                                                                                                                                                                                                                                                                                                    | `None`  |
| `additional_metadata` | `JSONSerializableMapping \| None`            | Additional metadata to attach to the task.                                                                                                                                                                                                                                                                                                                                                                | `None`  |
| `parent_outputs`      | `dict[str, JSONSerializableMapping] \| None` | Outputs from parent tasks, if any. This is useful for mimicking DAG functionality. For instance, if you have a task `step_2` that has a `parent` which is `step_1`, you can pass `parent_outputs={"step_1": {"result": "Hello, world!"}}` to `step_2.mock_run()` to be able to access `ctx.task_output(step_1)` in `step_2`.                                                                              | `None`  |
| `retry_count`         | `int`                                        | The number of times the task has been retried.                                                                                                                                                                                                                                                                                                                                                            | `0`     |
| `lifespan`            | `Any`                                        | The lifespan to be used in the task, which is useful if one was set on the worker. This will allow you to access `ctx.lifespan` inside of your task.                                                                                                                                                                                                                                                      | `None`  |
| `dependencies`        | `dict[str, Any] \| None`                     | Dependencies to be injected into the task. This is useful for tasks that have dependencies defined using `Depends`. **IMPORTANT**: You must pass the dependencies _directly_, **not** the `Depends` objects themselves. For example, if you have a task that has a dependency `config: Annotated[str, Depends(get_config)]`, you should pass `dependencies={"config": "config_value"}` to `aio_mock_run`. | `None`  |

Returns:

| Type | Description             |
| ---- | ----------------------- |
| `R`  | The output of the task. |

Raises:

| Type        | Description                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------- |
| `TypeError` | If the task is an async function and `mock_run` is called, or if the task is a sync function and `aio_mock_run` is called. |

## Standalone

Bases: `BaseWorkflow[TWorkflowInput]`, `Generic[TWorkflowInput, R]`

Methods:

| Name                   | Description                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `run`                  | Run the workflow synchronously and wait for it to complete.                                                              |
| `aio_run`              | Run the workflow asynchronously and wait for it to complete.                                                             |
| `run_no_wait`          | Trigger a workflow run without waiting for it to complete.                                                               |
| `aio_run_no_wait`      | Asynchronously trigger a workflow run without waiting for it to complete.                                                |
| `run_many`             | Run a workflow in bulk and wait for all runs to complete.                                                                |
| `aio_run_many`         | Run a workflow in bulk and wait for all runs to complete.                                                                |
| `run_many_no_wait`     | Run a workflow in bulk without waiting for all runs to complete.                                                         |
| `aio_run_many_no_wait` | Run a workflow in bulk without waiting for all runs to complete.                                                         |
| `schedule`             | Schedule a workflow to run at a specific time.                                                                           |
| `aio_schedule`         | Schedule a workflow to run at a specific time.                                                                           |
| `create_cron`          | Create a cron job for the workflow.                                                                                      |
| `aio_create_cron`      | Create a cron job for the workflow.                                                                                      |
| `create_bulk_run_item` | Create a bulk run item for the workflow. This is intended to be used in conjunction with the various `run_many` methods. |
| `list_runs`            | List runs of the workflow.                                                                                               |
| `aio_list_runs`        | List runs of the workflow.                                                                                               |
| `create_filter`        | Create a new filter.                                                                                                     |
| `aio_create_filter`    | Create a new filter.                                                                                                     |
| `delete`               | Permanently delete the workflow.                                                                                         |
| `aio_delete`           | Permanently delete the workflow.                                                                                         |
| `get_run_ref`          | Get a reference to a task run by its run ID.                                                                             |
| `get_result`           | Get the result of a task run by its run ID.                                                                              |
| `aio_get_result`       | Get the result of a task run by its run ID.                                                                              |
| `mock_run`             | Mimic the execution of a task. This method is intended to be used to unit test                                           |
| `aio_mock_run`         | Mimic the execution of a task. This method is intended to be used to unit test                                           |

### Functions

#### `run`

Run the workflow synchronously and wait for it to complete.

This method triggers a workflow run, blocks until completion, and returns the extracted result.

Parameters:

| Name      | Type                     | Description                                | Default                              |
| --------- | ------------------------ | ------------------------------------------ | ------------------------------------ |
| `input`   | `TWorkflowInput`         | The input data for the workflow.           | `cast(TWorkflowInput, EmptyModel())` |
| `options` | `TriggerWorkflowOptions` | Additional options for workflow execution. | `TriggerWorkflowOptions()`           |

Returns:

| Type | Description                                     |
| ---- | ----------------------------------------------- |
| `R`  | The extracted result of the workflow execution. |

#### `aio_run`

Run the workflow asynchronously and wait for it to complete.

This method triggers a workflow run, awaits until completion, and returns the extracted result.

Parameters:

| Name      | Type                     | Description                                                                     | Default                              |
| --------- | ------------------------ | ------------------------------------------------------------------------------- | ------------------------------------ |
| `input`   | `TWorkflowInput`         | The input data for the workflow, must match the workflow's input type.          | `cast(TWorkflowInput, EmptyModel())` |
| `options` | `TriggerWorkflowOptions` | Additional options for workflow execution like metadata and parent workflow ID. | `TriggerWorkflowOptions()`           |

Returns:

| Type | Description                                     |
| ---- | ----------------------------------------------- |
| `R`  | The extracted result of the workflow execution. |

#### `run_no_wait`

Trigger a workflow run without waiting for it to complete.

This method triggers a workflow run and immediately returns a reference to the run without blocking while the workflow runs.

Parameters:

| Name      | Type                     | Description                                                                     | Default                              |
| --------- | ------------------------ | ------------------------------------------------------------------------------- | ------------------------------------ |
| `input`   | `TWorkflowInput`         | The input data for the workflow, must match the workflow's input type.          | `cast(TWorkflowInput, EmptyModel())` |
| `options` | `TriggerWorkflowOptions` | Additional options for workflow execution like metadata and parent workflow ID. | `TriggerWorkflowOptions()`           |

Returns:

| Type                            | Description                                                           |
| ------------------------------- | --------------------------------------------------------------------- |
| `TaskRunRef[TWorkflowInput, R]` | A `TaskRunRef` object representing the reference to the workflow run. |

#### `aio_run_no_wait`

Asynchronously trigger a workflow run without waiting for it to complete. This method is useful for starting a workflow run and immediately returning a reference to the run without blocking while the workflow runs.

Parameters:

| Name      | Type                     | Description                                | Default                              |
| --------- | ------------------------ | ------------------------------------------ | ------------------------------------ |
| `input`   | `TWorkflowInput`         | The input data for the workflow.           | `cast(TWorkflowInput, EmptyModel())` |
| `options` | `TriggerWorkflowOptions` | Additional options for workflow execution. | `TriggerWorkflowOptions()`           |

Returns:

| Type                            | Description                                                           |
| ------------------------------- | --------------------------------------------------------------------- |
| `TaskRunRef[TWorkflowInput, R]` | A `TaskRunRef` object representing the reference to the workflow run. |

#### `run_many`

Run a workflow in bulk and wait for all runs to complete. This method triggers multiple workflow runs, blocks until all of them complete, and returns the final results.

Parameters:

| Name                | Type                             | Description                                                                                     | Default    |
| ------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------- | ---------- |
| `workflows`         | `list[WorkflowRunTriggerConfig]` | A list of `WorkflowRunTriggerConfig` objects, each representing a workflow run to be triggered. | _required_ |
| `return_exceptions` | `bool`                           | If `True`, exceptions will be returned as part of the results instead of raising them.          | `False`    |

Returns:

| Type                                  | Description                              |
| ------------------------------------- | ---------------------------------------- |
| `list[R] \| list[R \| BaseException]` | A list of results for each workflow run. |

#### `aio_run_many`

Run a workflow in bulk and wait for all runs to complete. This method triggers multiple workflow runs, blocks until all of them complete, and returns the final results.

Parameters:

| Name                | Type                             | Description                                                                                     | Default    |
| ------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------- | ---------- |
| `workflows`         | `list[WorkflowRunTriggerConfig]` | A list of `WorkflowRunTriggerConfig` objects, each representing a workflow run to be triggered. | _required_ |
| `return_exceptions` | `bool`                           | If `True`, exceptions will be returned as part of the results instead of raising them.          | `False`    |

Returns:

| Type                                  | Description                              |
| ------------------------------------- | ---------------------------------------- |
| `list[R] \| list[R \| BaseException]` | A list of results for each workflow run. |

#### `run_many_no_wait`

Run a workflow in bulk without waiting for all runs to complete.

This method triggers multiple workflow runs and immediately returns a list of references to the runs without blocking while the workflows run.

Parameters:

| Name        | Type                             | Description                                                                                     | Default    |
| ----------- | -------------------------------- | ----------------------------------------------------------------------------------------------- | ---------- |
| `workflows` | `list[WorkflowRunTriggerConfig]` | A list of `WorkflowRunTriggerConfig` objects, each representing a workflow run to be triggered. | _required_ |

Returns:

| Type                                  | Description                                                                          |
| ------------------------------------- | ------------------------------------------------------------------------------------ |
| `list[TaskRunRef[TWorkflowInput, R]]` | A list of `WorkflowRunRef` objects, each representing a reference to a workflow run. |

#### `aio_run_many_no_wait`

Run a workflow in bulk without waiting for all runs to complete.

This method triggers multiple workflow runs and immediately returns a list of references to the runs without blocking while the workflows run.

Parameters:

| Name        | Type                             | Description                                                                                     | Default    |
| ----------- | -------------------------------- | ----------------------------------------------------------------------------------------------- | ---------- |
| `workflows` | `list[WorkflowRunTriggerConfig]` | A list of `WorkflowRunTriggerConfig` objects, each representing a workflow run to be triggered. | _required_ |

Returns:

| Type                                  | Description                                                                          |
| ------------------------------------- | ------------------------------------------------------------------------------------ |
| `list[TaskRunRef[TWorkflowInput, R]]` | A list of `WorkflowRunRef` objects, each representing a reference to a workflow run. |

#### `schedule`

Schedule a workflow to run at a specific time.

Parameters:

| Name      | Type                             | Description                                 | Default                              |
| --------- | -------------------------------- | ------------------------------------------- | ------------------------------------ |
| `run_at`  | `datetime`                       | The time at which to schedule the workflow. | _required_                           |
| `input`   | `TWorkflowInput`                 | The input data for the workflow.            | `cast(TWorkflowInput, EmptyModel())` |
| `options` | `ScheduleTriggerWorkflowOptions` | Additional options for workflow execution.  | `ScheduleTriggerWorkflowOptions()`   |

Returns:

| Type              | Description                                                     |
| ----------------- | --------------------------------------------------------------- |
| `WorkflowVersion` | A `WorkflowVersion` object representing the scheduled workflow. |

#### `aio_schedule`

Schedule a workflow to run at a specific time.

Parameters:

| Name      | Type                             | Description                                 | Default                              |
| --------- | -------------------------------- | ------------------------------------------- | ------------------------------------ |
| `run_at`  | `datetime`                       | The time at which to schedule the workflow. | _required_                           |
| `input`   | `TWorkflowInput`                 | The input data for the workflow.            | `cast(TWorkflowInput, EmptyModel())` |
| `options` | `ScheduleTriggerWorkflowOptions` | Additional options for workflow execution.  | `ScheduleTriggerWorkflowOptions()`   |

Returns:

| Type              | Description                                                     |
| ----------------- | --------------------------------------------------------------- |
| `WorkflowVersion` | A `WorkflowVersion` object representing the scheduled workflow. |

#### `create_cron`

Create a cron job for the workflow.

Parameters:

| Name                  | Type                              | Description                                                       | Default                              |
| --------------------- | --------------------------------- | ----------------------------------------------------------------- | ------------------------------------ |
| `cron_name`           | `str`                             | The name of the cron job.                                         | _required_                           |
| `expression`          | `str`                             | The cron expression that defines the schedule for the cron job.   | _required_                           |
| `input`               | `TWorkflowInput`                  | The input data for the workflow.                                  | `cast(TWorkflowInput, EmptyModel())` |
| `additional_metadata` | `JSONSerializableMapping \| None` | Additional metadata for the cron job.                             | `None`                               |
| `priority`            | `int \| None`                     | The priority of the cron job. Must be between 1 and 3, inclusive. | `None`                               |

Returns:

| Type            | Description                                                 |
| --------------- | ----------------------------------------------------------- |
| `CronWorkflows` | A `CronWorkflows` object representing the created cron job. |

#### `aio_create_cron`

Create a cron job for the workflow.

Parameters:

| Name                  | Type                              | Description                                                       | Default                              |
| --------------------- | --------------------------------- | ----------------------------------------------------------------- | ------------------------------------ |
| `cron_name`           | `str`                             | The name of the cron job.                                         | _required_                           |
| `expression`          | `str`                             | The cron expression that defines the schedule for the cron job.   | _required_                           |
| `input`               | `TWorkflowInput`                  | The input data for the workflow.                                  | `cast(TWorkflowInput, EmptyModel())` |
| `additional_metadata` | `JSONSerializableMapping \| None` | Additional metadata for the cron job.                             | `None`                               |
| `priority`            | `int \| None`                     | The priority of the cron job. Must be between 1 and 3, inclusive. | `None`                               |

Returns:

| Type            | Description                                                 |
| --------------- | ----------------------------------------------------------- |
| `CronWorkflows` | A `CronWorkflows` object representing the created cron job. |

#### `create_bulk_run_item`

Create a bulk run item for the workflow. This is intended to be used in conjunction with the various `run_many` methods.

Parameters:

| Name      | Type                     | Description                                                                                                 | Default                              |
| --------- | ------------------------ | ----------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| `input`   | `TWorkflowInput`         | The input data for the workflow.                                                                            | `cast(TWorkflowInput, EmptyModel())` |
| `key`     | `str \| None`            | The key for the workflow run. This is used to identify the run in the bulk operation and for deduplication. | `None`                               |
| `options` | `TriggerWorkflowOptions` | Additional options for the workflow run.                                                                    | `TriggerWorkflowOptions()`           |

Returns:

| Type                       | Description                                                                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `WorkflowRunTriggerConfig` | A `WorkflowRunTriggerConfig` object that can be used to trigger the workflow run, which you then pass into the `run_many` methods. |

#### `list_runs`

List runs of the workflow.

Parameters:

| Name                           | Type                         | Description                                 | Default |
| ------------------------------ | ---------------------------- | ------------------------------------------- | ------- |
| `since`                        | `datetime \| None`           | The start time for the runs to be listed.   | `None`  |
| `until`                        | `datetime \| None`           | The end time for the runs to be listed.     | `None`  |
| `limit`                        | `int`                        | The maximum number of runs to be listed.    | `100`   |
| `offset`                       | `int \| None`                | The offset for pagination.                  | `None`  |
| `statuses`                     | `list[V1TaskStatus] \| None` | The statuses of the runs to be listed.      | `None`  |
| `additional_metadata`          | `dict[str, str] \| None`     | Additional metadata for filtering the runs. | `None`  |
| `worker_id`                    | `str \| None`                | The ID of the worker that ran the tasks.    | `None`  |
| `parent_task_external_id`      | `str \| None`                | The external ID of the parent task.         | `None`  |
| `only_tasks`                   | `bool`                       | Whether to list only task runs.             | `False` |
| `triggering_event_external_id` | `str \| None`                | The event id that triggered the task run.   | `None`  |

Returns:

| Type                  | Description                                                              |
| --------------------- | ------------------------------------------------------------------------ |
| `list[V1TaskSummary]` | A list of `V1TaskSummary` objects representing the runs of the workflow. |

#### `aio_list_runs`

List runs of the workflow.

Parameters:

| Name                           | Type                         | Description                                 | Default |
| ------------------------------ | ---------------------------- | ------------------------------------------- | ------- |
| `since`                        | `datetime \| None`           | The start time for the runs to be listed.   | `None`  |
| `until`                        | `datetime \| None`           | The end time for the runs to be listed.     | `None`  |
| `limit`                        | `int`                        | The maximum number of runs to be listed.    | `100`   |
| `offset`                       | `int \| None`                | The offset for pagination.                  | `None`  |
| `statuses`                     | `list[V1TaskStatus] \| None` | The statuses of the runs to be listed.      | `None`  |
| `additional_metadata`          | `dict[str, str] \| None`     | Additional metadata for filtering the runs. | `None`  |
| `worker_id`                    | `str \| None`                | The ID of the worker that ran the tasks.    | `None`  |
| `parent_task_external_id`      | `str \| None`                | The external ID of the parent task.         | `None`  |
| `only_tasks`                   | `bool`                       | Whether to list only task runs.             | `False` |
| `triggering_event_external_id` | `str \| None`                | The event id that triggered the task run.   | `None`  |

Returns:

| Type                  | Description                                                              |
| --------------------- | ------------------------------------------------------------------------ |
| `list[V1TaskSummary]` | A list of `V1TaskSummary` objects representing the runs of the workflow. |

#### `create_filter`

Create a new filter.

Parameters:

| Name         | Type                              | Description                                | Default    |
| ------------ | --------------------------------- | ------------------------------------------ | ---------- |
| `expression` | `str`                             | The expression to evaluate for the filter. | _required_ |
| `scope`      | `str`                             | The scope for the filter.                  | _required_ |
| `payload`    | `JSONSerializableMapping \| None` | The payload to send with the filter.       | `None`     |

Returns:

| Type       | Description         |
| ---------- | ------------------- |
| `V1Filter` | The created filter. |

#### `aio_create_filter`

Create a new filter.

Parameters:

| Name         | Type                              | Description                                | Default    |
| ------------ | --------------------------------- | ------------------------------------------ | ---------- |
| `expression` | `str`                             | The expression to evaluate for the filter. | _required_ |
| `scope`      | `str`                             | The scope for the filter.                  | _required_ |
| `payload`    | `JSONSerializableMapping \| None` | The payload to send with the filter.       | `None`     |

Returns:

| Type       | Description         |
| ---------- | ------------------- |
| `V1Filter` | The created filter. |

#### `delete`

Permanently delete the workflow.

**DANGEROUS: This will delete a workflow and all of its data**

#### `aio_delete`

Permanently delete the workflow.

**DANGEROUS: This will delete a workflow and all of its data**

#### `get_run_ref`

Get a reference to a task run by its run ID.

Parameters:

| Name     | Type  | Description                                 | Default    |
| -------- | ----- | ------------------------------------------- | ---------- |
| `run_id` | `str` | The ID of the run to get the reference for. | _required_ |

Returns:

| Type                            | Description                                                       |
| ------------------------------- | ----------------------------------------------------------------- |
| `TaskRunRef[TWorkflowInput, R]` | A `TaskRunRef` object representing the reference to the task run. |

#### `get_result`

Get the result of a task run by its run ID.

Parameters:

| Name     | Type  | Description                              | Default    |
| -------- | ----- | ---------------------------------------- | ---------- |
| `run_id` | `str` | The ID of the run to get the result for. | _required_ |

Returns:

| Type | Description                 |
| ---- | --------------------------- |
| `R`  | The result of the task run. |

#### `aio_get_result`

Get the result of a task run by its run ID.

Parameters:

| Name     | Type  | Description                              | Default    |
| -------- | ----- | ---------------------------------------- | ---------- |
| `run_id` | `str` | The ID of the run to get the result for. | _required_ |

Returns:

| Type | Description                 |
| ---- | --------------------------- |
| `R`  | The result of the task run. |

#### `mock_run`

Mimic the execution of a task. This method is intended to be used to unit test tasks without needing to interact with the Hatchet engine. Use `mock_run` for sync tasks and `aio_mock_run` for async tasks.

Parameters:

| Name                  | Type                                         | Description                                                                                                                                                                                                                                                                                                                                                                                               | Default |
| --------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `input`               | `TWorkflowInput \| None`                     | The input to the task.                                                                                                                                                                                                                                                                                                                                                                                    | `None`  |
| `additional_metadata` | `JSONSerializableMapping \| None`            | Additional metadata to attach to the task.                                                                                                                                                                                                                                                                                                                                                                | `None`  |
| `parent_outputs`      | `dict[str, JSONSerializableMapping] \| None` | Outputs from parent tasks, if any. This is useful for mimicking DAG functionality. For instance, if you have a task `step_2` that has a `parent` which is `step_1`, you can pass `parent_outputs={"step_1": {"result": "Hello, world!"}}` to `step_2.mock_run()` to be able to access `ctx.task_output(step_1)` in `step_2`.                                                                              | `None`  |
| `retry_count`         | `int`                                        | The number of times the task has been retried.                                                                                                                                                                                                                                                                                                                                                            | `0`     |
| `lifespan`            | `Any`                                        | The lifespan to be used in the task, which is useful if one was set on the worker. This will allow you to access `ctx.lifespan` inside of your task.                                                                                                                                                                                                                                                      | `None`  |
| `dependencies`        | `dict[str, Any] \| None`                     | Dependencies to be injected into the task. This is useful for tasks that have dependencies defined using `Depends`. **IMPORTANT**: You must pass the dependencies _directly_, **not** the `Depends` objects themselves. For example, if you have a task that has a dependency `config: Annotated[str, Depends(get_config)]`, you should pass `dependencies={"config": "config_value"}` to `aio_mock_run`. | `None`  |

Returns:

| Type | Description             |
| ---- | ----------------------- |
| `R`  | The output of the task. |

#### `aio_mock_run`

Mimic the execution of a task. This method is intended to be used to unit test tasks without needing to interact with the Hatchet engine. Use `mock_run` for sync tasks and `aio_mock_run` for async tasks.

Parameters:

| Name                  | Type                                         | Description                                                                                                                                                                                                                                                                                                                                                                                               | Default |
| --------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `input`               | `TWorkflowInput \| None`                     | The input to the task.                                                                                                                                                                                                                                                                                                                                                                                    | `None`  |
| `additional_metadata` | `JSONSerializableMapping \| None`            | Additional metadata to attach to the task.                                                                                                                                                                                                                                                                                                                                                                | `None`  |
| `parent_outputs`      | `dict[str, JSONSerializableMapping] \| None` | Outputs from parent tasks, if any. This is useful for mimicking DAG functionality. For instance, if you have a task `step_2` that has a `parent` which is `step_1`, you can pass `parent_outputs={"step_1": {"result": "Hello, world!"}}` to `step_2.mock_run()` to be able to access `ctx.task_output(step_1)` in `step_2`.                                                                              | `None`  |
| `retry_count`         | `int`                                        | The number of times the task has been retried.                                                                                                                                                                                                                                                                                                                                                            | `0`     |
| `lifespan`            | `Any`                                        | The lifespan to be used in the task, which is useful if one was set on the worker. This will allow you to access `ctx.lifespan` inside of your task.                                                                                                                                                                                                                                                      | `None`  |
| `dependencies`        | `dict[str, Any] \| None`                     | Dependencies to be injected into the task. This is useful for tasks that have dependencies defined using `Depends`. **IMPORTANT**: You must pass the dependencies _directly_, **not** the `Depends` objects themselves. For example, if you have a task that has a dependency `config: Annotated[str, Depends(get_config)]`, you should pass `dependencies={"config": "config_value"}` to `aio_mock_run`. | `None`  |

Returns:

| Type | Description             |
| ---- | ----------------------- |
| `R`  | The output of the task. |


---

<!-- Source: https://docs.hatchet.run/reference/python/asyncio -->

# Working with `asyncio`

Hatchet's Python SDK, similarly to other popular libraries like FastAPI, Langchain, etc., makes heavy use of `asyncio`, and recommends that you do as well!


  To learn the basics of `asyncio`, check out [this introduction from
  FastAPI](https://fastapi.tiangolo.com/async/).


However, as is the case in FastAPI, when using `asyncio` in Hatchet, you need to be careful to not have any blocking logic in the functions you define as tasks, as this will block the asyncio event loop and prevent additional work from executing until the blocking operation has completed.

For example, this is async-safe:

```python
async def async_safe() -> int:
    await asyncio.sleep(5)

    return 42
```

But this is not:

```python
async def blocking() -> int:
    time.sleep(5)

    return 42
```

In the second case, your worker will not be able to process any other work that's defined as async until the five-second sleep has finished.

### Using `asyncio.to_thread` and `loop.run_in_executor`

To avoid problems caused by blocking code, you can run your blocking code in an executor with `asyncio.to_thread` or, more verbosely, `loop.run_in_executor`. The two examples below are async-safe and will no longer block the event loop.

```python
async def to_thread() -> int:
    await asyncio.to_thread(time.sleep, 5)

    return 42
```

```python
async def run_in_executor() -> int:
    loop = asyncio.get_event_loop()

    await loop.run_in_executor(None, time.sleep, 5)

    return 42
```

### More Resources for working with `asyncio`

If you're looking for more info on developing with AsyncIO more broadly, we highly recommend the following
resources:

- Python's Documentation on [Developing with
  AsyncIO](https://docs.python.org/3/library/asyncio-dev.html)
- Tusamma's Medium post about [How AsyncIO
  works](https://medium.com/@tssovi/how-does-asyncio-works-f5386316b7fa)
- Zac Hatfield-Dodds's PyCon 2023 talk on [Async: scaling structured concurrency with static and dynamic analysis](https://www.youtube.com/watch?v=FrpUb6OEbcc)


---

<!-- Source: https://docs.hatchet.run/reference/python/pydantic -->

# Pydantic Support

The V1 Hatchet SDK leans heavily on [Pydantic](https://docs.pydantic.dev/latest/) (both internally and externally) for handling validation of workflow inputs and outputs, method inputs, and more.

### Usage

To enable Pydantic for validation, you'll need to:

1. Provide an `input_validator` as a parameter to your `workflow`.
2. Add return type hints for your `tasks`.

### Default Behavior

By default, if no `input_validator` is provided, the `EmptyModel` is used, which is a Pydantic model that accepts any input. For example:

```python
from hatchet_sdk import Context, EmptyModel, Hatchet

hatchet = Hatchet(debug=True)


@hatchet.task()
def simple(input: EmptyModel, ctx: Context) -> dict[str, str]:
    return {"result": "Hello, world!"}


@hatchet.durable_task()
def simple_durable(input: EmptyModel, ctx: Context) -> dict[str, str]:
    return {"result": "Hello, world!"}


def main() -> None:
    worker = hatchet.worker(
        "test-worker",
        workflows=[simple, simple_durable],
    )
    worker.start()
```

In this simple example, the `input` that's injected into the task accepts an argument `input`, which is of type `EmptyModel`. The `EmptyModel` can be imported directly from Hatchet, and is an alias for:

```python
from pydantic import BaseModel, ConfigDict

class EmptyModel(BaseModel):
    model_config = ConfigDict(extra="allow")
```

Note that since `extra="allow"` is set, workflows will not fail with validation errors if an extra field is provided.

### Example Usage

We highly recommend creating Pydantic models to represent your workflow inputs and outputs. This will help you catch errors early and ensure that your workflows are well-typed. For example, consider a fanout workflow like this:

```python
class ParentInput(BaseModel):
    n: int = 100


class ChildInput(BaseModel):
    a: str


parent_wf = hatchet.workflow(name="FanoutParent", input_validator=ParentInput)
child_wf = hatchet.workflow(name="FanoutChild", input_validator=ChildInput)


@parent_wf.task(execution_timeout=timedelta(minutes=5))
async def spawn(input: ParentInput, ctx: Context) -> dict[str, Any]:
    print("spawning child")

    result = await child_wf.aio_run_many(
        [
            child_wf.create_bulk_run_item(
                input=ChildInput(a=str(i)),
                options=TriggerWorkflowOptions(
                    additional_metadata={"hello": "earth"}, key=f"child{i}"
                ),
            )
            for i in range(input.n)
        ],
    )

    print(f"results {result}")

    return {"results": result}
```

In this case, we've defined two workflows: a parent and a child. They both have their inputs typed, and the parent spawns the child. Note that `child_wf.create_workflow_run_config` is typed, so the type checker (and your IDE) know the type of the input to the child workflow.

Then, the child tasks are defined as follows:

```python
@child_wf.task()
async def process(input: ChildInput, ctx: Context) -> dict[str, str]:
    print(f"child process {input.a}")
    return {"status": input.a}


@child_wf.task(parents=[process])
async def process2(input: ChildInput, ctx: Context) -> dict[str, str]:
    process_output = ctx.task_output(process)
    a = process_output["status"]

    return {"status2": a + "2"}
```

In the children, the inputs are validated by Pydantic, so you can access their attributes directly without needing a type cast or parsing a dictionary with the inputs instead.


---

<!-- Source: https://docs.hatchet.run/reference/python/lifespans -->

# Lifespans


  Lifespans are an **experimental feature** in Hatchet, and are subject to
  change.


Hatchet's Python SDK allows you define a **_lifespan_**, which is an async generator that runs when your worker starts up and cleans up when it exits, which lets you share state across all of the tasks running on the worker. This behaves almost identically to [FastAPI's lifespans](https://fastapi.tiangolo.com/advanced/events/), and is intended to be used in the same way. Lifespans are useful for sharing state like connection pools across all tasks on a single worker. They also work great for loading expensive machine learning models into memory before the worker starts.


  We recommend only using lifespans for storing **_immutable_** state to share
  between tasks running on your worker. The intention is not to e.g. store a
  counter of the number of tasks that a worker has run and increment that
  counter on each task run. This is prone to unexpected behavior due to
  concurrency in Hatchet.


## Usage

To use Hatchet's `lifespan` feature, define an async generator and pass it into your `worker`:

```python
class Lifespan(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    foo: str
    pool: ConnectionPool


async def lifespan() -> AsyncGenerator[Lifespan, None]:
    print("Running lifespan!")
    with ConnectionPool("postgres://hatchet:hatchet@localhost:5431/hatchet") as pool:
        yield Lifespan(
            foo="bar",
            pool=pool,
        )

    print("Cleaning up lifespan!")


worker = hatchet.worker(
    "test-worker", slots=1, workflows=[lifespan_workflow], lifespan=lifespan
)
```

When the worker starts, it will run the lifespan up to the `yield`. Then, on worker shutdown, it will clean up by running everything after the `yield` (the same as with any other generator).


  Your lifespan must only `yield` **_once_**.


Then, to use your lifespan in a task, you can extract it from the context with `Context.lifespan`.

```python
class TaskOutput(BaseModel):
    num_rows: int
    external_ids: list[UUID]


lifespan_workflow = hatchet.workflow(name="LifespanWorkflow")


@lifespan_workflow.task()
def sync_lifespan_task(input: EmptyModel, ctx: Context) -> TaskOutput:
    pool = cast(Lifespan, ctx.lifespan).pool

    with pool.connection() as conn:
        query = conn.execute("SELECT * FROM v1_lookup_table_olap LIMIT 5;")
        rows = query.fetchall()

        for row in rows:
            print(row)

        print("executed sync task with lifespan", ctx.lifespan)

        return TaskOutput(
            num_rows=len(rows),
            external_ids=[cast(UUID, row[0]) for row in rows],
        )
```


  For type checking, cast the `Context.lifespan` to whatever type your lifespan
  generator yields.


And that's it! Now, any task running on the worker with the lifespan provided will have access to the lifespan data.


---

<!-- Source: https://docs.hatchet.run/reference/python/dependency-injection -->

# Dependency Injection


  Dependency injection is an **experimental feature** in Hatchet, and is subject
  to change.


Hatchet's Python SDK allows you to inject **_dependencies_** into your tasks, FastAPI style. These dependencies can be either synchronous or asynchronous functions. They are executed before the task is triggered, and their results are injected into the task as parameters.

This behaves almost identically to [FastAPI's dependency injection](https://fastapi.tiangolo.com/tutorial/dependencies/), and is intended to be used in the same way. Dependencies are useful for sharing logic between tasks that you'd like to avoid repeating, or would like to factor out of the task logic itself (e.g. to make testing easier).


Since dependencies are run before tasks are executed, having many dependencies (or any that take a long time to evaluate) can cause tasks to experience significantly delayed start times, as they must wait for all dependencies to finish evaluating.


## Usage

To add dependencies to your tasks, import `Depends` from the `hatchet_sdk`. Then:

```python
async def async_dep(input: EmptyModel, ctx: Context) -> str:
    return ASYNC_DEPENDENCY_VALUE


def sync_dep(input: EmptyModel, ctx: Context) -> str:
    return SYNC_DEPENDENCY_VALUE


@asynccontextmanager
async def async_cm_dep(
    input: EmptyModel, ctx: Context, async_dep: Annotated[str, Depends(async_dep)]
) -> AsyncGenerator[str, None]:
    try:
        yield ASYNC_CM_DEPENDENCY_VALUE + "_" + async_dep
    finally:
        pass


@contextmanager
def sync_cm_dep(
    input: EmptyModel, ctx: Context, sync_dep: Annotated[str, Depends(sync_dep)]
) -> Generator[str, None, None]:
    try:
        yield SYNC_CM_DEPENDENCY_VALUE + "_" + sync_dep
    finally:
        pass


@contextmanager
def base_cm_dep(input: EmptyModel, ctx: Context) -> Generator[str, None, None]:
    try:
        yield CHAINED_CM_VALUE
    finally:
        pass


def chained_dep(
    input: EmptyModel, ctx: Context, base_cm: Annotated[str, Depends(base_cm_dep)]
) -> str:
    return "chained_" + base_cm


@asynccontextmanager
async def base_async_cm_dep(
    input: EmptyModel, ctx: Context
) -> AsyncGenerator[str, None]:
    try:
        yield CHAINED_ASYNC_CM_VALUE
    finally:
        pass


async def chained_async_dep(
    input: EmptyModel,
    ctx: Context,
    base_async_cm: Annotated[str, Depends(base_async_cm_dep)],
) -> str:
    return "chained_" + base_async_cm
```

In this example, we've declared two dependencies: one synchronous and one asynchronous. You can do anything you like in your dependencies, such as creating database sessions, managing configuration, sharing instances of service-layer logic, and more.

Once you've defined your dependency functions, inject them into your tasks as follows:

```python
@hatchet.task()
async def async_task_with_dependencies(
    _i: EmptyModel,
    ctx: Context,
    async_dep: Annotated[str, Depends(async_dep)],
    sync_dep: Annotated[str, Depends(sync_dep)],
    async_cm_dep: Annotated[str, Depends(async_cm_dep)],
    sync_cm_dep: Annotated[str, Depends(sync_cm_dep)],
    chained_dep: Annotated[str, Depends(chained_dep)],
    chained_async_dep: Annotated[str, Depends(chained_async_dep)],
) -> Output:
    return Output(
        sync_dep=sync_dep,
        async_dep=async_dep,
        async_cm_dep=async_cm_dep,
        sync_cm_dep=sync_cm_dep,
        chained_dep=chained_dep,
        chained_async_dep=chained_async_dep,
    )
```


  Important note: Your dependency functions must take two positional arguments:
  the workflow input and the `Context` (the same as any other task).


That's it! Now, whenever your task is triggered, its dependencies will be evaluated, and the results will be injected into the task at runtime for you to use as needed.


---

<!-- Source: https://docs.hatchet.run/reference/python/dataclasses -->

# Dataclass Support

Throughout the docs, we use Pydantic models in virtually all of our Python examples for validating task inputs and outputs. This is the recommended path, as it provides lots of safety guarantees as you're writing tasks. With that said, Hatchet also supports using `dataclasses` as both input and output types to tasks. **Dataclass support was added in SDK version 1.21.0.**

> **Warning:** Dataclasses do not perform any type validation on instantiation like Pydantic
>   models do.

### Usage

To use a dataclass instead of a Pydantic model, you'll need to:

1. Provide an `input_validator` as a parameter to your `workflow` or `task` (in the case of a standalone task with `hatchet.task`).
2. Add return type hints for your `tasks`.

### Example Usage

`dataclass` validators work exactly like Pydantic models in Hatchet. First, you create the classes:

```python
@dataclass
class Input:
    name: str


@dataclass
class Output:
    message: str
```

And then you provide the classes to your workflow or task:

```python
@hatchet.task(input_validator=Input)
def say_hello(input: Input, ctx: Context) -> Output:
    return Output(message=f"Hello, {input.name}!")
```

And finally, triggering works the same as well - you just provide the dataclass instance as input:

```python
say_hello.run(input=Input(name="Hatchet"))
```


---

<!-- Source: https://docs.hatchet.run/reference/typescript/client -->

# Hatchet TypeScript SDK Reference

This is the TypeScript SDK reference, documenting methods available for interacting with Hatchet resources.
Check out the [user guide](https://docs.hatchet.run/home/) for an introduction to getting your first tasks running.

<a id="hatchetclient"></a>

### HatchetClient

HatchetV1 implements the main client interface for interacting with the Hatchet workflow engine.
It provides methods for creating and executing workflows, as well as managing workers.

Implements

- `IHatchetClient`

Properties

| Property                                  | Type     | Description                          |
| ----------------------------------------- | -------- | ------------------------------------ |
| <a id="property-tenantid"></a> `tenantId` | `string` | The tenant ID for the Hatchet client |

Accessors

<a id="api"></a>

##### `api`

Get Signature

Get the API client for making HTTP requests to the Hatchet API
Note: This is not recommended for general use, but is available for advanced scenarios

Returns

`Api`\<`unknown`\>

A API client instance

<a id="crons"></a>

##### `crons`

Get Signature

Get the cron client for creating and managing cron workflow runs

Returns

[`CronClient`](feature-clients/crons.mdx#cronclient)

A cron client instance

Implementation of

```ts
IHatchetClient.crons;
```

<a id="events"></a>

##### `events`

Get Signature

Get the event client for creating and managing event workflow runs

Returns

`EventClient`

A event client instance

Implementation of

```ts
IHatchetClient.events;
```

<a id="filters"></a>

##### `filters`

Get Signature

Get the filters client for creating and managing filters

Returns

[`FiltersClient`](feature-clients/filters.mdx#filtersclient)

A filters client instance

Implementation of

```ts
IHatchetClient.filters;
```

<a id="logs"></a>

##### `logs`

Get Signature

Get the logs client for creating and managing logs

Returns

[`LogsClient`](feature-clients/logs.mdx#logsclient)

A logs client instance

Implementation of

```ts
IHatchetClient.logs;
```

<a id="metrics"></a>

##### `metrics`

Get Signature

Get the metrics client for creating and managing metrics

Returns

[`MetricsClient`](feature-clients/metrics.mdx#metricsclient)

A metrics client instance

Implementation of

```ts
IHatchetClient.metrics;
```

<a id="ratelimits"></a>

##### `ratelimits`

Get Signature

Get the rate limits client for creating and managing rate limits

Returns

[`RatelimitsClient`](feature-clients/ratelimits.mdx#ratelimitsclient)

A rate limits client instance

Implementation of

```ts
IHatchetClient.ratelimits;
```

<a id="runs"></a>

##### `runs`

Get Signature

Get the runs client for creating and managing runs

Returns

[`RunsClient`](feature-clients/runs.mdx#runsclient)

A runs client instance

Implementation of

```ts
IHatchetClient.runs;
```

<a id="scheduled"></a>

##### `scheduled`

Get Signature

Get the schedules client for creating and managing scheduled workflow runs

Returns

[`ScheduleClient`](feature-clients/schedules.mdx#scheduleclient)

A schedules client instance

Implementation of

```ts
IHatchetClient.scheduled;
```

<a id="schedules"></a>

##### `schedules`

Get Signature

Alias

scheduled

Returns

[`ScheduleClient`](feature-clients/schedules.mdx#scheduleclient)

<a id="tasks"></a>

##### `tasks`

Get Signature

Get the tasks client for creating and managing tasks

Returns

[`WorkflowsClient`](feature-clients/workflows.mdx#workflowsclient)

A tasks client instance

<a id="tenant"></a>

##### `tenant`

Get Signature

Get the tenant client for managing tenants

Returns

`TenantClient`

A tenant client instance

Implementation of

```ts
IHatchetClient.tenant;
```

<a id="webhooks"></a>

##### `webhooks`

Get Signature

Get the webhooks client for creating and managing webhooks

Returns

[`WebhooksClient`](feature-clients/webhooks.mdx#webhooksclient)

A webhooks client instance

Implementation of

```ts
IHatchetClient.webhooks;
```

<a id="workers"></a>

##### `workers`

Get Signature

Get the workers client for creating and managing workers

Returns

[`WorkersClient`](feature-clients/workers.mdx#workersclient)

A workers client instance

Implementation of

```ts
IHatchetClient.workers;
```

<a id="workflows"></a>

##### `workflows`

Get Signature

Get the workflows client for creating and managing workflows

Returns

[`WorkflowsClient`](feature-clients/workflows.mdx#workflowsclient)

A workflows client instance

Implementation of

```ts
IHatchetClient.workflows;
```

#### Methods

<a id="durabletask"></a>

##### `durableTask()`

Implementation of the durableTask method.

Creates a new durable task workflow.
Types can be explicitly specified as generics or inferred from the function signature.

Parameters

| Parameter | Type                                                                                                                               | Description                        |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| `options` | `CreateDurableTaskWorkflowOpts`\<`I` & `Resolved`\<`GlobalInput`, `MiddlewareBefore`\>, `MergeIfNonEmpty`\<`O`, `GlobalOutput`\>\> | Durable task configuration options |

Returns

[`TaskWorkflowDeclaration`](Runnables.mdx#taskworkflowdeclaration)\<`I`, `O`, `GlobalInput`, `GlobalOutput`, `MiddlewareBefore`, `MiddlewareAfter`\>

A TaskWorkflowDeclaration instance for a durable task

Creates a new durable task workflow with types inferred from the function parameter.

Parameters

| Parameter | Type                                                                     | Description                                                         |
| --------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| `options` | `object` & `Omit`\<`CreateDurableTaskWorkflowOpts`\<`I`, `O`\>, `"fn"`\> | Durable task configuration options with function that defines types |

Returns

[`TaskWorkflowDeclaration`](Runnables.mdx#taskworkflowdeclaration)\<`I`, `O`, `GlobalInput`, `GlobalOutput`, `MiddlewareBefore`, `MiddlewareAfter`\>

A TaskWorkflowDeclaration instance with inferred types

<a id="run"></a>

##### `run()`

Triggers a workflow run and waits for the result.

Parameters

| Parameter  | Type                                                            | Description                                                         |
| ---------- | --------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow` | `string` \| `Workflow` \| `BaseWorkflowDeclaration`\<`I`, `O`\> | The workflow to run, either as a Workflow instance or workflow name |
| `input`    | `I`                                                             | The input data for the workflow                                     |
| `options`  | `RunOpts`                                                       | Configuration options for the workflow run                          |

Returns

`Promise`\<`O`\>

A promise that resolves with the workflow result

<a id="runandwait"></a>

##### `runAndWait()`

Triggers a workflow run and waits for the result.

Parameters

| Parameter  | Type                                                            | Description                                                         |
| ---------- | --------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow` | `string` \| `Workflow` \| `BaseWorkflowDeclaration`\<`I`, `O`\> | The workflow to run, either as a Workflow instance or workflow name |
| `input`    | `I`                                                             | The input data for the workflow                                     |
| `options`  | `RunOpts`                                                       | Configuration options for the workflow run                          |

Returns

`Promise`\<`O`\>

A promise that resolves with the workflow result

Alias

run

<a id="runnowait"></a>

##### `runNoWait()`

Triggers a workflow run without waiting for completion.

Parameters

| Parameter  | Type                                                            | Description                                                         |
| ---------- | --------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow` | `string` \| `Workflow` \| `BaseWorkflowDeclaration`\<`I`, `O`\> | The workflow to run, either as a Workflow instance or workflow name |
| `input`    | `I`                                                             | The input data for the workflow                                     |
| `options`  | `RunOpts`                                                       | Configuration options for the workflow run                          |

Returns

`Promise`\<`WorkflowRunRef`\<`O`\>\>

A WorkflowRunRef containing the run ID and methods to interact with the run

<a id="task"></a>

##### `task()`

Implementation of the task method.

Creates a new task workflow.
Types can be explicitly specified as generics or inferred from the function signature.

Parameters

| Parameter | Type                                                                                                                        | Description                |
| --------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| `options` | `CreateTaskWorkflowOpts`\<`I` & `Resolved`\<`GlobalInput`, `MiddlewareBefore`\>, `MergeIfNonEmpty`\<`O`, `GlobalOutput`\>\> | Task configuration options |

Returns

[`TaskWorkflowDeclaration`](Runnables.mdx#taskworkflowdeclaration)\<`I`, `O`, `GlobalInput`, `GlobalOutput`, `MiddlewareBefore`, `MiddlewareAfter`\>

A TaskWorkflowDeclaration instance

Creates a new task workflow with types inferred from the function parameter.

Parameters

| Parameter | Type                                                              | Description                                                 |
| --------- | ----------------------------------------------------------------- | ----------------------------------------------------------- |
| `options` | `object` & `Omit`\<`CreateTaskWorkflowOpts`\<`I`, `O`\>, `"fn"`\> | Task configuration options with function that defines types |

Returns

[`TaskWorkflowDeclaration`](Runnables.mdx#taskworkflowdeclaration)\<`I`, `O`, `GlobalInput`, `GlobalOutput`, `MiddlewareBefore`, `MiddlewareAfter`\>

A TaskWorkflowDeclaration instance with inferred types

<a id="worker"></a>

##### `worker()`

Creates a new worker instance for processing workflow tasks.

Parameters

| Parameter  | Type                           | Description                                   |
| ---------- | ------------------------------ | --------------------------------------------- |
| `name`     | `string`                       | -                                             |
| `options?` | `number` \| `CreateWorkerOpts` | Configuration options for creating the worker |

Returns

`Promise`\<`Worker`\>

A promise that resolves with a new HatchetWorker instance

<a id="workflow"></a>

##### `workflow()`

Creates a new workflow definition.

Parameters

| Parameter | Type                 | Description                                     |
| --------- | -------------------- | ----------------------------------------------- |
| `options` | `CreateWorkflowOpts` | Configuration options for creating the workflow |

Returns

[`WorkflowDeclaration`](Runnables.mdx#workflowdeclaration)\<`I`, `O`, `Resolved`\<`GlobalInput`, `MiddlewareBefore`\>\>

A new Workflow instance

Note

It is possible to create an orphaned workflow if no client is available using @hatchet/client CreateWorkflow


---

<!-- Source: https://docs.hatchet.run/reference/typescript/Context -->

# Context

The Hatchet Context class provides helper methods and useful data to tasks at runtime. It is passed as the second argument to all tasks and durable tasks.

There are two types of context classes you'll encounter:

- Context - The standard context for regular tasks with methods for logging, task output retrieval, cancellation, and more.
- DurableContext - An extended context for durable tasks that includes additional methods for durable execution.

<a id="context"></a>

### Context

Extended by

- [`DurableContext`](#durablecontext)

#### Methods

<a id="additionalmetadata"></a>

##### `additionalMetadata()`

Retrieves additional metadata associated with the current workflow run.

Returns

`Record`\<`string`, `string`\>

A record of metadata key-value pairs.

<a id="bulkrunchildren"></a>

##### `bulkRunChildren()`

Runs multiple children workflows in parallel and waits for all results.

Parameters

| Parameter  | Type       | Description                                                                                  |
| ---------- | ---------- | -------------------------------------------------------------------------------------------- |
| `children` | `object`[] | An array of objects containing the workflow name, input data, and options for each workflow. |

Returns

`Promise`\<`P`[]\>

A list of results from the children workflows.

<a id="bulkrunnowaitchildren"></a>

##### `bulkRunNoWaitChildren()`

Runs multiple children workflows in parallel without waiting for their results.

Parameters

| Parameter  | Type       | Description                                                                                  |
| ---------- | ---------- | -------------------------------------------------------------------------------------------- |
| `children` | `object`[] | An array of objects containing the workflow name, input data, and options for each workflow. |

Returns

`Promise`\<`WorkflowRunRef`\<`P`\>[]\>

A list of workflow run references to the enqueued runs.

<a id="childindex"></a>

##### `childIndex()`

Gets the index of this workflow if it was spawned as part of a bulk operation.

Returns

`number` \| `undefined`

The child index number, or undefined if not set.

<a id="childkey"></a>

##### `childKey()`

Gets the key associated with this workflow if it was spawned as a child workflow.

Returns

`string` \| `undefined`

The child key, or undefined if not set.

<a id="errors"></a>

##### `errors()`

Returns errors from any task runs in the workflow.

Returns

`Record`\<`string`, `string`\>

A record mapping task names to error messages.

Throws

A warning if no errors are found (this method should be used in on-failure tasks).

<a id="filterpayload"></a>

##### `filterPayload()`

Gets the payload from the filter that matched when triggering the event.

Returns

`Record`\<`string`, `any`\>

The payload.

<a id="parentoutput"></a>

##### `parentOutput()`

Retrieves the output of a parent task.

Parameters

| Parameter    | Type                                                                                                   | Description                                             |
| ------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| `parentTask` | \| `string` \| `CreateWorkflowTaskOpts`\<`any`, `L`\> \| `CreateWorkflowDurableTaskOpts`\<`any`, `L`\> | The a CreateTaskOpts or string of the parent task name. |

Returns

`Promise`\<`L`\>

The output of the specified parent task.

Throws

An error if the task output is not found.

<a id="parentworkflowrunid"></a>

##### `parentWorkflowRunId()`

Gets the ID of the parent workflow run if this workflow was spawned as a child.

Returns

`string` \| `undefined`

The parent workflow run ID, or undefined if not a child workflow.

<a id="putstream"></a>

##### `putStream()`

Streams data from the current task run.

Parameters

| Parameter | Type                                          | Description                            |
| --------- | --------------------------------------------- | -------------------------------------- |
| `data`    | `string` \| `Uint8Array`\<`ArrayBufferLike`\> | The data to stream (string or binary). |

Returns

`Promise`\<`void`\>

A promise that resolves when the data has been streamed.

<a id="refreshtimeout"></a>

##### `refreshTimeout()`

Refreshes the timeout for the current task.

Parameters

| Parameter     | Type       | Description                                                                                                                                                   |
| ------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `incrementBy` | `Duration` | The interval by which to increment the timeout. The interval should be specified in the format of '10s' for 10 seconds, '1m' for 1 minute, or '1d' for 1 day. |

Returns

`Promise`\<`void`\>

<a id="releaseslot"></a>

##### `releaseSlot()`

Releases a worker slot for a task run such that the worker can pick up another task.
Note: this is an advanced feature that may lead to unexpected behavior if used incorrectly.

Returns

`Promise`\<`void`\>

A promise that resolves when the slot has been released.

<a id="rethrowifcancelled"></a>

##### `rethrowIfCancelled()`

Helper for broad `catch` blocks so cancellation isn't accidentally swallowed.

Example:

```ts
try { ... } catch (e) { ctx.rethrowIfCancelled(e); ... }
```

Parameters

| Parameter | Type      |
| --------- | --------- |
| `err`     | `unknown` |

Returns

`void`

<a id="retrycount"></a>

##### `retryCount()`

Gets the number of times the current task has been retried.

Returns

`number`

The retry count.

<a id="runchild"></a>

##### `runChild()`

Runs a new workflow and waits for its result.

Parameters

| Parameter  | Type                                                                                                                                                               | Description                                                                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| `workflow` | \| `string` \| `BaseWorkflowDeclaration`\<`Q`, `P`\> \| [`TaskWorkflowDeclaration`](Runnables.mdx#taskworkflowdeclaration)\<`Q`, `P`, \{ \}, \{ \}, \{ \}, \{ \}\> | The workflow to run (name, Workflow instance, or WorkflowV1 instance).      |
| `input`    | `Q`                                                                                                                                                                | The input data for the workflow.                                            |
| `options?` | `ChildRunOpts`                                                                                                                                                     | An options object containing key, sticky, priority, and additionalMetadata. |

Returns

`Promise`\<`P`\>

The result of the workflow.

<a id="runnowaitchild"></a>

##### `runNoWaitChild()`

Enqueues a new workflow without waiting for its result.

Parameters

| Parameter  | Type                                              | Description                                                                 |
| ---------- | ------------------------------------------------- | --------------------------------------------------------------------------- |
| `workflow` | `string` \| `BaseWorkflowDeclaration`\<`Q`, `P`\> | The workflow to enqueue (name, Workflow instance, or WorkflowV1 instance).  |
| `input`    | `Q`                                               | The input data for the workflow.                                            |
| `options?` | `ChildRunOpts`                                    | An options object containing key, sticky, priority, and additionalMetadata. |

Returns

`Promise`\<`WorkflowRunRef`\<`P`\>\>

A reference to the spawned workflow run.

<a id="taskname"></a>

##### `taskName()`

Gets the name of the current running task.

Returns

`string`

The name of the task.

<a id="taskrunexternalid"></a>

##### `taskRunExternalId()`

Gets the ID of the current task run.

Returns

`string`

The task run ID.

<a id="triggeredbyevent"></a>

##### `triggeredByEvent()`

Determines if the workflow was triggered by an event.

Returns

`boolean`

True if the workflow was triggered by an event, otherwise false.

<a id="triggers"></a>

##### `triggers()`

Gets the dag conditional triggers for the current workflow run.

Returns

`TriggerData`

The triggers for the current workflow.

<a id="userdata"></a>

##### `userData()`

Gets the user data associated with the workflow.

Returns

`K`

The user data.

<a id="workflowid"></a>

##### `workflowId()`

Gets the workflow ID of the currently running workflow.

Returns

`string` \| `undefined`

The workflow id.

<a id="workflowname"></a>

##### `workflowName()`

Gets the name of the current workflow.

Returns

`string`

The name of the workflow.

<a id="workflowrunid"></a>

##### `workflowRunId()`

Gets the ID of the current workflow run.

Returns

`string`

The workflow run ID.

<a id="workflowversionid"></a>

##### `workflowVersionId()`

Gets the workflow version ID of the currently running workflow.

Returns

`string` \| `undefined`

The workflow version ID.

---

<a id="contextworker"></a>

### ContextWorker

ContextWorker is a wrapper around the V1Worker class that provides a more user-friendly interface for the worker from the context of a run.

#### Methods

<a id="hasworkflow"></a>

##### `hasWorkflow()`

Checks if the worker has a registered workflow.

Parameters

| Parameter      | Type     | Description                        |
| -------------- | -------- | ---------------------------------- |
| `workflowName` | `string` | The name of the workflow to check. |

Returns

`boolean`

True if the workflow is registered, otherwise false.

<a id="id"></a>

##### `id()`

Gets the ID of the worker.

Returns

`string` \| `undefined`

The ID of the worker.

<a id="labels"></a>

##### `labels()`

Gets the current state of the worker labels.

Returns

`WorkerLabels`

The labels of the worker.

<a id="upsertlabels"></a>

##### `upsertLabels()`

Upserts the a set of labels on the worker.

Parameters

| Parameter | Type           | Description           |
| --------- | -------------- | --------------------- |
| `labels`  | `WorkerLabels` | The labels to upsert. |

Returns

`Promise`\<`WorkerLabels`\>

A promise that resolves when the labels have been upserted.

---

<a id="durablecontext"></a>

### DurableContext

DurableContext provides helper methods and useful data to durable tasks at runtime.
It extends the Context class and includes additional methods for durable execution like sleepFor and waitFor.

Extends

- [`Context`](#context)\<`T`, `K`\>

#### Methods

<a id="sleepfor"></a>

##### `sleepFor()`

Pauses execution for the specified duration.
Duration is "global" meaning it will wait in real time regardless of transient failures like worker restarts.

Parameters

| Parameter          | Type       | Description                |
| ------------------ | ---------- | -------------------------- |
| `duration`         | `Duration` | The duration to sleep for. |
| `readableDataKey?` | `string`   | -                          |

Returns

`Promise`\<`Record`\<`string`, `any`\>\>

A promise that resolves when the sleep duration has elapsed.

<a id="waitfor"></a>

##### `waitFor()`

Pauses execution until the specified conditions are met.
Conditions are "global" meaning they will wait in real time regardless of transient failures like worker restarts.

Parameters

| Parameter    | Type                           | Description                 |
| ------------ | ------------------------------ | --------------------------- |
| `conditions` | `Conditions` \| `Conditions`[] | The conditions to wait for. |

Returns

`Promise`\<`Record`\<`string`, `any`\>\>

A promise that resolves with the event that satisfied the conditions.


---

<!-- Source: https://docs.hatchet.run/reference/typescript/feature-clients/crons -->

<a id="cronclient"></a>

### Cron Client

The cron client is a client for managing cron workflows within Hatchet.

#### Methods

<a id="create"></a>

##### `create()`

Creates a new Cron workflow.

Parameters

| Parameter                  | Type                                                                                                                                                                 | Description                                   |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| `workflow`                 | `string` \| `BaseWorkflowDeclaration`\<`any`, `any`\> \| `Workflow`                                                                                                  | The workflow identifier or Workflow object.   |
| `cron`                     | \{ `additionalMetadata?`: `Record`\<`string`, `string`\>; `expression`: `string`; `input?`: `Record`\<`string`, `any`\>; `name`: `string`; `priority?`: `number`; \} | The input data for creating the Cron Trigger. |
| `cron.additionalMetadata?` | `Record`\<`string`, `string`\>                                                                                                                                       | -                                             |
| `cron.expression`          | `string`                                                                                                                                                             | -                                             |
| `cron.input?`              | `Record`\<`string`, `any`\>                                                                                                                                          | -                                             |
| `cron.name`                | `string`                                                                                                                                                             | -                                             |
| `cron.priority?`           | `number`                                                                                                                                                             | -                                             |

Returns

`Promise`\<`CronWorkflows`\>

A promise that resolves to the created CronWorkflows object.

Throws

Will throw an error if the input is invalid or the API call fails.

<a id="delete"></a>

##### `delete()`

Deletes an existing Cron Trigger.

Parameters

| Parameter | Type                        | Description                                              |
| --------- | --------------------------- | -------------------------------------------------------- |
| `cron`    | `string` \| `CronWorkflows` | The Cron Trigger ID as a string or CronWorkflows object. |

Returns

`Promise`\<`void`\>

A promise that resolves when the Cron Trigger is deleted.

<a id="get"></a>

##### `get()`

Retrieves a specific Cron Trigger by its ID.

Parameters

| Parameter | Type                        | Description                                              |
| --------- | --------------------------- | -------------------------------------------------------- |
| `cron`    | `string` \| `CronWorkflows` | The Cron Trigger ID as a string or CronWorkflows object. |

Returns

`Promise`\<`CronWorkflows`\>

A promise that resolves to the CronWorkflows object.

<a id="list"></a>

##### `list()`

Lists all Cron Triggers based on the provided query parameters.

Parameters

| Parameter | Type                | Description                                 |
| --------- | ------------------- | ------------------------------------------- |
| `query`   | `object` & `object` | Query parameters for listing Cron Triggers. |

Returns

`Promise`\<`CronWorkflowsList`\>

A promise that resolves to a CronWorkflowsList object.


---

<!-- Source: https://docs.hatchet.run/reference/typescript/feature-clients/filters -->

<a id="filtersclient"></a>

### Filters Client

The filters client is a client for interacting with Hatchet's filters API.

#### Methods

<a id="create"></a>

##### `create()`

Creates a new filter.

Parameters

| Parameter | Type                    | Description                           |
| --------- | ----------------------- | ------------------------------------- |
| `opts`    | `V1CreateFilterRequest` | The options for the create operation. |

Returns

`Promise`\<`V1Filter`\>

A promise that resolves to the created filter.

<a id="delete"></a>

##### `delete()`

Deletes a filter by its ID.

Parameters

| Parameter  | Type     | Description                     |
| ---------- | -------- | ------------------------------- |
| `filterId` | `string` | The ID of the filter to delete. |

Returns

`Promise`\<`V1Filter`\>

A promise that resolves to the deleted filter.

<a id="get"></a>

##### `get()`

Gets a filter by its ID.

Parameters

| Parameter  | Type     | Description                  |
| ---------- | -------- | ---------------------------- |
| `filterId` | `string` | The ID of the filter to get. |

Returns

`Promise`\<`V1Filter`\>

A promise that resolves to the filter.

<a id="list"></a>

##### `list()`

Lists all filters.

Parameters

| Parameter           | Type                                                                                    | Description                                                    |
| ------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `opts?`             | \{ `limit?`: `number`; `offset?`: `number`; `scopes?`: ...[]; `workflowIds?`: ...[]; \} | The options for the list operation.                            |
| `opts.limit?`       | `number`                                                                                | The number of filters to return.                               |
| `opts.offset?`      | `number`                                                                                | The number of filters to skip before returning the result set. |
| `opts.scopes?`      | ...[]                                                                                   | A list of scopes to filter by.                                 |
| `opts.workflowIds?` | ...[]                                                                                   | A list of workflow IDs to filter by.                           |

Returns

`Promise`\<`V1FilterList`\>

A promise that resolves to the list of filters.

<a id="update"></a>

##### `update()`

Updates a filter by its ID.

Parameters

| Parameter  | Type                    | Description                         |
| ---------- | ----------------------- | ----------------------------------- |
| `filterId` | `string`                | The ID of the filter to update.     |
| `updates`  | `V1UpdateFilterRequest` | The updates to apply to the filter. |

Returns

`Promise`\<`V1Filter`\>

A promise that resolves to the updated filter.


---

<!-- Source: https://docs.hatchet.run/reference/typescript/feature-clients/logs -->

<a id="logsclient"></a>

### Logs Client

The logs client is a client for interacting with Hatchet's logs API.

#### Methods

<a id="list"></a>

##### `list()`

Lists the logs for a given task run.

Parameters

| Parameter   | Type                            | Description                                |
| ----------- | ------------------------------- | ------------------------------------------ |
| `taskRunId` | `string`                        | The ID of the task run to list logs for.   |
| `opts?`     | [`ListLogsOpts`](#listlogsopts) | The options filter for the list operation. |

Returns

`Promise`\<`V1LogLineList`\>

A promise that resolves to the list of logs.

## Type Aliases

<a id="listlogsopts"></a>

### ListLogsOpts

```ts
type ListLogsOpts = object;
```

The options for the list logs operation.

Properties

| Property                                          | Type                        | Description                                |
| ------------------------------------------------- | --------------------------- | ------------------------------------------ |
| <a id="attempt"></a> `attempt?`                   | `number`                    | Filter logs by attempt number.             |
| <a id="levels"></a> `levels?`                     | `V1LogLineLevel`[]          | Filter logs by log level.                  |
| <a id="limit"></a> `limit?`                       | `number`                    | The maximum number of log lines to return. |
| <a id="orderbydirection"></a> `orderByDirection?` | `V1LogLineOrderByDirection` | The direction to order the logs by.        |
| <a id="search"></a> `search?`                     | `string`                    | Filter logs by a search string.            |
| <a id="since"></a> `since?`                       | `Date`                      | Return only logs after this date.          |
| <a id="until"></a> `until?`                       | `Date`                      | Return only logs before this date.         |


---

<!-- Source: https://docs.hatchet.run/reference/typescript/feature-clients/metrics -->

<a id="metricsclient"></a>

### Metrics Client

The metrics client is a client for reading metrics out of Hatchet’s metrics API.

#### Methods

<a id="getqueuemetrics"></a>

##### `getQueueMetrics()`

Returns the queue metrics for the current tenant.

Parameters

| Parameter | Type            | Description                  |
| --------- | --------------- | ---------------------------- |
| `opts?`   | `RequestParams` | The options for the request. |

Returns

`Promise`\<`TenantStepRunQueueMetrics`\>

The queue metrics for the current tenant.

<a id="gettaskstatusmetrics"></a>

##### `getTaskStatusMetrics()`

Returns aggregate task run counts grouped by status (queued, running, completed, failed, cancelled)

Parameters

| Parameter                             | Type                                                                                                                                                                                           | Description                                                                                     |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `query`                               | \{ `additional_metadata?`: `string`[]; `parent_task_external_id?`: `string`; `since`: `string`; `triggering_event_external_id?`: `string`; `until?`: `string`; `workflow_ids?`: `string`[]; \} | Filters for the metrics query (e.g. `since`, `until`, `workflow_ids`).                          |
| `query.additional_metadata?`          | `string`[]                                                                                                                                                                                     | Additional metadata k-v pairs to filter by                                                      |
| `query.parent_task_external_id?`      | `string`                                                                                                                                                                                       | The parent task's external id **Format** uuid **Min Length** 36 **Max Length** 36               |
| `query.since?`                        | `string`                                                                                                                                                                                       | The start time to get metrics for **Format** date-time                                          |
| `query.triggering_event_external_id?` | `string`                                                                                                                                                                                       | The id of the event that triggered the task **Format** uuid **Min Length** 36 **Max Length** 36 |
| `query.until?`                        | `string`                                                                                                                                                                                       | The end time to get metrics for **Format** date-time                                            |
| `query.workflow_ids?`                 | `string`[]                                                                                                                                                                                     | The workflow id to find runs for                                                                |
| `requestParams?`                      | `RequestParams`                                                                                                                                                                                | Optional request-level overrides (headers, signal, etc.).                                       |

Returns

`Promise`\<`TaskStatusMetrics`\>

Counts per status for the matched task runs.


---

<!-- Source: https://docs.hatchet.run/reference/typescript/feature-clients/ratelimits -->

<a id="ratelimitsclient"></a>

### RatelimitsClient

The rate limits client is a wrapper for Hatchet’s gRPC API that makes it easier to work with rate limits in Hatchet.

#### Methods

<a id="list"></a>

##### `list()`

Lists all rate limits for the current tenant.

Parameters

| Parameter | Type                                                                                                                                                                              | Description                         |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `opts`    | \| \{ `limit?`: `number`; `offset?`: `number`; `orderByDirection?`: `RateLimitOrderByDirection`; `orderByField?`: `RateLimitOrderByField`; `search?`: `string`; \} \| `undefined` | The options for the list operation. |

Returns

`Promise`\<`RateLimitList`\>

A promise that resolves to the list of rate limits.

<a id="upsert"></a>

##### `upsert()`

Upserts a rate limit for the current tenant.

Parameters

| Parameter | Type                  | Description                           |
| --------- | --------------------- | ------------------------------------- |
| `opts`    | `CreateRateLimitOpts` | The options for the upsert operation. |

Returns

`Promise`\<`string`\>

A promise that resolves to the key of the upserted rate limit.


---

<!-- Source: https://docs.hatchet.run/reference/typescript/feature-clients/runs -->

<a id="runsclient"></a>

### Runs Client

The runs client is a client for interacting with task and workflow runs within Hatchet.

#### Methods

<a id="cancel"></a>

##### `cancel()`

Cancels a task or workflow run by its ID.

Parameters

| Parameter | Type            | Description                           |
| --------- | --------------- | ------------------------------------- |
| `opts`    | `CancelRunOpts` | The options for the cancel operation. |

Returns

`Promise`\<`AxiosResponse`\<`V1CancelledTasks`, `any`, \{
\}\>\>

A promise that resolves to the cancelled run.

<a id="get"></a>

##### `get()`

Gets a task or workflow run by its ID.

Parameters

| Parameter | Type                                | Description               |
| --------- | ----------------------------------- | ------------------------- |
| `run`     | `string` \| `WorkflowRunRef`\<`T`\> | The ID of the run to get. |

Returns

`Promise`\<`V1WorkflowRunDetails`\>

A promise that resolves to the run.

<a id="get_status"></a>

##### `get_status()`

Gets the status of a task or workflow run by its ID.

Parameters

| Parameter | Type                                | Description                             |
| --------- | ----------------------------------- | --------------------------------------- |
| `run`     | `string` \| `WorkflowRunRef`\<`T`\> | The ID of the run to get the status of. |

Returns

`Promise`\<`V1TaskStatus`\>

A promise that resolves to the status of the run.

<a id="list"></a>

##### `list()`

Lists all task and workflow runs for the current tenant.

Parameters

| Parameter | Type                        | Description                         |
| --------- | --------------------------- | ----------------------------------- |
| `opts?`   | `Partial`\<`ListRunsOpts`\> | The options for the list operation. |

Returns

`Promise`\<`V1TaskSummaryList`\>

A promise that resolves to the list of runs.

<a id="replay"></a>

##### `replay()`

Replays a task or workflow run by its ID.

Parameters

| Parameter | Type            | Description                           |
| --------- | --------------- | ------------------------------------- |
| `opts`    | `ReplayRunOpts` | The options for the replay operation. |

Returns

`Promise`\<`AxiosResponse`\<`V1ReplayedTasks`, `any`, \{
\}\>\>

A promise that resolves to the replayed run.

<a id="runref"></a>

##### `runRef()`

Creates a run reference for a task or workflow run by its ID.

Parameters

| Parameter | Type     | Description                                  |
| --------- | -------- | -------------------------------------------- |
| `id`      | `string` | The ID of the run to create a reference for. |

Returns

`WorkflowRunRef`\<`T`\>

A promise that resolves to the run reference.

<a id="subscribetostream"></a>

##### `subscribeToStream()`

Subscribes to a stream of events for a task or workflow run by its ID.

Parameters

| Parameter       | Type     | Description                        |
| --------------- | -------- | ---------------------------------- |
| `workflowRunId` | `string` | The ID of the run to subscribe to. |

Returns

`AsyncIterableIterator`\<`string`\>

A promise that resolves to the stream of events.


---

<!-- Source: https://docs.hatchet.run/reference/typescript/feature-clients/schedules -->

<a id="scheduleclient"></a>

### ScheduleClient

The scheduled client is a client for managing scheduled workflows within Hatchet

#### Methods

<a id="bulkdelete"></a>

##### `bulkDelete()`

Bulk deletes scheduled runs (by explicit IDs and/or a filter).

Parameters

| Parameter             | Type                                                                                     | Description                                                       |
| --------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `opts`                | \{ `filter?`: `ScheduledWorkflowsBulkDeleteFilter`; `scheduledRuns?`: (... \| ...)[]; \} | Either `scheduledRuns` (ids/objects) and/or a server-side filter. |
| `opts.filter?`        | `ScheduledWorkflowsBulkDeleteFilter`                                                     | -                                                                 |
| `opts.scheduledRuns?` | (... \| ...)[]                                                                           | -                                                                 |

Returns

`Promise`\<`ScheduledWorkflowsBulkDeleteResponse`\>

A promise that resolves to deleted ids + per-id errors.

<a id="bulkupdate"></a>

##### `bulkUpdate()`

Bulk updates (reschedules) scheduled runs.

Parameters

| Parameter | Type       | Description                        |
| --------- | ---------- | ---------------------------------- |
| `updates` | `object`[] | List of id/object + new triggerAt. |

Returns

`Promise`\<`ScheduledWorkflowsBulkUpdateResponse`\>

A promise that resolves to updated ids + per-id errors.

<a id="create"></a>

##### `create()`

Creates a new Scheduled Run.

Parameters

| Parameter                  | Type                                                                                                                                            | Description                           |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| `workflow`                 | `string` \| `Workflow`                                                                                                                          | The workflow name or Workflow object. |
| `cron`                     | \{ `additionalMetadata?`: `Record`\<`string`, `string`\>; `input?`: `Record`\<`string`, `any`\>; `priority?`: `number`; `triggerAt`: `Date`; \} | -                                     |
| `cron.additionalMetadata?` | `Record`\<`string`, `string`\>                                                                                                                  | -                                     |
| `cron.input?`              | `Record`\<`string`, `any`\>                                                                                                                     | -                                     |
| `cron.priority?`           | `number`                                                                                                                                        | -                                     |
| `cron.triggerAt`           | `Date`                                                                                                                                          | -                                     |

Returns

`Promise`\<`ScheduledWorkflows`\>

A promise that resolves to the created ScheduledWorkflows object.

Throws

Will throw an error if the input is invalid or the API call fails.

<a id="delete"></a>

##### `delete()`

Deletes an existing Scheduled Run.

Parameters

| Parameter      | Type                             | Description                                                    |
| -------------- | -------------------------------- | -------------------------------------------------------------- |
| `scheduledRun` | `string` \| `ScheduledWorkflows` | The Scheduled Run ID as a string or ScheduledWorkflows object. |

Returns

`Promise`\<`void`\>

A promise that resolves when the Scheduled Run is deleted.

<a id="get"></a>

##### `get()`

Retrieves a specific Scheduled Run by its ID.

Parameters

| Parameter      | Type                             | Description                                                    |
| -------------- | -------------------------------- | -------------------------------------------------------------- |
| `scheduledRun` | `string` \| `ScheduledWorkflows` | The Scheduled Run ID as a string or ScheduledWorkflows object. |

Returns

`Promise`\<`ScheduledWorkflows`\>

A promise that resolves to the ScheduledWorkflows object.

<a id="list"></a>

##### `list()`

Lists all Cron Triggers based on the provided query parameters.

Parameters

| Parameter | Type                | Description                                  |
| --------- | ------------------- | -------------------------------------------- |
| `query`   | `object` & `object` | Query parameters for listing Scheduled Runs. |

Returns

`Promise`\<`ScheduledWorkflowsList`\>

A promise that resolves to a ScheduledWorkflowsList object.

<a id="update"></a>

##### `update()`

Updates (reschedules) an existing Scheduled Run.

Parameters

| Parameter          | Type                             | Description                                                    |
| ------------------ | -------------------------------- | -------------------------------------------------------------- |
| `scheduledRun`     | `string` \| `ScheduledWorkflows` | The Scheduled Run ID as a string or ScheduledWorkflows object. |
| `update`           | \{ `triggerAt`: `Date`; \}       | The update payload (currently only triggerAt).                 |
| `update.triggerAt` | `Date`                           | -                                                              |

Returns

`Promise`\<`ScheduledWorkflows`\>

A promise that resolves to the updated ScheduledWorkflows object.


---

<!-- Source: https://docs.hatchet.run/reference/typescript/feature-clients/webhooks -->

<a id="webhooksclient"></a>

### Webhooks Client

Client for managing incoming webhooks in Hatchet.

Webhooks allow external systems to trigger Hatchet workflows by sending
HTTP requests to dedicated endpoints. This enables real-time integration
with third-party services like GitHub, Stripe, Slack, or any system that
can send webhook events.

#### Methods

<a id="create"></a>

##### `create()`

Creates a new webhook.

Parameters

| Parameter | Type                   | Description                                   |
| --------- | ---------------------- | --------------------------------------------- |
| `request` | `CreateWebhookOptions` | The request options for the create operation. |

Returns

`Promise`\<`V1Webhook`\>

A promise that resolves to the created webhook.

<a id="delete"></a>

##### `delete()`

Deletes a webhook by its name.

Parameters

| Parameter     | Type     | Description                        |
| ------------- | -------- | ---------------------------------- |
| `webhookName` | `string` | The name of the webhook to delete. |

Returns

`Promise`\<`V1Webhook`\>

A promise that resolves to the deleted webhook.

<a id="get"></a>

##### `get()`

Gets a webhook by its name.

Parameters

| Parameter     | Type     | Description                     |
| ------------- | -------- | ------------------------------- |
| `webhookName` | `string` | The name of the webhook to get. |

Returns

`Promise`\<`V1Webhook`\>

A promise that resolves to the webhook.

<a id="list"></a>

##### `list()`

Lists all webhooks for the current tenant.

Parameters

| Parameter               | Type                                                                                          | Description                         |
| ----------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------- |
| `options?`              | \{ `limit?`: `number`; `offset?`: `number`; `sourceNames?`: ...[]; `webhookNames?`: ...[]; \} | The options for the list operation. |
| `options.limit?`        | `number`                                                                                      | -                                   |
| `options.offset?`       | `number`                                                                                      | -                                   |
| `options.sourceNames?`  | ...[]                                                                                         | -                                   |
| `options.webhookNames?` | ...[]                                                                                         | -                                   |

Returns

`Promise`\<`V1WebhookList`\>

A promise that resolves to the list of webhooks.

<a id="update"></a>

##### `update()`

Updates a webhook by its name.

Parameters

| Parameter     | Type                                  | Description                           |
| ------------- | ------------------------------------- | ------------------------------------- |
| `webhookName` | `string`                              | The name of the webhook to update.    |
| `options`     | `Partial`\<`V1UpdateWebhookRequest`\> | The options for the update operation. |

Returns

`Promise`\<`V1Webhook`\>

A promise that resolves to the updated webhook.


---

<!-- Source: https://docs.hatchet.run/reference/typescript/feature-clients/workers -->

<a id="workersclient"></a>

### Workers Client

The workers client is a client for managing workers programmatically within Hatchet.

#### Methods

<a id="get"></a>

##### `get()`

Get a worker by its ID.

Parameters

| Parameter  | Type     | Description                  |
| ---------- | -------- | ---------------------------- |
| `workerId` | `string` | The ID of the worker to get. |

Returns

`Promise`\<`Worker`\>

A promise that resolves to the worker.

<a id="ispaused"></a>

##### `isPaused()`

Check if a worker is paused.

Parameters

| Parameter  | Type     | Description                    |
| ---------- | -------- | ------------------------------ |
| `workerId` | `string` | The ID of the worker to check. |

Returns

`Promise`\<`boolean`\>

A promise that resolves to true if the worker is paused, false otherwise.

<a id="list"></a>

##### `list()`

List all workers in the tenant.

Returns

`Promise`\<`WorkerList`\>

A promise that resolves to the list of workers.

<a id="pause"></a>

##### `pause()`

Pause a worker.

Parameters

| Parameter  | Type     | Description                    |
| ---------- | -------- | ------------------------------ |
| `workerId` | `string` | The ID of the worker to pause. |

Returns

`Promise`\<`Worker`\>

A promise that resolves to the paused worker.

<a id="unpause"></a>

##### `unpause()`

Unpause a worker.

Parameters

| Parameter  | Type     | Description                      |
| ---------- | -------- | -------------------------------- |
| `workerId` | `string` | The ID of the worker to unpause. |

Returns

`Promise`\<`Worker`\>

A promise that resolves to the unpaused worker.


---

<!-- Source: https://docs.hatchet.run/reference/typescript/feature-clients/workflows -->

<a id="workflowsclient"></a>

### Workflows Client

The workflows client is a client for managing workflows programmatically within Hatchet.

NOTE: that workflows are the declaration, not the individual runs. If you're looking for runs, use the RunsClient instead.

#### Methods

<a id="delete"></a>

##### `delete()`

Delete a workflow by its name, ID, or object.

Parameters

| Parameter  | Type                                                                | Description                       |
| ---------- | ------------------------------------------------------------------- | --------------------------------- |
| `workflow` | `string` \| `BaseWorkflowDeclaration`\<`any`, `any`\> \| `Workflow` | The workflow name, ID, or object. |

Returns

`Promise`\<`void`\>

A promise that resolves to the deleted workflow.

<a id="get"></a>

##### `get()`

Get a workflow by its name, ID, or object.

Parameters

| Parameter  | Type                                                                | Description                       |
| ---------- | ------------------------------------------------------------------- | --------------------------------- |
| `workflow` | `string` \| `BaseWorkflowDeclaration`\<`any`, `any`\> \| `Workflow` | The workflow name, ID, or object. |

Returns

`Promise`\<`Workflow`\>

A promise that resolves to the workflow.

<a id="getworkflowidfromname"></a>

##### `getWorkflowIdFromName()`

Gets the workflow ID from a workflow name, ID, or object.
If the input is not a valid UUID, it will look up the workflow by name.

Parameters

| Parameter  | Type                                                                                           | Description                       |
| ---------- | ---------------------------------------------------------------------------------------------- | --------------------------------- |
| `workflow` | \| `string` \| `WorkflowDefinition` \| `BaseWorkflowDeclaration`\<`any`, `any`\> \| `Workflow` | The workflow name, ID, or object. |

Returns

`Promise`\<`string`\>

The workflow ID as a string.

<a id="list"></a>

##### `list()`

List all workflows in the tenant.

Parameters

| Parameter      | Type                                                              | Description                                            |
| -------------- | ----------------------------------------------------------------- | ------------------------------------------------------ |
| `opts?`        | \{ `limit?`: `number`; `name?`: `string`; `offset?`: `number`; \} | The options for the list operation.                    |
| `opts.limit?`  | `number`                                                          | The number to limit by **Format** int **Default** `50` |
| `opts.name?`   | `string`                                                          | Search by name                                         |
| `opts.offset?` | `number`                                                          | The number to skip **Format** int **Default** `0`      |

Returns

`Promise`\<`WorkflowList`\>

A promise that resolves to the list of workflows.


---

<!-- Source: https://docs.hatchet.run/reference/typescript/Runnables -->

# Runnables

`Runnables` in the Hatchet TypeScript SDK are things that can be run, namely tasks and workflows. The two main types of runnables you'll encounter are:

- `WorkflowDeclaration`, returned by `hatchet.workflow(...)`, which lets you define tasks and call `run()`, `schedule()`, `cron()`, etc.
- `TaskWorkflowDeclaration`, returned by `hatchet.task(...)`, which is a single standalone task that exposes the same execution helpers as a workflow.

<a id="taskworkflowdeclaration"></a>

### TaskWorkflowDeclaration

A standalone task declaration that can be run like a workflow.

`TaskWorkflowDeclaration` is returned by `hatchet.task(...)` and wraps a single
task definition while exposing the same execution helpers as workflows, such as
`run()`, `runNoWait()`, `schedule()`, and `cron()` (inherited from
`BaseWorkflowDeclaration`).

Example:

```typescript
const greet = hatchet.task<{ name: string }, { message: string }>({
  name: "greet",
  fn: async (input) => ({ message: `Hello, ${input.name}!` }),
});

await greet.run({ name: "World" });
const ref = await greet.runNoWait({ name: "World" });
```

#### Methods

<a id="cron"></a>

##### `cron()`

Creates a cron schedule for the task.

Parameters

| Parameter    | Type                | Description                                                 |
| ------------ | ------------------- | ----------------------------------------------------------- |
| `name`       | `string`            | The name of the cron schedule.                              |
| `expression` | `string`            | The cron expression defining the schedule.                  |
| `input`      | `I` & `GlobalInput` | The input data for the task, including global input fields. |
| `options?`   | `RunOpts`           | Optional configuration for this task run.                   |

Returns

`Promise`\<`CronWorkflows`\>

A promise that resolves with the cron workflow details.

Overrides

```ts
BaseWorkflowDeclaration.cron;
```

<a id="delay"></a>

##### `delay()`

Schedules the task to run after a specified delay.

Parameters

| Parameter  | Type                | Description                                                 |
| ---------- | ------------------- | ----------------------------------------------------------- |
| `duration` | `number`            | The delay in seconds before the task should run.            |
| `input`    | `I` & `GlobalInput` | The input data for the task, including global input fields. |
| `options?` | `RunOpts`           | Optional configuration for this task run.                   |

Returns

`Promise`\<`ScheduledWorkflows`\>

A promise that resolves with the scheduled workflow details.

Overrides

```ts
BaseWorkflowDeclaration.delay;
```

<a id="run"></a>

##### `run()`

Triggers a task run and waits for the result.

Parameters

| Parameter  | Type                | Description                                                 |
| ---------- | ------------------- | ----------------------------------------------------------- |
| `input`    | `I` & `GlobalInput` | The input data for the task, including global input fields. |
| `options?` | `RunOpts`           | Optional configuration for this task run.                   |

Returns

`Promise`\<`O` & `Resolved`\<`GlobalOutput`, `MiddlewareAfter`\>\>

A promise that resolves with the task output merged with post-middleware fields.

Overrides

```ts
BaseWorkflowDeclaration.run;
```

<a id="runandwait"></a>

##### `runAndWait()`

Triggers a task run and waits for the result.

Parameters

| Parameter  | Type                | Description                                                 |
| ---------- | ------------------- | ----------------------------------------------------------- |
| `input`    | `I` & `GlobalInput` | The input data for the task, including global input fields. |
| `options?` | `RunOpts`           | Optional configuration for this task run.                   |

Returns

`Promise`\<`O` & `Resolved`\<`GlobalOutput`, `MiddlewareAfter`\>\>

A promise that resolves with the task output merged with post-middleware fields.

Overrides

```ts
BaseWorkflowDeclaration.runAndWait;
```

<a id="runnowait"></a>

##### `runNoWait()`

Triggers a task run without waiting for completion.

Parameters

| Parameter  | Type                | Description                                                 |
| ---------- | ------------------- | ----------------------------------------------------------- |
| `input`    | `I` & `GlobalInput` | The input data for the task, including global input fields. |
| `options?` | `RunOpts`           | Optional configuration for this task run.                   |

Returns

`Promise`\<`WorkflowRunRef`\<`O` & `Resolved`\<..., ...\>\>\>

A WorkflowRunRef containing the run ID and methods to get results.

Overrides

```ts
BaseWorkflowDeclaration.runNoWait;
```

Triggers a task run without waiting for completion.

Parameters

| Parameter  | Type                  | Description                                                 |
| ---------- | --------------------- | ----------------------------------------------------------- |
| `input`    | `I` & `GlobalInput`[] | The input data for the task, including global input fields. |
| `options?` | `RunOpts`             | Optional configuration for this task run.                   |

Returns

`Promise`\<`WorkflowRunRef`\<... & ...\>[]\>

A WorkflowRunRef containing the run ID and methods to get results.

Overrides

```ts
BaseWorkflowDeclaration.runNoWait;
```

<a id="schedule"></a>

##### `schedule()`

Schedules the task to run at a specific date and time.

Parameters

| Parameter   | Type                | Description                                                 |
| ----------- | ------------------- | ----------------------------------------------------------- |
| `enqueueAt` | `Date`              | The date when the task should be triggered.                 |
| `input`     | `I` & `GlobalInput` | The input data for the task, including global input fields. |
| `options?`  | `RunOpts`           | Optional configuration for this task run.                   |

Returns

`Promise`\<`ScheduledWorkflows`\>

A promise that resolves with the scheduled workflow details.

Overrides

```ts
BaseWorkflowDeclaration.schedule;
```

---

<a id="workflowdeclaration"></a>

### WorkflowDeclaration

A Hatchet workflow, which lets you define tasks and perform actions on the workflow.

Workflows in Hatchet represent coordinated units of work that can be triggered,
scheduled, or run on a cron schedule. Each workflow can contain multiple tasks
that can be arranged in dependencies (DAGs), with customized retry behavior,
timeouts, concurrency controls, and more.

Example:

```typescript
import { hatchet } from "./hatchet-client";

type MyInput = { name: string };

const workflow = hatchet.workflow({
  name: "my-workflow",
});

workflow.task({
  name: "greet",
  fn: async (input) => {
    return { message: `Hello, ${input.name}!` };
  },
});

// Run the workflow
await workflow.run({ name: "World" });
```

Workflows support various execution patterns, including:

- One-time execution with `run()` and `runNoWait()`
- Scheduled execution with `schedule()`
- Cron-based recurring execution with `cron()`
- Bulk execution by passing an array input to `run()` and `runNoWait()`

Tasks within workflows can be defined with `workflow.task()` or
`workflow.durableTask()` and arranged into complex dependency patterns.

#### Methods

<a id="durabletask"></a>

##### `durableTask()`

Adds a durable task to the workflow.
The return type will be either the property on O that corresponds to the task name,
or if there is no matching property, the inferred return type of the function.

Parameters

| Parameter | Type                                                               | Description                     |
| --------- | ------------------------------------------------------------------ | ------------------------------- |
| `options` | `Omit`\<`CreateWorkflowTaskOpts`\<`I`, `TO`\>, `"fn"`\> & `object` | The task configuration options. |

Returns

`CreateWorkflowDurableTaskOpts`\<`I`, `TO`\>

The task options that were added.

<a id="onfailure"></a>

##### `onFailure()`

Adds an onFailure task to the workflow.
This will only run if any task in the workflow fails.

Parameters

| Parameter | Type                                                                                                                                                                       | Description                     |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `options` | \| `Omit`\<`CreateOnFailureTaskOpts`\<..., ...\>, `"fn"`\> & `object` \| [`TaskWorkflowDeclaration`](#taskworkflowdeclaration)\<`any`, `any`, \{ \}, \{ \}, \{ \}, \{ \}\> | The task configuration options. |

Returns

`CreateWorkflowTaskOpts`\<`I`, `TaskOutputType`\<`O`, `Name`, `L`\>\>

The task options that were added.

<a id="onsuccess"></a>

##### `onSuccess()`

Adds an onSuccess task to the workflow.
This will only run if all tasks in the workflow complete successfully.

Parameters

| Parameter | Type                                                                                                                                                                       | Description                     |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `options` | \| [`TaskWorkflowDeclaration`](#taskworkflowdeclaration)\<`any`, `any`, \{ \}, \{ \}, \{ \}, \{ \}\> \| `Omit`\<`CreateOnSuccessTaskOpts`\<..., ...\>, `"fn"`\> & `object` | The task configuration options. |

Returns

`CreateWorkflowTaskOpts`\<`I`, `TaskOutputType`\<`O`, `Name`, `L`\>\>

The task options that were added.

<a id="task"></a>

##### `task()`

Adds a task to the workflow.
The return type will be either the property on O that corresponds to the task name,
or if there is no matching property, the inferred return type of the function.

Parameters

| Parameter | Type                                                                                                                                                                   | Description                     |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| `options` | \| `Omit`\<`CreateWorkflowTaskOpts`\<..., ...\>, `"fn"`\> & `object` \| [`TaskWorkflowDeclaration`](#taskworkflowdeclaration)\<`I`, `TO`, \{ \}, \{ \}, \{ \}, \{ \}\> | The task configuration options. |

Returns

`CreateWorkflowTaskOpts`\<`I`, `TO`\>

The task options that were added.

## Functions

<a id="createdurabletaskworkflow"></a>

### `CreateDurableTaskWorkflow()`

Creates a new durable task workflow declaration with types inferred from the function parameter.

Parameters

| Parameter | Type                                                                     | Description                             |
| --------- | ------------------------------------------------------------------------ | --------------------------------------- |
| `options` | `object` & `Omit`\<`CreateWorkflowDurableTaskOpts`\<`I`, `O`\>, `"fn"`\> | The durable task configuration options. |
| `client?` | `IHatchetClient`                                                         | Optional Hatchet client instance.       |

Returns

[`TaskWorkflowDeclaration`](#taskworkflowdeclaration)\<`I`, `O`\>

A new TaskWorkflowDeclaration with inferred types.

---

<a id="createtaskworkflow"></a>

### `CreateTaskWorkflow()`

Creates a new task workflow declaration with types inferred from the function parameter.

Parameters

| Parameter | Type                                                              | Description                       |
| --------- | ----------------------------------------------------------------- | --------------------------------- |
| `options` | `object` & `Omit`\<`CreateTaskWorkflowOpts`\<`I`, `O`\>, `"fn"`\> | The task configuration options.   |
| `client?` | `IHatchetClient`                                                  | Optional Hatchet client instance. |

Returns

[`TaskWorkflowDeclaration`](#taskworkflowdeclaration)\<`I`, `O`\>

A new TaskWorkflowDeclaration with inferred types.

---

<a id="createworkflow"></a>

### `CreateWorkflow()`

Creates a new workflow instance.

Parameters

| Parameter | Type                 | Description                                                                                                                             |
| --------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `options` | `CreateWorkflowOpts` | The options for creating the workflow. Optionally include a Zod schema via the `input` field to generate a JSON Schema for the backend. |
| `client?` | `IHatchetClient`     | Optional Hatchet client instance.                                                                                                       |

Returns

[`WorkflowDeclaration`](#workflowdeclaration)\<`I`, `O`\>

A new Workflow instance.


---

<!-- Source: https://docs.hatchet.run/reference/cli/index -->

# Hatchet CLI Setup & Installation

> **Warning:** The Hatchet CLI is currently in beta and may have breaking changes in future
>   releases.

The Hatchet CLI is a command-line tool with utilities for running workers locally, interacting with a running Hatchet deployment, and running a local Hatchet instance for development.

## Features

- **Quickstarts**: the `hatchet quickstart` command sets up a local Hatchet instance with a sample project to help you get started quickly.

- **Local worker reloading**: the [`hatchet worker dev`](/cli/running-workers-locally) command lets you run a worker locally with automatic reloading when code changes are detected.

- **A full built-in TUI**: the [`hatchet tui`](/cli/tui) command lets you interact with your Hatchet deployment through a terminal user interface (TUI) that provides real-time observability into tasks, workflows, workers, and more.

- **Profiles**: the [`hatchet profile`](/cli/profiles) commands allow you to manage multiple Hatchet instances and tenants with named profiles, making it easy to switch between different environments.

## Installation

The recommended way to install the Hatchet CLI is via our install script or Homebrew:

#### Native Install (Recommended)

**MacOS, Linux, WSL**

```sh
    curl -fsSL https://install.hatchet.run/install.sh | bash
```

#### Homebrew

**MacOS**

```sh
    brew install hatchet-dev/hatchet/hatchet --cask
```

## Verifying Installation

After installation, verify that the Hatchet CLI is installed correctly by checking its version:

```sh
hatchet --version
```


---

<!-- Source: https://docs.hatchet.run/reference/cli/profiles -->

# Profiles

The Hatchet CLI supports managing multiple Hatchet instances and tenants using named profiles. This feature makes it easy to switch between different environments, such as development, staging, and production.

## Creating a Profile

You can create a new profile using the `hatchet profile add` command. You will need to provide a Hatchet API token for the profile.

```sh
hatchet profile add
```

This command will prompt you to enter the API token followed by the profile name. You can also provide these as flags:

```sh
hatchet profile add --name [name] --token [token]
```

## Listing Profiles

You can list all the profiles you have configured using the `hatchet profile list` command:

```sh
hatchet profile list
```

This will display all configured profiles, with the default profile marked with `(default)` if one is set.

## Setting a Default Profile

You can set a profile as the default using the `hatchet profile set-default` command. The default profile will be automatically used when no profile is specified with the `--profile` flag.

```sh
# Set default profile interactively (prompts for selection)
hatchet profile set-default

# Set a specific profile as default
hatchet profile set-default --name [name]
```

Once a default profile is set, you can run commands without specifying the `--profile` flag:

```sh
# Uses the default profile
hatchet worker dev
```

To unset the default profile:

```sh
hatchet profile unset-default
```

## Using a Profile

To use a specific profile for your Hatchet CLI commands, you can specify the profile name using the `--profile` flag. This overrides the default profile if one is set.

```sh
hatchet worker dev --profile [name]
```

## Updating a Profile

You can update an existing profile using the `hatchet profile update` command. This allows you to change the API token associated with a profile.

```sh
hatchet profile update
```

## Deleting a Profile

You can delete a profile using the `hatchet profile remove` command:

```sh
hatchet profile remove
```

If you remove a profile that is set as the default, the default profile setting will be automatically cleared.


---

<!-- Source: https://docs.hatchet.run/reference/cli/running-hatchet-locally -->

# Running Hatchet Locally

The Hatchet CLI provides the `hatchet server` commands to run a local instance of Hatchet for development and testing purposes. This local instance relies on Docker to run the necessary services.

## Prerequisites

Before running Hatchet locally, you must have Docker installed on your machine. You can download Docker from [here](https://www.docker.com/get-started).

## Starting Hatchet Locally

To start a local instance of Hatchet, run the following command in your terminal:

```sh
hatchet server start
```

## Stopping Hatchet Locally

To stop the local Hatchet instance, run the following command:

```sh
hatchet server stop
```

## Reference

#### `hatchet server start`

```txt
Start a local Hatchet server environment using Docker containers. This command will start both a PostgreSQL database and a Hatchet server instance, automatically creating a local profile for easy access.

Usage:
  hatchet server start [flags]

Examples:
  # Start server with default settings (port 8888)
  hatchet server start

  # Start server with custom dashboard port
  hatchet server start --dashboard-port 9000

  # Start server with custom ports and project name
  hatchet server start --dashboard-port 9000 --grpc-port 8077 --project-name my-hatchet

  # Start server with custom profile name
  hatchet server start --profile my-local

Flags:
  -d, --dashboard-port int    Port for the Hatchet dashboard (default: auto-detect starting at 8888)
  -g, --grpc-port int         Port for the Hatchet gRPC server (default: auto-detect starting at 7077)
  -h, --help                  help for start
  -n, --profile string        Name for the local profile (default: local) (default "local")
  -p, --project-name string   Docker project name for containers (default: hatchet-cli)

Global Flags:
  -v, --version   The version of the hatchet cli.
```

#### `hatchet server stop`

```txt
Stop a local Hatchet server environment that was started using Docker containers with the 'hatchet server start' command.

Usage:
  hatchet server stop [flags]

Examples:
  # Stop the local Hatchet server
  hatchet server stop

  # Stop the local Hatchet server with a custom project name
  hatchet server stop --project-name my-hatchet

Flags:
  -h, --help                  help for stop
  -p, --project-name string   Docker project name for containers (default: hatchet-cli)

Global Flags:
  -v, --version   The version of the hatchet cli.
```


---

<!-- Source: https://docs.hatchet.run/reference/cli/running-workers-locally -->

# Running Workers Locally

The Hatchet CLI provides the `hatchet worker` commands to run Hatchet workers locally for development and testing purposes.

## Setting up a hatchet.yaml file

> **Info:** If you've set up a project using `hatchet quickstart`, a `hatchet.yaml` file
>   is already created for you in the project directory.

The `hatchet worker` commands rely on a `hatchet.yaml` configuration file to define the worker settings. You can create a `hatchet.yaml` file in your project directory which resembles the following (you will need to adjust the `preCmds` and `runCmd` fields to match your project's setup):

#### Python

```yaml
dev:
  preCmds: ["poetry install"]
  runCmd: "poetry run python src/worker.py"
  files:
    - "**/*.py"
    - "!**/__pycache__/**"
    - "!**/.venv/**"
  reload: true
```

#### Typescript

```yaml
dev:
  preCmds: ["pnpm install"]
  runCmd: "pnpm start"
  files:
    - "**/*.ts"
    - "!**/node_modules/**"
  reload: true
```

#### Go

```yaml
dev:
  preCmds: ["go mod download"]
  runCmd: "go run ./cmd/worker"
  files:
    - "**/*.go"
  reload: true
```

## Running a worker

Once you have a `hatchet.yaml` file set up, you can run a worker locally using the following command:

```sh
hatchet worker dev
```

To run a worker with a specific profile, you can run:

```sh
hatchet worker dev --profile <profile-name>
```

### Disabling auto-reload

If you want to run the worker without auto-reloading on file changes, you can set the `dev.reload` field to `false` in your `hatchet.yaml` file:

```yaml
dev:
  reload: false
```

Or you can pass the `--no-reload` flag when running the worker:

```sh
hatchet worker dev --no-reload
```

### Overriding the run command

You can override the `runCmd` specified in the `hatchet.yaml` file by using the `--run-cmd` flag:

```sh
hatchet worker dev --run-cmd "npm run dev"
```


---

<!-- Source: https://docs.hatchet.run/reference/cli/triggering-workflows -->

# Triggering Workflows

You can use the `hatchet trigger` command to trigger workflows locally for testing and development purposes. This command allows you to set up triggers in your `hatchet.yaml` file that define how to run specific workflows.

## Example

In your `hatchet.yaml` file, you can define a trigger for a simple workflow like this:

```yaml
triggers:
  - name: "simple"
    command: "poetry run python src/run.py"
    description: "Trigger a simple workflow"
```

Then, you can select this trigger when running the `hatchet trigger` command:

```sh
hatchet trigger simple
```

Or just `hatchet trigger`, which will prompt you to select a trigger interactively.


---

<!-- Source: https://docs.hatchet.run/reference/cli/tui -->

# Using the Hatchet TUI

The Hatchet CLI includes a built-in terminal user interface (TUI) that you can use to interact with your Hatchet deployment directly from the terminal. The TUI provides real-time observability into tasks, workflows, workers, and more:

```sh
hatchet tui
```

# Features

> **Info:** You can access help documentation by pressing the `h` key within the TUI. This
>   will display a list of available commands and their descriptions.

## Runs View

The Runs view provides a similar experience to the Runs page in the Hatchet dashboard. You can filter and list runs based on filters.

<video controls preload="auto">
  <source src="../../../public/cli/runs_view.mp4" type="video/mp4" />
  Your browser does not support the video tag
</video>

## Workflows View

The Workflows view allows you to see the list of workflows defined in your Hatchet deployment. You can view some details about each workflow, along with recent runs:

<video controls preload="auto">
  <source src="../../../public/cli/workflows_view.mp4" type="video/mp4" />
  Your browser does not support the video tag
</video>

## Workers View

The Workers view shows the status of workers connected to your Hatchet deployment. You can see which workers are online, their registered workflows, and some other information.

<video controls preload="auto">
  <source src="../../../public/cli/workers_view.mp4" type="video/mp4" />
  Your browser does not support the video tag
</video>


---

<!-- Source: https://docs.hatchet.run/contributing/index -->

# Contributing

> **Note:** this guide### Setup

1. Start the Database and Queue services:

```sh
task start-db
```

2. Install dependencies, run migrations, generate encryption keys, and seed the database:

```sh
task setup
```

### Starting the dev server

Start the Hatchet engine, API server, dashboard, and Prisma studio:

```sh
task start-dev # or task start-dev-tmux if you want to use tmux panes
```

### Creating and testing workflows

To create and test workflows, run the examples in the `./examples` directory.

You will need to add the tenant (output from the `task seed-dev` command) to the `.env` file in each example directory. An example `.env` file for the `./examples/simple` directory can be generated via:

```sh
alias get_token='go run ./cmd/hatchet-admin token create --name local --tenant-id 707d0855-80ab-4e1f-a156-f1c4546cbf52'

cat > ./examples/simple/.env <

# optional
OTEL_EXPORTER_OTLP_HEADERS=<optional-headers>

# optional
OTEL_EXPORTER_OTLP_ENDPOINT=<collector-url>
```

### CloudKMS

CloudKMS can be used to generate master encryption keys:

```
gcloud kms keyrings create "development" --location "global"
gcloud kms keys create "development" --location "global" --keyring "development" --purpose "encryption"
gcloud kms keys list --location "global" --keyring "development"
```

From the last step, copy the Key URI and set the following environment variable:

```
SERVER_ENCRYPTION_CLOUDKMS_KEY_URI=gcp-kms://projects//locations/global/keyRings/development/cryptoKeys/development
```

Generate a service account in GCP which can encrypt/decrypt on CloudKMS, then download a service account JSON file and set it via:

```
SERVER_ENCRYPTION_CLOUDKMS_CREDENTIALS_JSON='{...}'
```

## Issues

### Query engine leakage

Sometimes the spawned query engines from Prisma don't get killed when hot reloading. You can run `task kill-query-engines` on OSX to kill the query engines.

Make sure you call `.Disconnect` on the database config object when writing CLI commands which interact with the database. If you don't, and you try to wrap these CLI commands in a new command, it will never exit, for example:

```
export HATCHET_CLIENT_TOKEN="$(go run ./cmd/hatchet-admin token create --tenant-id <tenant>)"
```


---

<!-- Source: https://docs.hatchet.run/contributing/github-app-setup -->

## Setup

### Using `ngrok`

You can use `ngrok` to expose a local port to the internet to accept incoming webhooks from Github. To do this, run the following:

```sh
task start-ngrok
```

Make note of the `https` URL as you will need it later.

### Github App Creation

To create a Github app that can read from your repositories, navigate to your organization settings page (alternately, you can navigate to your personal settings page) and select **Developer Settings** in the sidebar. Go to **Github Apps** and select **New Github App**. You should use the following settings:

- Homepage URL: you can set this as https://hatchet.run, or some other domain for your organization.
- Callback URL: `<protocol>://<your-domain>/api/v1/users/github-app/callback`
- The **Request user authorization (OAuth) during installation** checkbox should be checked.
- Webhook URL: `<protocol>://<your-https-ngrok-address>/api/v1/github/webhook`
- Webhook secret: generate a random webhook secret for your domain, for example by running `cat /dev/urandom | base64 | head -c 32`. **Make note of this secret, as you will need it later**.
- Permissions:
  - **Repository:**
    - **Checks (Read & write)**: required to write Github checks for each commit/PR.
    - **Contents (Read):** required for Hatchet to read files from the repository.
    - **Metadata (Read-only):** mandatory, required for Github apps that integrate with repositories.
    - **Pull Requests (Read & write):** required for Hatchet to add comments to Github PRs, and to create PRs.
    - **Webhooks (Read & write):** required for Hatchet to create a Github repository webhooks that notify the Hatchet instance when PRs are updated.
  - **Account:**
    - **Email addresses (read-only)**: required for Hatchet to read your Github email address for authentication.

### Creating a Secret and Private Key

After creating the Github App, create the following:

- In the "Client secrets" section, select **Generate a new client secret**. You will need this secret in the following section.
- In the "Private keys" section, download a new private key for your app. You will need this private key in the following section.

### Private Keys and Environment Variables

After creating the private key, you can place it somewhere in your filesystem and set the `SERVER_VCS_GITHUB_APP_SECRET_PATH` environment variable to the path of the private key.

Make sure the following environment variables are set:

```txt
SERVER_VCS_KIND=github
SERVER_VCS_GITHUB_ENABLED=true
SERVER_VCS_GITHUB_APP_CLIENT_ID=<client-id>
SERVER_VCS_GITHUB_APP_CLIENT_SECRET=<client-secret>
SERVER_VCS_GITHUB_APP_NAME=<app-name>
SERVER_VCS_GITHUB_APP_WEBHOOK_SECRET=<webhook-secret>
SERVER_VCS_GITHUB_APP_WEBHOOK_URL=<webhook-url>
SERVER_VCS_GITHUB_APP_ID=<app-id>
SERVER_VCS_GITHUB_APP_SECRET_PATH=<path-to-pem-file>
```


---

<!-- Source: https://docs.hatchet.run/contributing/sdks -->

# SDKs

This document tracks the feature support of the various SDKs, and aims to consolidate the expected behavior around environment variables and configuration loading.

## Environment Variables

Each SDK should support the following environment variables:

| Variable                          | Description                                                                                                                                            | Required                                                                                                | Default                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| `HATCHET_CLIENT_TOKEN`            | The tenant-scoped API token to use.                                                                                                                    | Yes                                                                                                     | N/A                                       |
| `HATCHET_CLIENT_HOST_PORT`        | The host and port of the Hatchet server to connect to, in `host:port` format. SDKs should handle schemes and trailing slashes, i.e. `https://host:port | No                                                                                                      | Automatically detected in new tokens.     |
| `HATCHET_CLIENT_TLS_STRATEGY`     | The TLS strategy to use. Valid values are `none`, `tls`, and `mtls`.                                                                                   | No                                                                                                      | `tls`                                     |
| `HATCHET_CLIENT_TLS_CERT_FILE`    | The path to the TLS client certificate file to use.                                                                                                    | Only if strategy is set to `mtls`                                                                       | N/A                                       |
| `HATCHET_CLIENT_TLS_CERT`         | The TLS client key file to use.                                                                                                                        | Only if strategy is set to `mtls`                                                                       | N/A                                       |
| `HATCHET_CLIENT_TLS_KEY_FILE`     | The path to the TLS client key file to use.                                                                                                            | Only if strategy is set to `mtls`                                                                       | N/A                                       |
| `HATCHET_CLIENT_TLS_KEY`          | The TLS client key to use.                                                                                                                             | Only if strategy is set to `mtls`                                                                       | N/A                                       |
| `HATCHET_CLIENT_TLS_ROOT_CA_FILE` | The path to the TLS root CA file to use.                                                                                                               | Only if the server certificate is not signed by a public authority that's available to your environment | N/A                                       |
| `HATCHET_CLIENT_TLS_ROOT_CA`      | The TLS root CA to use.                                                                                                                                | Only if the server certificate is not signed by a public authority that's available to your environment | N/A                                       |
| `HATCHET_CLIENT_TLS_SERVER_NAME`  | The TLS server name to use.                                                                                                                            | No                                                                                                      | Defaults to the `host` of the `host:port` |

The following environment variables are deprecated:

| Variable                   | Description           | Explanation                    |
| -------------------------- | --------------------- | ------------------------------ |
| `HATCHET_CLIENT_TENANT_ID` | The tenant ID to use. | This is now part of the token. |

## Compatibility Matrices

### DAGs

Whether the SDKs support full DAG-style execution.

| SDK            | DAGs? | Notes |
| -------------- | ----- | ----- |
| Go SDK         | Yes   |       |
| Python SDK     | Yes   |       |
| Typescript SDK | Yes   |       |

### Timeouts

Whether the SDKs support setting timeouts and cancelling after timeouts.

| SDK            | Timeouts? | Step cancellation? | Notes                                          |
| -------------- | --------- | ------------------ | ---------------------------------------------- |
| Go SDK         | Yes       | Yes                |                                                |
| Python SDK     | Yes       | Yes                | If thread is blocking, this won't be respected |
| Typescript SDK | Yes       | Unknown            |                                                |

### Middleware

Whether the SDKs support setting middleware.

| SDK            | Middleware? | Notes |
| -------------- | ----------- | ----- |
| Go SDK         | Yes         |       |
| Python SDK     | No          |       |
| Typescript SDK | No          |       |

### Separately Registering and Calling Actions

Whether the SDKs support separately registering and calling actions, instead of defining them inline in the workflows.

| SDK            | Supported? | Notes |
| -------------- | ---------- | ----- |
| Go SDK         | Yes        |       |
| Python SDK     | No         |       |
| Typescript SDK | No         |       |

### Custom Services

Whether the SDKs support defining services to logically separate workflows and actions.

| SDK            | Supported? | Notes |
| -------------- | ---------- | ----- |
| Go SDK         | Yes        |       |
| Python SDK     | No         |       |
| Typescript SDK | No         |       |

### Scheduled Workflows

Whether the SDKs support defining scheduled workflows.

| SDK            | Supported? | Notes |
| -------------- | ---------- | ----- |
| Go SDK         | Yes        |       |
| Python SDK     | No         |       |
| Typescript SDK | No         |       |


---

<!-- Source: https://docs.hatchet.run/agent-instructions/setup-cli -->

# Install and Set Up the Hatchet CLI

These are instructions for an AI agent to install the Hatchet CLI and configure a profile. Follow each step in order.

## Step 1: Check if Already Installed

```bash
hatchet --version
```

If this prints a version number, the CLI is already installed. Skip to Step 3 (profile setup).

If the command is not found, proceed to Step 2.

## Step 2: Install the CLI

On macOS, Linux, or WSL:

```bash
curl -fsSL https://install.hatchet.run/install.sh | bash
```

Alternatively, on macOS via Homebrew:

```bash
brew install hatchet-dev/hatchet/hatchet --cask
```

After installation, verify it worked:

```bash
hatchet --version
```

## Step 3: Check for Existing Profiles

```bash
hatchet profile list
```

If a profile already exists that connects to the correct Hatchet instance, note its name and use it as the `-p` flag in all subsequent commands. You are done.

If no profiles exist or the correct one is missing, proceed to Step 4.

## Step 4: Create a Profile

You need a Hatchet API token. Ask the user for one if you do not have it. Then create a profile:

```bash
hatchet profile add --name HATCHET_PROFILE --token 
```

Replace `HATCHET_PROFILE` with a descriptive name (e.g. `local`, `staging`, `production`) and `` with the actual token.

To set it as the default profile (so `-p` is optional in future commands):

```bash
hatchet profile set-default --name HATCHET_PROFILE
```

## Step 5: Verify Connectivity

Test that the profile works by listing workflows:

```bash
hatchet runs list -o json -p HATCHET_PROFILE --since 1h --limit 1
```

If this returns a JSON response (even with an empty rows list), the profile is correctly configured and connected.

## Troubleshooting

- **"command not found"** after install: The CLI binary may not be on your PATH. Check `~/.local/bin/hatchet` or re-run the install script.
- **Authentication error**: The API token may be invalid or expired. Ask the user for a new token and run `hatchet profile update`.
- **Connection refused**: The Hatchet server may not be running. For local development, start it with `hatchet server start`.


---

<!-- Source: https://docs.hatchet.run/agent-instructions/start-worker -->

# Start a Hatchet Worker in Dev Mode

These are instructions for an AI agent to start a Hatchet worker using the CLI. Follow each step in order.

## Prerequisites

You need a `hatchet.yaml` file in the project root. If one does not exist, create it with the following structure:

```yaml
dev:
  runCmd: "python src/worker.py"
  files:
    - "**/*.py"
  reload: true
```

Adjust `runCmd` to match the project's language and entry point:

- Python: `poetry run python src/worker.py` or `python src/worker.py`
- TypeScript/Node: `npx ts-node src/worker.ts` or `npm run dev`
- Go: `go run ./cmd/worker`

The `files` list contains glob patterns for file watching. The `reload: true` setting enables automatic worker restart when watched files change.

## Start the Worker

Run the following command in a **background terminal** (the worker is a long-running process that must stay alive):

```bash
hatchet worker dev -p HATCHET_PROFILE
```

The worker will connect to Hatchet using the specified profile and begin listening for tasks.

## Important Notes

- The worker **must be running** before you trigger any workflows. If a workflow is triggered with no worker running, tasks will remain in QUEUED status indefinitely.
- When `reload: true` is set, the worker automatically restarts when any watched file changes. This means you can edit task code and the worker picks up changes without manual restart.
- To disable auto-reload, add `--no-reload`.
- To override the run command without editing `hatchet.yaml`, use `--run-cmd "your command here"`.
- If the worker fails to start, check that the profile exists (`hatchet profile list`) and that the Hatchet server is reachable.

## Optional: Pre-commands

You can add setup commands that run before the worker starts:

```yaml
dev:
  preCmds:
    - "poetry install"
    - "npm install"
  runCmd: "poetry run python src/worker.py"
  files:
    - "**/*.py"
  reload: true
```

These run once each time the worker starts (including on reload).


---

<!-- Source: https://docs.hatchet.run/agent-instructions/trigger-and-watch -->

# Trigger a Workflow and Watch for Completion

These are instructions for an AI agent to trigger a Hatchet workflow and poll until it completes. Follow each step in order.

## Prerequisites

- A Hatchet worker must be running (`hatchet worker dev -p HATCHET_PROFILE`). If no worker is running, the task will stay QUEUED forever.
- You must know the workflow name and have the input JSON ready.

## Step 1: Write Input to a Temp File

Write the input JSON to a uniquely-named temp file to avoid collisions with other sessions:

```bash
HATCHET_INPUT_FILE="/tmp/hatchet-input-$(date +%s)-$$.json"
cat > "$HATCHET_INPUT_FILE" << 'ENDJSON'
INPUT_JSON
ENDJSON
```

Replace `INPUT_JSON` with the actual JSON payload for the workflow.

## Step 2: Trigger the Workflow

```bash
RUN_ID=$(hatchet trigger manual -w WORKFLOW_NAME -j "$HATCHET_INPUT_FILE" -p HATCHET_PROFILE -o json | jq -r '.runId')
```

The `-o json` flag makes the command output `{"runId": "...", "workflow": "..."}` to stdout. The command above captures the run ID directly into `$RUN_ID` for the next steps.

## Step 3: Poll for Completion

Run the following command every 5 seconds until the run reaches a terminal state:

```bash
hatchet runs get  -o json -p HATCHET_PROFILE
```

Parse the JSON response and check the status:

- Look at `.run.status` for the overall run status and `.tasks[].status` for individual task statuses.
- Terminal statuses are: `COMPLETED`, `FAILED`, `CANCELLED`.
- Non-terminal statuses are: `QUEUED`, `RUNNING`. Keep polling if you see these.

## Step 4: Handle Failure

If the run status is `FAILED`, gather diagnostic information:

### Fetch logs

```bash
hatchet runs logs  -p HATCHET_PROFILE
```

This prints application-level log output (e.g. print statements, logger calls from your task code). Look for error messages, stack traces, or unexpected output.

### Fetch events

```bash
hatchet runs events  -o json -p HATCHET_PROFILE
```

This returns the lifecycle event log showing how the task was dispatched, started, and failed. Look at the `eventType` and `message` fields to understand the failure sequence.

## Step 5: Clean Up

```bash
rm -f "$HATCHET_INPUT_FILE"
```

## Common Issues

- **Task stays QUEUED**: The worker is not running, or the workflow/task name does not match what the worker registered. Start or restart the worker.
- **Task FAILED immediately**: Check the logs for a stack trace. The task code likely threw an exception.
- **Task CANCELLED**: Something cancelled the run externally. Check events to see the cancellation source.


---

<!-- Source: https://docs.hatchet.run/agent-instructions/debug-run -->

# Debug a Hatchet Run

These are instructions for an AI agent to diagnose why a Hatchet run failed, is stuck, or behaved unexpectedly. Follow each step in order.

## Step 1: Get Run State

```bash
hatchet runs get RUN_ID -o json -p HATCHET_PROFILE
```

Examine the JSON response:

- `.run.status` -- the overall run status (`QUEUED`, `RUNNING`, `COMPLETED`, `FAILED`, `CANCELLED`)
- `.run.displayName` -- the workflow name
- `.run.input` -- the input that was provided when the workflow was triggered
- `.tasks[]` -- each task in the run, with its own `status`, `displayName`, and `output` or `errorMessage`
- `.tasks[].startedAt` and `.tasks[].finishedAt` -- timing information

## Step 2: Get Event Log

```bash
hatchet runs events RUN_ID -o json -p HATCHET_PROFILE
```

The event log shows the full lifecycle of the run. Each event has:

- `eventType` -- what happened (e.g. `QUEUED`, `STARTED`, `FINISHED`, `FAILED`, `CANCELLED`)
- `message` -- human-readable description
- `taskDisplayName` -- which task the event belongs to
- `timestamp` -- when it happened

Read events in chronological order to understand the sequence of what happened.

## Step 3: Get Logs

```bash
hatchet runs logs RUN_ID -p HATCHET_PROFILE
```

This prints the application-level log output from the task code (e.g. print statements, logger calls). For multi-task (DAG) runs, logs from all tasks are merged and sorted by timestamp with task name prefixes.

## Diagnostic Cheat Sheet

### Task stuck in QUEUED (no STARTED event)

The task was never picked up by a worker. Likely causes:

- **No worker is running.** Start one with `hatchet worker dev -p HATCHET_PROFILE`.
- **Worker does not register this task type.** The task name in the workflow definition must match what the worker code registers. Check the worker startup logs.
- **Worker is connected to a different tenant/profile.** Verify the worker and the trigger use the same `-p` profile.

### Task FAILED

Check the logs output from Step 3 for a stack trace or error message. Common causes:

- Unhandled exception in the task code.
- Timeout exceeded.
- A dependency (database, API, etc.) was unreachable.

The events from Step 2 will show a `FAILED` event with an error message.

### Task CANCELLED

Check the events for a `CANCELLED` event. The message field indicates the cancellation source:

- Manual cancellation via the dashboard or CLI.
- Parent workflow cancellation (for DAG workflows).
- Timeout-based cancellation.

### Run COMPLETED but output is wrong

If the run completed but produced unexpected results:

1. Check `.tasks[].output` in the run state (Step 1) to see what each task returned.
2. Check the logs (Step 3) to trace the execution flow.
3. Check `.run.input` to verify the correct input was provided.

### Slow execution

Compare `startedAt` and `finishedAt` timestamps for each task in Step 1 to identify which task is the bottleneck. Check if there is a long gap between the run being triggered and the first task starting (indicates queuing delay, possibly due to worker capacity).


---

<!-- Source: https://docs.hatchet.run/agent-instructions/replay-run -->

# Replay a Hatchet Run

These are instructions for an AI agent to replay a previously executed Hatchet run, optionally with modified input. Follow each step in order.

## Step 1: Inspect the Original Run

First, understand what happened in the original run:

```bash
hatchet runs get RUN_ID -o json -p HATCHET_PROFILE
```

From the response, note:

- `.run.displayName` -- the workflow name (needed if re-triggering with new input)
- `.run.input` -- the original input JSON
- `.run.status` -- why you might be replaying (e.g. `FAILED`)
- `.tasks[].status` and `.tasks[].errorMessage` -- which specific tasks failed and why

## Step 2a: Replay with the Same Input

If you want to re-run the exact same workflow with the same input (e.g. after fixing a bug in the task code):

```bash
hatchet runs replay RUN_ID -o json -p HATCHET_PROFILE
```

This creates a new run of the same workflow with the same input. The response includes the new run IDs in `.ids[]`.

## Step 2b: Replay with New Input

If you need to change the input (e.g. fixing bad input data), you must trigger a new run instead of using replay:

Write the new input JSON to a uniquely-named temp file:

```bash
HATCHET_INPUT_FILE="/tmp/hatchet-input-$(date +%s)-$$.json"
cat > "$HATCHET_INPUT_FILE" << 'ENDJSON'
NEW_INPUT_JSON
ENDJSON
```

Then trigger a fresh run using the workflow name from Step 1:

```bash
RUN_ID=$(hatchet trigger manual -w WORKFLOW_NAME -j "$HATCHET_INPUT_FILE" -p HATCHET_PROFILE -o json | jq -r '.runId')
```

Clean up the temp file:

```bash
rm -f "$HATCHET_INPUT_FILE"
```

## Step 3: Watch the New Run

After either Step 2a or 2b, you have a new run ID. Poll for completion:

```bash
hatchet runs get  -o json -p HATCHET_PROFILE
```

Check `.run.status` and `.tasks[].status` every 5 seconds until all reach a terminal state (`COMPLETED`, `FAILED`, `CANCELLED`).

If the new run also fails, use the debug instructions:

1. `hatchet runs logs  -p HATCHET_PROFILE` for application logs
2. `hatchet runs events  -o json -p HATCHET_PROFILE` for lifecycle events

## Common Replay Workflow

The typical flow when an agent is iterating on task code:

1. Trigger a run and it fails
2. Read the logs/events to understand why
3. Fix the code (the worker auto-reloads if `reload: true` in `hatchet.yaml`)
4. Replay the run with `hatchet runs replay RUN_ID -o json -p HATCHET_PROFILE`
5. If it fails again, repeat from step 2

