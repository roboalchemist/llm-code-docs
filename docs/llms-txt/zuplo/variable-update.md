# Source: https://www.zuplo.com/docs/cli/variable-update.md

# Zuplo CLI: Variable Update

<CliCommand
  command="variable update"
  description="Updates an existing variable for a branch"
  options={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the variable to update",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "value",
    "type": "string",
    "description": "The value of the variable to update",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "branch",
    "type": "string",
    "description": "The branch where the variable exists",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "project",
    "type": "string",
    "description": "The project name",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "account",
    "type": "string",
    "description": "The account name",
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 variable update --name API_KEY --value new-secret-key --branch main",
    "Update a variable on the main branch"
  ],
  [
    "$0 variable update \\\n  --name BASE_URL \\\n  --value https://api.prod.example.com \\\n  --branch production \\\n  --account my-account \\\n  --project my-project",
    "Explicitly specify the account and project"
  ]
]}
  usage="$0 variable update --name <name> --value <value> --branch <branch> [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)

## Additional resources

- [Environment variables](../articles/environment-variables.mdx)
