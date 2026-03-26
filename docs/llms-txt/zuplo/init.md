# Source: https://www.zuplo.com/docs/cli/init.md

# Zuplo CLI: Init

<CliCommand
  command="init"
  description="Initialize a Zuplo project on the platform (create project and deploy initial environment)"
  options={[
  {
    "name": "directory",
    "type": "string",
    "description": "Directory containing the project (defaults to current directory)",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "with-account",
    "type": "string",
    "description": "Pre-select the account name for project creation",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "with-project",
    "type": "string",
    "description": "Pre-select or create a project with this name",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "yes",
    "type": "boolean",
    "description": "Use defaults for all prompts",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "alias": [
      "y"
    ]
  }
]}
  examples={[
  [
    "$0 init",
    "Initialize the current directory with Zuplo platform"
  ],
  [
    "$0 init my-api",
    "Initialize the my-api directory with Zuplo platform"
  ],
  [
    "$0 init --with-account my-account --with-project my-api",
    "Initialize with a specific account and project"
  ],
  [
    "$0 init -y",
    "Initialize with all defaults (create project, deploy)"
  ]
]}
  usage="$0 init [directory] [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
