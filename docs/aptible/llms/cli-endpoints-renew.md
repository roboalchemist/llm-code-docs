# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-endpoints-renew.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible endpoints:renew

This command triggers an initial renewal of a [Managed TLS](/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls) Endpoint after creating it using [`aptible endpoints:https:create`](/reference/aptible-cli/cli-commands/cli-endpoints-https-create) or [`aptible endpoints:tls:create`](/reference/aptible-cli/cli-commands/cli-endpoints-tls-create) and having set up the required [Managed HTTPS Validation Records](/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls#managed-https-validation-records).

> ⚠️ We recommend reviewing the documentation on [rate limits](/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls#rate-limits) before using this command automatically.\
> \
> 📘 You only need to do this once! After initial provisioning, Aptible automatically renews your Managed TLS certificates on a periodic basis.

# Synopsis

> 📘  Use the [`aptible endpoints:list`](/reference/aptible-cli/cli-commands/cli-endpoints-list) command to easily locate the [Endpoint Hostname](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain#endpoint-hostname) for a given Endpoint.

```
Usage:
  aptible endpoints:renew [--app APP] ENDPOINT_HOSTNAME

Options:
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]
```
