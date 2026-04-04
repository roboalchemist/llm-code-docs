# Source: https://docs.base44.com/developers/references/cli/commands/eject.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# eject

> Clone an existing Base44 app into a separate local project

Clone an existing Base44 app into a separate local project. This command downloads the frontend code and backend resources from a selected app and creates a new project with its own app ID. Your original app stays in Base44 unchanged.

<Warning>
  The ejected project has an empty database. Your entity schemas are copied, but not your data. Your original Base44 app remains unchanged and the 2 projects are independent after ejection.
</Warning>

For a step-by-step guide, see [Start from an Existing Base44 App](/developers/backend/overview/start-from-existing-app).

## Usage

```bash  theme={null}
base44 eject
```

The command guides you through an interactive flow:

1. Prompts you to select from your existing Base44 apps.
2. Downloads the frontend code from the selected app.
3. Downloads entity schemas and other backend resources, but not your data.
4. Creates a new backend project with a unique ID.
5. Sets up a local [project structure](/developers/backend/overview/project-structure) with all resources.

## See also

* [Start from an Existing Base44 App](/developers/backend/overview/start-from-existing-app): Clone an existing Base44 project
* [`create`](/developers/references/cli/commands/create): Start a new project from scratch
* [`link`](/developers/references/cli/commands/link): Connect local project files to Base44


Built with [Mintlify](https://mintlify.com).