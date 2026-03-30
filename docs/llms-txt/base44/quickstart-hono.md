# Source: https://docs.base44.com/developers/backend/quickstart/frameworks/quickstart-hono.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Hono Quickstart

> Add Base44 to your Hono project

Follow this quickstart to add Base44 to your Hono project. You'll create a Base44 backend, define entities, and integrate the SDK into your API routes.

<Note>The CLI requires Node.js 20.19.0 or higher.</Note>

## Setup

<Steps>
  <Step title="Install the Base44 CLI">
    Install the Base44 CLI globally:

    ```bash  theme={null}
    npm install -g base44@latest
    ```
  </Step>

  <Step title="Create a Base44 backend">
    Navigate to your Hono project directory, then run:

    ```bash  theme={null}
    base44 create
    ```

    If you're not already logged in, the command will prompt you to authenticate.

    Select **Create a basic project** when prompted. This creates the backend files within your Hono project directory. Then follow the prompts to configure your project.

    When you create a project, [Base44 skills](/developers/backend/overview/base44-skills) are included automatically, providing your AI agent with instructions and context for Base44 tasks.
  </Step>

  <Step title="Configure the output directory (optional)">
    If you're serving static files with Hono, update [config.jsonc](/developers/backend/overview/project-structure) to point to your build output. Add or modify the `site.outputDirectory` field:

    ```json  theme={null}
    {
      "site": {
        "outputDirectory": "dist"
      }
    }
    ```

    <Note>
      If you're building a pure API with Hono and not serving a frontend, you can skip the `outputDirectory` configuration or omit this step.
    </Note>
  </Step>

  <Step title="Define entities">
    Create [entity schemas](/developers/references/entities/introduction) to define your data structures. Entity files must be placed in the `base44/entities/` directory.

    For example, create `base44/entities/task.jsonc`:

    ```json  theme={null}
    {
      "name": "Task",
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "completed": {
          "type": "boolean",
          "default": false
        }
      },
      "required": ["title"]
    }
    ```
  </Step>

  <Step title="Push entities to Base44">
    Push your entity schemas to Base44:

    ```bash  theme={null}
    base44 entities push
    ```

    This command synchronizes your local entity definitions with your Base44 backend, making them available for use in your application. See [`entities push`](/developers/references/cli/commands/entities-push) for more information.
  </Step>

  <Step title="Install the Base44 SDK">
    Install the Base44 JavaScript SDK:

    ```bash  theme={null}
    npm install @base44/sdk
    ```
  </Step>

  <Step title="Create a Base44 client">
    Create a Base44 SDK [client](/developers/references/sdk/getting-started/client) in your project. The `appId` can be found in your `base44/.app.jsonc` file.

    For example, create `lib/base44.js`:

    ```javascript  theme={null}
    import { createClient } from '@base44/sdk';

    export const base44 = createClient({
      appId: 'your-app-id-from-app.jsonc'
    });
    ```
  </Step>

  <Step title="Use the SDK in your API routes">
    Use the Base44 SDK to interact with your [entities](/developers/references/sdk/docs/type-aliases/entities) in Hono route handlers. For example:

    ```javascript  theme={null}
    import { Hono } from 'hono';
    import { base44 } from './lib/base44Client';

    const app = new Hono();

    // Get all tasks
    app.get('/api/tasks', async (c) => {
      const tasks = await base44.entities.Task.list();
      return c.json(tasks);
    });

    // Create a new task
    app.post('/api/tasks', async (c) => {
      const body = await c.req.json();
      const newTask = await base44.entities.Task.create({
        title: body.title,
        completed: false
      });
      return c.json(newTask, 201);
    });

    export default app;
    ```

    <Note>
      Use the exact entity name from your schema when calling the SDK, including capitalization. By convention, entity names begin with a capital letter. For example, if your schema has `"name": "Task"`, you access it as `base44.entities.Task.list()`.
    </Note>
  </Step>

  <Step title="Run your API locally">
    Start your Hono development server to test your integration. From your project root, run:

    ```bash  theme={null}
    npm run dev
    ```

    Your Hono API will connect to your Base44 backend through the SDK client, allowing you to work with your deployed entities in real-time.
  </Step>
</Steps>

## Next steps

Now that your Base44 backend is integrated with your project, you can:

* Use the [SDK](/developers/references/sdk/getting-started/overview) to add more functionality to your API.
* Add [entities](/developers/backend/resources/entities/overview), [backend functions](/developers/backend/resources/functions), and [agents](/developers/backend/resources/agents-config). If you're working in TypeScript, [generate types](/developers/references/sdk/getting-started/dynamic-types) to get autocomplete and type safety.
* Test locally by running [`base44 dev`](/developers/references/cli/commands/dev) for the Base44 backend alongside your Hono dev server. See [Local development](/developers/backend/overview/local-dev/local-development-overview) for setup instructions.
* Continue building your API and deploy it according to your chosen runtime.

## See also

* [CLI Command Reference](/developers/references/cli/commands/introduction): All available CLI commands
* [Project Structure](/developers/backend/overview/project-structure): How project files are organized
* [JavaScript SDK Documentation](/developers/references/sdk/getting-started/overview): Connect your app to the backend
* [Base44 Skills](/developers/backend/overview/base44-skills): Teach AI assistants to work with Base44


Built with [Mintlify](https://mintlify.com).