# Source: https://docs.base44.com/developers/backend/quickstart/templates/quickstart-react-template.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# React Quickstart

> Create a full-stack Base44 project with a Base44 backend and a Vite-powered React frontend

Follow this quickstart to scaffold a project, define an entity, and run your app locally. This project includes a pre-configured Base44 SDK client, UI components, and Tailwind CSS styling.

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

    Select **Start from a template** when prompted, then follow the prompts to configure your project, push entities, and deploy your site.
  </Step>
</Steps>

When complete, you'll see your project name, a link to your Base44 dashboard, and your live application URL.

The generated project structure:

<Tree>
  <Tree.Folder name="<your-project-name>" defaultOpen>
    <Tree.Folder name="base44" defaultOpen>
      <Tree.File name=".app.jsonc" />

      <Tree.File name="config.jsonc" />

      <Tree.Folder name="entities" defaultOpen>
        <Tree.File name="task.jsonc" />
      </Tree.Folder>
    </Tree.Folder>

    <Tree.Folder name="src" defaultOpen>
      <Tree.Folder name="api">
        <Tree.File name="base44Client.js" />
      </Tree.Folder>

      <Tree.Folder name="components">
        <Tree.Folder name="ui" />

        <Tree.File name="Base44Logo.jsx" />
      </Tree.Folder>

      <Tree.File name="App.jsx" />

      <Tree.File name="main.jsx" />

      <Tree.File name="index.css" />
    </Tree.Folder>

    <Tree.File name=".gitignore" />

    <Tree.File name=".nvmrc" />

    <Tree.File name="components.json" />

    <Tree.File name="index.html" />

    <Tree.File name="jsconfig.json" />

    <Tree.File name="package.json" />

    <Tree.File name="postcss.config.js" />

    <Tree.File name="README.md" />

    <Tree.File name="tailwind.config.js" />

    <Tree.File name="vite.config.js" />
  </Tree.Folder>
</Tree>

For more information about the files in this project, see [Project Structure](/developers/backend/overview/project-structure).

This project includes an example `Task` [entity](/developers/references/entities/introduction) in `base44/entities/task.jsonc` which was pushed to Base44 during project creation. You can modify this entity or create additional ones.

## Next steps

Now that your Base44 backend is integrated with your project, you can:

* Use the [SDK](/developers/references/sdk/getting-started/overview) to add more functionality to your frontend.
* Add [entities](/developers/backend/resources/entities/overview), [backend functions](/developers/backend/resources/functions), and [agents](/developers/backend/resources/agents-config). If you're working in TypeScript, [generate types](/developers/references/sdk/getting-started/dynamic-types) to get autocomplete and type safety.
* Test locally by running [`base44 dev`](/developers/references/cli/commands/dev) for the backend and `npm run dev` for the frontend. See [Local development](/developers/backend/overview/local-dev/local-development-overview) for setup instructions.
* Deploy updates with [`base44 deploy`](/developers/references/cli/commands/deploy).
* Open your deployed site with [`base44 site open`](/developers/references/cli/commands/site-open).

Your project includes [Base44 skills](/developers/backend/overview/base44-skills) that teach AI coding assistants how to work with Base44. You can open your project in Cursor, Claude Code, or your preferred AI assistant and describe what you want to build.

## See also

* [CLI Command Reference](/developers/references/cli/commands/introduction): All available CLI commands
* [Project Structure](/developers/backend/overview/project-structure): How project resources are organized
* [Entities](/developers/references/entities/introduction): Learn about database schema configuration
* [Example apps](https://github.com/base44/apps-examples): Sample projects to learn from


Built with [Mintlify](https://mintlify.com).