# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-endpoints-tcp-modify.md

# aptible endpoints:tcp:modify

This command modifies App [TCP Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/tcp-endpoints).

# Synopsis

```
Usage:
  aptible endpoints:tcp:modify [--app APP] ENDPOINT_HOSTNAME

Options:
  --env, [--environment=ENVIRONMENT]
      [--app=APP]
  -r, [--remote=REMOTE]
      [--ports=one two three]         # A list of ports to expose on this Endpoint
      [--ip-whitelist=one two three]  # A list of IPv4 sources (addresses or CIDRs) to which to restrict traffic to this Endpoint
      [--no-ip-whitelist]             # Disable IP Whitelist
```

# Examples

The options available for this command are similar to those available for [`aptible endpoints:tcp:create`](/reference/aptible-cli/cli-commands/cli-endpoints-tcp-create). Review the examples there.
