# Source: https://www.zuplo.com/docs/cli/tunnel-create.md

# Zuplo CLI: Tunnel Create

<CliCommand
  command="tunnel create"
  description="Creates a new tunnel in your account"
  options={[
  {
    "name": "tunnel-name",
    "type": "string",
    "description": "The name of the tunnel to create",
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
    "$0 tunnel create --tunnel-name my-tunnel",
    "Create a new tunnel"
  ],
  [
    "$0 tunnel create --tunnel-name production-tunnel --account my-account",
    "Explicitly specify the account"
  ]
]}
  usage="$0 tunnel create --tunnel-name <name> [options]"
>

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)

## Additional resources

- [Secure Tunnels](../articles/secure-tunnel.mdx)
- [Tunnel Setup & Configuration](../articles/tunnel-setup.mdx)
- [Tunnel Troubleshooting](../articles/tunnel-troubleshooting.mdx)
