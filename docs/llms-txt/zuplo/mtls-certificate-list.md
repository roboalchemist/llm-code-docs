# Source: https://www.zuplo.com/docs/cli/mtls-certificate-list.md

# Zuplo CLI: Mtls Certificate List

<CliCommand
  command="mtls-certificate list"
  description="Lists all mTLS certificates for a project"
  options={[
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
  }
]}
  examples={[
  [
    "$0 mtls-certificates list",
    "List all mTLS certificates for your project"
  ],
  [
    "$0 mtls-certificates list --account my-account --project my-project",
    "Explicitly specify the account and project"
  ]
]}
  usage="$0 mtls-certificates list [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
