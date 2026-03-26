# Source: https://www.zuplo.com/docs/cli/variable-create.md

# Zuplo CLI: Variable Create

<CliCommand
  command="variable create"
  description="Creates a new variable for a branch"
  options={[
  {
    "name": "name",
    "type": "string",
    "description": "The name of the variable to create",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "value",
    "type": "string",
    "description": "The value of the variable to create",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "branch",
    "type": "string",
    "description": "The branch where the variable should be set",
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
    "name": "is-secret",
    "type": "boolean",
    "description": "Is the variable a secret",
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 variable create \\\n  --name API_KEY \\\n  --value my-secret-key \\\n  --is-secret true \\\n  --branch main",
    "Create a secret variable for the main branch"
  ],
  [
    "$0 variable create \\\n  --name BASE_URL \\\n  --value https://api.example.com \\\n  --is-secret false \\\n  --branch production",
    "Create a non-secret variable for the production branch"
  ],
  [
    "$0 variable create \\\n  --name DB_HOST \\\n  --value localhost \\\n  --is-secret false \\\n  --branch dev \\\n  --account my-account \\\n  --project my-project",
    "Explicitly specify the account and project"
  ]
]}
  usage="$0 variable create \
  --name <name> \
  --value <value> \
  --is-secret <boolean> \
  --branch <branch> [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)

## Additional resources

- [Environment variables](../articles/environment-variables.mdx)
