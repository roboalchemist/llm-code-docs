# Source: https://www.zuplo.com/docs/cli/list.md

# Zuplo CLI: List

<CliCommand
  command="list"
  description="Lists all deployed Zuplo APIs"
  options={[
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
  },
  {
    "name": "self-hosted-endpoint",
    "type": "string",
    "description": "The endpoint of your self-hosted service to deploy to",
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 list",
    "List all deployed environments for your project"
  ],
  [
    "$0 list --account my-account --project my-project",
    "Explicitly specify the account and project"
  ]
]}
  usage="$0 list [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
