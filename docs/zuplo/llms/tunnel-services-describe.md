# Source: https://www.zuplo.com/docs/cli/tunnel-services-describe.md

# Zuplo CLI: Tunnel Services Describe

<CliCommand
  command="tunnel services describe"
  description="Describes the services for this tunnel"
  options={[
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
    "$0 tunnel services describe --tunnel-id tnl_TRMZwunq2PLNQDwhu6A04Bmx",
    "View the services configuration for a tunnel"
  ],
  [
    "$0 tunnel services describe \\\n  --tunnel-id tnl_TRMZwunq2PLNQDwhu6A04Bmx \\\n  --account my-account",
    "Explicitly specify the account"
  ]
]}
  usage="$0 tunnel services describe --tunnel-id <id> [options]"
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
