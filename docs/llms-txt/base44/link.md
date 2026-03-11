# Source: https://docs.base44.com/developers/references/cli/commands/link.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# link

> Link a local project to a Base44 project

Link a local project to Base44. You can create a new backend project or link to an existing one created with the CLI. The command writes the project ID to your [`.app.jsonc`](/developers/backend/overview/project-structure#app-jsonc) file.

You can only link to Base44 backend projects, not Base44 apps.

Use this when you have a local project but haven't yet connected it to Base44.

<Note>
  If you don't have any project files yet, use [`base44 create`](/developers/references/cli/commands/create) to generate a new project. The `create` command generates new code, while `link` connects existing code files to a backend. For a complete guide, see [Link an Existing Backend Project](/developers/backend/overview/link-existing-project).
</Note>

## Requirements

* Must be run from a directory containing a `base44/config.jsonc` file.
* Project must not already be linked. If an [`.app.jsonc`](/developers/backend/overview/project-structure#app-jsonc) file with an app ID already exists, the command will fail.

## Usage

```bash  theme={null}
base44 link
```

An interactive prompt will guide you through creating a new project or selecting an existing one.

For a step-by-step guide on linking existing projects, see [Link an Existing Backend Project](/developers/backend/overview/link-existing-project).

## Flags

| Flag                              | Description                                                             |
| --------------------------------- | ----------------------------------------------------------------------- |
| `-c, --create`                    | Create a new backend project on Base44. This skips the selection prompt |
| `-n, --name <name>`               | Project name. Required when using `--create`                            |
| `-d, --description <description>` | Project description                                                     |
| `-e, --existing`                  | Link to an existing project. This skips the selection prompt            |
| `-p, --projectId <id>`            | Project ID. Required when using `--existing`                            |

## Non-interactive usage

For scripts or CI environments, use the flags to skip prompts:

Create a new project:

```bash  theme={null}
base44 link --create --name "my-project" --description "My app"
```

Link to an existing project:

```bash  theme={null}
base44 link --existing --projectId "your-project-id"
```

## See also

* [`create`](/developers/references/cli/commands/create): Create a new Base44 project
* [`dashboard open`](/developers/references/cli/commands/dashboard-open): Open your app in the dashboard
* [`site open`](/developers/references/cli/commands/site-open): Open the deployed site in your browser
* [Project Structure](/developers/backend/overview/project-structure): How project files are organized


Built with [Mintlify](https://mintlify.com).