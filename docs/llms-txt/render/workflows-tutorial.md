# Source: https://render.com/docs/workflows-tutorial.md

# Your First Workflow — Register your first task and trigger its first run.


> *Render Workflows is in public beta.*
>
> During the beta, bugs or changes in API/SDK behavior are possible as we continue refining the product. We welcome any and all feedback at *workflows-feedback@render.com*.

Welcome to Render Workflows! Follow these steps to register your first task and trigger its first run.

## 1. Copy a starter template

> *Workflows currently support TypeScript and Python for defining tasks.*
>
> SDKs for additional languages are planned for future releases.

As part of creating a workflow, you'll link a GitHub/GitLab/Bitbucket repo that contains your task definitions.

*To get started quickly, copy one of our basic templates on GitHub:*

- [TypeScript](https://github.com/render-examples/workflows-template-ts)
- [Python](https://github.com/render-examples/workflows-template-python)

On the template page, click *Use this template > Create a new repository* to create your own repo with the template's contents.

### The anatomy of a workflow

The following excerpts from the basic templates illustrate the bare minimum syntax for defining a workflow:

**TypeScript**

```typescript:index.ts
import { task } from '@renderinc/sdk/workflows'

// Minimal task definition
const calculateSquare = task(
  { name: 'calculateSquare' },
  function calculateSquare(a: number): number {
    return a * a
  }
)
```

- You import `task` from the [Render SDK for TypeScript](/workflows-sdk-typescript), which is the template's only dependency aside from TypeScript itself.
- You define tasks by calling `task(...)` once for each, providing options and a function definition.
- No additional initialization is required when using the TypeScript SDK.

**Python**

```python:main.py
from render_sdk import Workflows

app = Workflows()

# Minimal task definition
@app.task
def calculate_square(a: int) -> int:
  return a * a

if __name__ == "__main__":
  app.start() # Workflow entry point
```

- You define a task by first initializing a `Workflows` app, then applying the `@app.task` decorator to any function.
- You call `app.start()` on startup to initiate both task registration and run execution on Render.
- The `Workflows` class is imported from the [Render SDK for Python](/workflows-sdk-python), which is the template's only dependency.

## 2. Create a workflow service

1. In the [Render Dashboard](https://dashboard.render.com), click *New > Workflow*:

   [image: Creating a new workflow in the Render Dashboard]

   The workflow creation form appears.

2. Link the GitHub/GitLab/Bitbucket repo with your workflow's task definitions.

3. Complete the remainder of the creation form. See guidance for important fields:

------

###### Field

*Language*

###### Description

- Set to *Node* if you're using the TypeScript SDK.
   - Set to *Python 3* if you're using the Python SDK.

   Support for other languages is planned for future releases.

---

###### Field

*Region*

###### Description

Your workflow's task runs will execute in the specified region. This determines which of your _other_ Render services they can reach over your private network.

---

###### Field

*Build Command*

###### Description

If you're using a Render-provided template, this is the following:

   **TypeScript**

   ```bash
   npm install
   ```

   **Python**

   ```bash
   pip install -r requirements.txt
   ```

   Otherwise, provide the command that Render should use to install dependencies and build your code.

---

###### Field

*Start Command*

###### Description

If you're using a Render-provided template, this is the following:

   **TypeScript**

   ```bash
   npm start
   ```

   **Python**

   ```bash
   python main.py
   ```

   Otherwise, provide the command that Render should use to start your workflow.

------

4. Click *Deploy Workflow*. Render kicks off your workflow's first build, which includes registering your tasks.

That's it! After the build completes, your tasks are officially registered. You can view them from your workflow's *Tasks* page in the [Render Dashboard](https://dashboard.render.com):

[image: Viewing a registered task in the Render Dashboard]

## 3. Trigger a task run

Now that we've registered a task, let's run it! The quickest way to trigger our first run is in the [Render Dashboard](https://dashboard.render.com):

1. From your workflow's *Tasks* page, click a task to open its *Runs* page.
2. Click *Start Task* in the top-right corner of the page:

   [image: Running a task in the Render Dashboard]

   A dialog appears for providing the task's input arguments:

   [image: Providing input arguments for a task run in the Render Dashboard]

3. Provide the task's input arguments as a JSON array (e.g., `[5]` for a task that takes a single integer argument, or `[]` for a task that takes zero arguments).

4. Click *Start task*.

   Your new task run appears at the top of the *Runs* table.

## Next steps

Congratulations! You've registered your first workflow task and triggered its first run. Now it's time to start designing your own tasks and triggering runs from application code:

- [Define advanced tasks](/workflows-defining) with retries, chaining, and more.
- [Trigger task runs](/workflows-running) from your application code.
- [Test task runs locally](/workflows-local-development) for faster development.

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

###### region

Each Render service runs in one of the following regions: *Oregon*, *Ohio*, *Virginia*, *Frankfurt*, or *Singapore*.

Services in the same region can communicate over their *private network*.

Related article: https://render.com/docs/regions.md

###### private network

Your Render services in the same *region* can reach each other without traversing the public internet, enabling faster and safer communication.

Related article: https://render.com/docs/private-network.md

###### build command

The command that Render runs to build your service from source.

Common examples include `npm install` for Node.js and `pip install -r requirements.txt` for Python.

Related article: https://render.com/docs/deploys.md#build-command

###### start command

The command that Render runs to start your built service in a newly deployed *instance*.

Common examples include `npm start` for Node.js and `gunicorn your_application.wsgi` for Python.

Related article: https://render.com/docs/deploys.md#start-command