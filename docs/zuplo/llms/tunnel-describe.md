# Source: https://www.zuplo.com/docs/cli/tunnel-describe.md

# Zuplo CLI: Tunnel Describe

<CliCommand
  command="tunnel describe"
  description="Describes a tunnel in your account"
  options={[
  {
    "name": "tunnel-id",
    "type": "string",
    "description": "The ID of the tunnel to describe",
    "required": false,
    "deprecated": false,
    "hidden": false
  }
]}
  examples={[
  [
    "$0 tunnel describe --tunnel-id tnl_TRMZwunq2PLNQDwhu6A04Bmx",
    "Get details about a tunnel"
  ],
  [
    "$0 tunnel describe --tunnel-id tnl_TRMZwunq2PLNQDwhu6A04Bmx --account my-account",
    "Explicitly specify the account"
  ]
]}
  usage="$0 tunnel describe --tunnel-id <id> [options]"
>

**Additional Resources**

- [Secure Tunnels](../articles/secure-tunnel.mdx)
- [Tunnel Setup & Configuration](../articles/tunnel-setup.mdx)
- [Tunnel Troubleshooting](../articles/tunnel-troubleshooting.mdx)

</CliCommand>

## Global options

The following global options are available for all commands:

- [`--help`](./global-options.mdx#help)
- [`--api-key`](./global-options.mdx#api-key)
