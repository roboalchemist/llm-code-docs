# Source: https://www.zuplo.com/docs/dev-portal/zudoku/components/link.md

# Source: https://www.zuplo.com/docs/cli/link.md

# Zuplo CLI: Link

<CliCommand
  command="link"
  description="Links information from your Zuplo account to your local machine allowing"
  options={[
  {
    "name": "dir",
    "type": "string",
    "description": "The directory containing your Zuplo API",
    "default": ".",
    "required": false,
    "deprecated": false,
    "hidden": true,
    "normalize": true
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
    "name": "environment",
    "type": "string",
    "description": "The environment name",
    "required": false,
    "deprecated": false,
    "hidden": false
  },
  {
    "name": "fetch-environments",
    "type": "boolean",
    "description": "Fetch the environments for your project from Zuplo. If this is false, then the environment will automatically be detected from the git branch.",
    "default": true,
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 link",
    "Link your local project to your Zuplo account"
  ],
  [
    "$0 link --account my-account --project my-project --environment my-env",
    "Explicitly specify the account, project, and environment"
  ]
]}
  usage="$0 link [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
