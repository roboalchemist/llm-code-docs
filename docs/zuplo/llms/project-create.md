# Source: https://www.zuplo.com/docs/cli/project-create.md

# Zuplo CLI: Project Create

<CliCommand
  command="project create"
  description="Creates a new project in your account"
  options={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the project to create",
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 project create --name my-api-project",
    "Create a new project with the specified name"
  ],
  [
    "$0 project create",
    "Create a new project (will prompt for name)"
  ],
  [
    "$0 project create --name my-project --account my-account",
    "Explicitly specify the account"
  ]
]}
  usage="$0 project create [--name <name>] [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
