# Source: https://docs.base44.com/developers/app-code/overview/project-structure.md

# Source: https://docs.base44.com/developers/backend/overview/project-structure.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Project Structure

> Understanding the Base44 project structure for local development

The Base44 CLI's [`create`](/developers/references/cli/commands/create) command creates new projects with all necessary files and configuration. This article describes the Base44 backend project structure and explains what each file and directory does.

## Backend project structure

When you create a backend-only Base44 project, the CLI generates this minimal structure:

<Tree>
  <Tree.Folder name="<your-project-name>" defaultOpen>
    <Tree.Folder name="base44" defaultOpen>
      <Tree.File name=".app.jsonc" />

      <Tree.File name="config.jsonc" />
    </Tree.Folder>

    <Tree.File name=".gitignore" />
  </Tree.Folder>
</Tree>

As you develop your project, you add files for your resources such as [entities](/developers/backend/resources/entities/overview) and [functions](/developers/backend/resources/backend-functions/overview):

<Tree>
  <Tree.Folder name="<your-project-name>" defaultOpen>
    <Tree.Folder name="base44" defaultOpen>
      <Tree.File name=".app.jsonc" />

      <Tree.File name="config.jsonc" />

      <Tree.Folder name=".types" defaultOpen>
        <Tree.File name="types.d.ts" />
      </Tree.Folder>

      <Tree.Folder name="entities" defaultOpen>
        <Tree.File name="<entity-name>.jsonc" />
      </Tree.Folder>

      <Tree.Folder name="functions" defaultOpen>
        <Tree.Folder name="<function-name>" defaultOpen>
          <Tree.File name="entry.ts" />

          <Tree.File name="function.jsonc" />
        </Tree.Folder>
      </Tree.Folder>
    </Tree.Folder>

    <Tree.File name=".gitignore" />
  </Tree.Folder>
</Tree>

<Note>
  Functions only require an `entry.ts` or `entry.js` file. You can optionally add `function.jsonc` for advanced configurations like custom names or automations. See [Backend Functions](/developers/backend/resources/backend-functions/overview) for details.
</Note>

### base44/

Contains all Base44 backend configuration and resource definitions.

#### config.jsonc

Defines your project configuration, including paths to [entities](/developers/backend/resources/entities/overview), [functions](/developers/backend/resources/functions), [agents](/developers/backend/resources/agents-config), [connectors](/developers/backend/resources/connectors), and site hosting settings for full-stack projects. The CLI creates this with just your project name, and you can add more configuration as needed.

Your project requires a `config.jsonc` (or `config.json`) file in the `base44/` directory:

```jsonc  theme={null}
// Base44 Project Configuration
{
  "name": "my-project",
  "description": "My Base44 app",

  // Directory paths (relative to config file)
  "entitiesDir": "./entities",
  "functionsDir": "./functions",
  "agentsDir": "./agents",
  "connectorsDir": "./connectors",

  // Site/hosting configuration (for full-stack projects)
  "site": {
    "outputDirectory": "./dist", // Required - where your built files are located
  },
}
```

| Property               | Description                                                                             | Default        |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------- |
| `name`                 | Project name (required)                                                                 | —              |
| `description`          | Project description                                                                     | —              |
| `entitiesDir`          | Path to [entities](/developers/backend/resources/entities/overview) directory           | `./entities`   |
| `functionsDir`         | Path to [functions](/developers/backend/resources/backend-functions/overview) directory | `./functions`  |
| `agentsDir`            | Path to [agents](/developers/backend/resources/agents-config) directory                 | `./agents`     |
| `connectorsDir`        | Path to [connectors](/developers/backend/resources/connectors) directory                | `./connectors` |
| `site.outputDirectory` | Where your built site files are located (required for site deployment)                  | —              |
| `site.buildCommand`    | Used only during `base44 create` for automated deployment                               | —              |
| `site.installCommand`  | Used only during `base44 create` for automated deployment                               | —              |
| `site.serveCommand`    | Reference only. Not currently used by the CLI                                           | —              |

<Note>
  The `buildCommand`, `installCommand`, and `serveCommand` properties are
  included automatically when you create a project from the full-stack template.
  They're used only during the initial `base44 create` flow for automated
  deployment. You don't need to specify or modify these properties after project
  creation. When deploying your site later with `site deploy`, only
  `outputDirectory` is used.
</Note>

#### .app.jsonc

Links your local project to your Base44 app. This file is automatically created by the CLI when you create or link a project.

```jsonc  theme={null}
// Base44 App Configuration
// This file links your local project to your Base44 app.
// Do not commit this file to version control.
{
  "id": "your-app-id",
}
```

<Note>
  The `.app.jsonc` file should not be committed to version control. The CLI
  automatically creates a `.gitignore` file that excludes this file.
</Note>

#### .types/types.d.ts

Generated TypeScript type definitions for your entities, functions, agents, and connectors. Created by running [`base44 types generate`](/developers/references/cli/commands/types-generate). This file provides autocomplete and type safety when using the SDK in TypeScript projects. See [Dynamic Types](/developers/references/sdk/getting-started/dynamic-types) for more details.

#### entities/

Directory containing [entity schema definitions](/developers/backend/resources/entities/overview). Each entity is defined in a separate `.json` or `.jsonc` file. Create this directory when you're ready to define your first entity.

#### functions/

Directory containing serverless [backend functions](/developers/backend/resources/backend-functions/overview). Each function requires its own subdirectory with an `entry.ts` or `entry.js` code file. The CLI uses the directory path relative to the functions root as the function name. For example, `functions/sendEmail/entry.ts` creates a function named `sendEmail`. You can optionally add a `function.jsonc` configuration file to customize the function name or add automations.

<Tree>
  <Tree.Folder name="functions" defaultOpen>
    <Tree.Folder name="<function-name>" defaultOpen>
      <Tree.File name="entry.ts" />

      <Tree.File name="function.jsonc" />
    </Tree.Folder>
  </Tree.Folder>
</Tree>

#### agents/

Directory containing [AI agent configurations](/developers/backend/resources/agents-config). Each agent is defined in a separate `.json` or `.jsonc` file.

#### connectors/

Directory containing [OAuth connector configurations](/developers/backend/resources/connectors). Each connector is defined in a separate `.json` or `.jsonc` file named after the integration type such as `slack.jsonc` or `googlecalendar.jsonc`.

### .gitignore

Prevents files from being committed to version control. Your project starts with this file to prevent `.app.jsonc` from being committed.

### AI agent skills folders

When you create a project with `base44 create`, [AI agent skills](/developers/backend/overview/base44-skills) are automatically installed. These appear in agent-specific folders like `.claude/skills/`, `.cursor/skills/`, or similar, depending on which AI coding assistant you use. These folders help your coding agent understand how to work with Base44 and are safe to commit to version control.

## See also

* [Quickstart - Backend only](/developers/backend/quickstart/templates/quickstart-backend-only): Create your first backend-only project
* [Quickstart - React](/developers/backend/quickstart/templates/quickstart-react-template): Build a full-stack React app with Base44
* [`types generate` command](/developers/references/cli/commands/types-generate): Generate TypeScript types from your project
* [Dynamic Types](/developers/references/sdk/getting-started/dynamic-types): Get type safety for your SDK code
* [Entities](/developers/backend/resources/entities/overview): Learn about database schema configuration
* [Backend Functions](/developers/backend/resources/backend-functions/overview): Create serverless API endpoints
* [AI Agents](/developers/backend/resources/agents-config): Configure AI agents for your app
* [Connectors](/developers/backend/resources/connectors): Set up OAuth connections to third-party services


Built with [Mintlify](https://mintlify.com).