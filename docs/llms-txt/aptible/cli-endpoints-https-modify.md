# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-endpoints-https-modify.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible endpoints:https:modify

This command modifies an existing App [HTTP(S) Endpoint.](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview)

> 📘 Tip: Use the [`aptible endpoints:list`](/reference/aptible-cli/cli-commands/cli-endpoints-list) command to easily locate the [Endpoint Hostname](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain#endpoint-hostname) for a given Endpoint.

# Synopsis

```
Usage:
  aptible endpoints:https:modify [--app APP] ENDPOINT_HOSTNAME

Options:
  --env, [--environment=ENVIRONMENT]
      [--app=APP]
  -r, [--remote=REMOTE]
      [--port=N]                                                       # A port to expose on this Endpoint
      [--load-balancing-algorithm-type=LOAD_BALANCING_ALGORITHM_TYPE]  # The load balancing algorithm for this Endpoint. Valid options are round_robin, least_outstanding_requests, and weighted_random
      [--ip-whitelist=one two three]                                   # A list of IPv4 sources (addresses or CIDRs) to which to restrict traffic to this Endpoint
      [--no-ip-whitelist]                                              # Disable IP Whitelist
      [--certificate-file=CERTIFICATE_FILE]                            # A file containing a certificate to use on this Endpoint
      [--private-key-file=PRIVATE_KEY_FILE]                            # A file containing a private key to use on this Endpoint
      [--managed-tls], [--no-managed-tls]                              # Enable Managed TLS on this Endpoint
      [--managed-tls-domain=MANAGED_TLS_DOMAIN]                        # A domain to use for Managed TLS
      [--certificate-fingerprint=CERTIFICATE_FINGERPRINT]              # The fingerprint of an existing Certificate to use on this Endpoint
      [--shared], [--no-shared]                                        # Share this Endpoint's load balancer with other Endpoints
```

# Examples

The options available for this command are similar to those available for [`aptible endpoints:https:create`](/reference/aptible-cli/cli-commands/cli-endpoints-https-create). Review the examples there.
