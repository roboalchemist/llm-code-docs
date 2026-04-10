# Source: https://www.zuplo.com/docs/cli/tunnel-services-update.md

# Zuplo CLI: Tunnel Services Update

<CliCommand
  command="tunnel services update"
  description="Updates the services for this tunnel"
  options={[
  {
    "name": "configuration-file",
    "type": "string",
    "description": "The path to the configuration file",
    "required": false,
    "deprecated": false,
    "hidden": false,
    "normalize": true
  },
  {
    "name": "tunnel-id",
    "type": "string",
    "description": "The ID of the tunnel containing the services",
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 tunnel services update \\\n  --tunnel-id tnl_TRMZwunq2PLNQDwhu6A04Bmx \\\n  --configuration-file ./services.json",
    "Update the services configuration for a tunnel"
  ],
  [
    "$0 tunnel services update \\\n  --tunnel-id tnl_TRMZwunq2PLNQDwhu6A04Bmx \\\n  --configuration-file ./config/tunnel-services.json \\\n  --account my-account",
    "Explicitly specify the account"
  ]
]}
  usage="$0 tunnel services update --tunnel-id <id> --configuration-file <file> [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
