# Source: https://docs.base44.com/developers/backend/quickstart/templates/quickstart-backend-only.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Backend only

> Create a backend only project with Base44

Create a backend only Base44 project with [entities](/developers/backend/resources/entities/overview) and [functions](/developers/backend/overview/project-structure#functions). Use this template when you want to build your own frontend or integrate with existing apps.

<Note>The CLI requires Node.js 20.19.0 or higher.</Note>

## Setup

<Steps>
  <Step title="Install the Base44 CLI">
    Install the Base44 CLI globally:

    ```bash  theme={null}
    npm install -g base44@latest
    ```
  </Step>

  <Step title="Create a project">
    Create a new Base44 project:

    ```bash  theme={null}
    base44 create
    ```

    If you're not already logged in, the command will prompt you to authenticate.

    Select **Create a basic project** when prompted, then follow the prompts to configure your project.
  </Step>
</Steps>

When complete, you'll see your project name and a link to your Base44 dashboard. The CLI creates your project with the following structure:

<Tree>
  <Tree.Folder name="<your-project-name>" defaultOpen>
    <Tree.Folder name="base44" defaultOpen>
      <Tree.File name=".app.jsonc" />

      <Tree.File name="config.jsonc" />
    </Tree.Folder>

    <Tree.File name=".gitignore" />
  </Tree.Folder>
</Tree>

Your app ID is automatically added to [`.app.jsonc`](/developers/backend/overview/project-structure#app-jsonc).

## Next steps

Now that your Base44 project is set up, you can:

* Add [entities](/developers/backend/resources/entities/overview), [backend functions](/developers/backend/resources/functions), and [agents](/developers/backend/resources/agents-config). If you're working in TypeScript, [generate types](/developers/references/sdk/getting-started/dynamic-types) to get autocomplete and type safety.
* Build or connect a frontend application using the [SDK](/developers/references/sdk/getting-started/overview).
* Deploy updates with [`base44 deploy`](/developers/references/cli/commands/deploy).

Your project includes [Base44 skills](/developers/backend/overview/base44-skills) that teach AI coding assistants how to work with Base44. You can open your project in Cursor, Claude Code, or your preferred AI assistant and describe what you want to build.

### Build a frontend

Create a frontend app using your preferred framework.

Install the Base44 JavaScript SDK:

```bash  theme={null}
npm install @base44/sdk
```

Configure the SDK client with your app ID (from `base44/.app.jsonc`) and use it to interact with your entities:

```javascript  theme={null}
import { createClient } from "@base44/sdk";

const base44 = createClient({
  appId: "your-app-id",
});

const tasks = await base44.entities.Task.list();
```

Learn more in the [JavaScript SDK documentation](/developers/references/sdk/getting-started/overview).

### Local development

Most frontend frameworks support local development servers with hot reloading. Through the SDK, your local frontend will connect to Base44's hosted backend.

You can also run [`base44 dev`](/developers/references/cli/commands/dev) to start a local development server that handles backend functions, entities, and media uploads on your machine. This lets you test changes without deploying. See [Local development](/developers/backend/overview/local-dev/local-development-overview) for details.

### Deploy your frontend

If you want to deploy your frontend to Base44's hosting platform, configure the `outputDirectory` in your `base44/config.jsonc`:

```jsonc  theme={null}
{
  "name": "basic-test-app",

  // Site/hosting configuration
  "site": {
    "outputDirectory": "./dist",
  },
}
```

The `outputDirectory` tells the CLI where your build tool outputs the compiled files. Build your frontend, then deploy with the [`site deploy`](/developers/references/cli/commands/site-deploy) command.

## See also

* [Project Structure](/developers/backend/overview/project-structure): How project files are organized
* [CLI Command Reference](/developers/references/cli/commands/introduction): All available CLI commands
* [JavaScript SDK](/developers/references/sdk/getting-started/overview): Connect your app to the backend
* [Example apps](https://github.com/base44/apps-examples): Sample projects to learn from


Built with [Mintlify](https://mintlify.com).