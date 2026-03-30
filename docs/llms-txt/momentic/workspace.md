# Source: https://momentic.ai/docs/cli/workspace.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Workspaces

For organizations with multiple teams, you can initialize a separate Momentic
project for each team to isolate tests, environments, and settings. A group of
projects is known as a **workspace**. Each Git repository should have at most
one workspace.

## Creating a workspace

Create a `momentic.workspace.yaml` file in the location where you want users to
start the app. For most organizations, this should be the root of your Git
repository.

### `projects`

The workspace file currently supports a single `projects` key, which is an list
of paths where Momentic should look for projects:

```yaml  theme={null}
projects:
  - project-a
  - folder/*
  - apps/**/*
```


Built with [Mintlify](https://mintlify.com).