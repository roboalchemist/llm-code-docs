# Source: https://www.zuplo.com/docs/cli/delete.md

# Zuplo CLI: Delete

<CliCommand
  command="delete"
  description="Deletes the Zuplo API by URL"
  options={[
  {
    "name": "url",
    "type": "string",
    "description": "The URL of the Zuplo API to delete",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "branch",
    "type": "string",
    "description": "The branch name to delete deployments for",
    "required": false,
    "deprecated": false,
    "hidden": true
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
  },
  {
    "name": "self-hosted-endpoint",
    "type": "string",
    "description": "The endpoint of your self-hosted service to deploy to",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "wait",
    "type": "boolean",
    "description": "Should the CLI wait until the Zuplo API is deleted",
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 delete --url https://my-api-dev-123abc.zuplo.app",
    "Delete a deployed environment by its URL"
  ],
  [
    "$0 delete --url https://my-api-dev-123abc.zuplo.app --wait",
    "Delete an environment and wait until the deletion is complete"
  ]
]}
  usage="$0 delete --url <url> [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
