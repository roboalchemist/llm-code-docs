# Source: https://developers.cloudflare.com/workflows/python/index.md

---
title: Python Workflows SDK · Cloudflare Workflows docs
description: >-
  Workflow entrypoints can be declared using Python. To achieve this, you can
  export a WorkflowEntrypoint that runs on the Cloudflare Workers platform.

  Refer to Python Workers for more information about Python on the Workers
  runtime.
lastUpdated: 2026-02-09T12:13:25.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/workflows/python/
  md: https://developers.cloudflare.com/workflows/python/index.md
---

Workflow entrypoints can be declared using Python. To achieve this, you can export a `WorkflowEntrypoint` that runs on the Cloudflare Workers platform. Refer to [Python Workers](https://developers.cloudflare.com/workers/languages/python) for more information about Python on the Workers runtime.

Python Workflows are in beta, as well as the underlying platform.

Join the #python-workers channel in the [Cloudflare Developers Discord](https://discord.cloudflare.com/) and let us know what you'd like to see next.

## Get Started

The main entrypoint for a Python workflow is the [`WorkflowEntrypoint`](https://developers.cloudflare.com/workflows/build/workers-api/#workflowentrypoint) class. Your workflow logic should exist inside the [`run`](https://developers.cloudflare.com/workflows/build/workers-api/#run) handler.

```python
from workers import WorkflowEntrypoint


class MyWorkflow(WorkflowEntrypoint):
    async def run(self, event, step):
        # steps here
```

For example, a Workflow may be defined as:

```python
from workers import Response, WorkflowEntrypoint


class PythonWorkflowStarter(WorkflowEntrypoint):
    async def run(self, event, step):


        @step.do('step1')
        async def step_1():
            # does stuff
            print('executing step1')


        @step.do('step2')
        async def step_2():
            # does stuff
            print('executing step2')


        await step_1()
        await step_2()


async def on_fetch(request, env):
    await env.MY_WORKFLOW.create()
    return Response("Hello world!")
```

You must add both `python_workflows` and `python_workers` compatibility flags to your Wrangler configuration file.

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "name": "hello-python",
    "main": "src/entry.py",
    "compatibility_flags": [
      "python_workers",
      "experimental",
      "python_workflows"
    ],
    "compatibility_date": "2026-02-14",
    "workflows": [
      {
        "name": "workflows-demo",
        "binding": "MY_WORKFLOW",
        "class_name": "PythonWorkflowStarter"
      }
    ]
  }
  ```

* wrangler.toml

  ```toml
  "$schema" = "./node_modules/wrangler/config-schema.json"
  name = "hello-python"
  main = "src/entry.py"
  compatibility_flags = [ "python_workers", "experimental", "python_workflows" ]
  compatibility_date = "2026-02-14"


  [[workflows]]
  name = "workflows-demo"
  binding = "MY_WORKFLOW"
  class_name = "PythonWorkflowStarter"
  ```

To run a Python Workflow locally, use [Wrangler](https://developers.cloudflare.com/workers/wrangler/), the CLI for Cloudflare Workers:

```bash
npx wrangler@latest dev
```

To deploy a Python Workflow to Cloudflare, run [`wrangler deploy`](https://developers.cloudflare.com/workers/wrangler/commands/#deploy):

```bash
npx wrangler@latest deploy
```

Join the #python-workers channel in the [Cloudflare Developers Discord](https://discord.cloudflare.com/) and let us know what you would like to see next.
