# Source: https://www.zuplo.com/docs/cli/source-upgrade.md

# Zuplo CLI: Source Upgrade

<CliCommand
  command="source upgrade"
  description="Updates your project structure to the latest conventions"
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
  }
]}
  examples={[
  [
    "$0 source upgrade",
    "Upgrade your project structure to the latest conventions"
  ],
  [
    "$0 source upgrade --dir ./my-zuplo-project",
    "Specify the project directory path"
  ]
]}
  usage="$0 source upgrade [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
