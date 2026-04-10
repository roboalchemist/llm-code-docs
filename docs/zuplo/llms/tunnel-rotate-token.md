# Source: https://www.zuplo.com/docs/cli/tunnel-rotate-token.md

# Zuplo CLI: Tunnel Rotate Token

<CliCommand
  command="tunnel rotate-token"
  description="Rotates the token for a tunnel in your account"
  options={[
  {
    "name": "tunnel-id",
    "type": "string",
    "description": "The ID of the tunnel to rotate the token for",
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 tunnel rotate-token --tunnel-id tnl_TRMZwunq2PLNQDwhu6A04Bmx",
    "Rotate the authentication token for a tunnel"
  ],
  [
    "$0 tunnel rotate-token \\\n  --tunnel-id tnl_TRMZwunq2PLNQDwhu6A04Bmx \\\n  --account my-account",
    "Explicitly specify the account"
  ]
]}
  usage="$0 tunnel rotate-token --tunnel-id <id> [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
