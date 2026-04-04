# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-endpoints-tls-modify.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible endpoints:tls:modify

This command lets you modify [TLS Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/tls-endpoints).

# Synopsis

```
Usage:
  aptible endpoints:tls:modify [--app APP] ENDPOINT_HOSTNAME

Options:
  --env, [--environment=ENVIRONMENT]
      [--app=APP]
  -r, [--remote=REMOTE]
      [--ports=one two three]                              # A list of ports to expose on this Endpoint
      [--ip-whitelist=one two three]                       # A list of IPv4 sources (addresses or CIDRs) to which to restrict traffic to this Endpoint
      [--no-ip-whitelist]                                  # Disable IP Whitelist
      [--certificate-file=CERTIFICATE_FILE]                # A file containing a certificate to use on this Endpoint
      [--private-key-file=PRIVATE_KEY_FILE]                # A file containing a private key to use on this Endpoint
      [--managed-tls], [--no-managed-tls]                  # Enable Managed TLS on this Endpoint
      [--managed-tls-domain=MANAGED_TLS_DOMAIN]            # A domain to use for Managed TLS
      [--certificate-fingerprint=CERTIFICATE_FINGERPRINT]  # The fingerprint of an existing Certificate to use on this Endpoint
```

# Examples

The options available for this command are similar to those available for [`aptible endpoints:tls:create`](/reference/aptible-cli/cli-commands/cli-endpoints-tls-create). Review the examples there.
