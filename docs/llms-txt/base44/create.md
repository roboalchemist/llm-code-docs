# Source: https://docs.base44.com/developers/references/cli/commands/create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# create

> Create a new Base44 project

Create a new Base44 project with all necessary configuration files and folder structure. You'll be guided through setup with interactive prompts.

<Note>
  If you've cloned or downloaded existing Base44 project files, such as an example app, use [`base44 link`](/developers/backend/overview/link-existing-project) instead. The `create` command generates new code, while `link` connects existing code files to a backend.
</Note>

## Usage

```bash  theme={null}
base44 create
```

## Flags

| Flag                              | Description                                                        |
| --------------------------------- | ------------------------------------------------------------------ |
| `-n, --name <name>`               | Project name                                                       |
| `-d, --description <description>` | Project description                                                |
| `-p, --path <path>`               | Path where to create the project                                   |
| `-t, --template <id>`             | Template ID. Options include: `backend-only`, `backend-and-client` |
| `--deploy`                        | Build and deploy the site after creation                           |

<Note>
  When using `--name` and `--path` flags together, the command runs in non-interactive mode. The template defaults to `backend-only` unless specified with `--template`.
</Note>

## Project options

When you run this command, you'll be prompted to choose what kind of project to create:

* **Create a basic project:** Minimal Base44 backend for defining your data models and logic. See the [backend-only quickstart](/developers/backend/quickstart/templates/quickstart-backend-only) for detailed instructions.
* **Start from a template:** Full-stack example with a Base44 backend and a Vite + React client app. See the [React quickstart](/developers/backend/quickstart/templates/quickstart-react-template) for detailed instructions.

## See also

* [Project Structure](/developers/backend/overview/project-structure): How project files are organized
* [`entities push`](/developers/references/cli/commands/entities-push): Deploy entity schemas to Base44


Built with [Mintlify](https://mintlify.com).