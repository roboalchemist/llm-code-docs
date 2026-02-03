# Source: https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/ip-filtering.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# IP Filtering

[Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview) support IP filtering. This lets you restrict access to Apps hosted on Aptible to a set of whitelisted IP addresses or networks and block other incoming traffic.

The maximum amount of IP sources (aka IPv4 addresses and CIDRs) per Endpoint available for IP filtering is 50. IPv6 is not currently supported.

# Use Cases

While IP filtering is no substitute for strong authentication, it is useful to:

* Further lock down access to sensitive apps and interfaces, such as admin dashboards or third-party apps you're hosting on Aptible for internal use only (For example: Kibana, Sentry).
* Restrict access to your Apps and APIs to a set of trusted customers or data partners.

If you’re hosting development Apps on Aptible, IP filtering can also help you make sure no one outside your company can view your latest and greatest before you're ready to release it to the world.

Note that IP filtering only applies to [Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview), not to [`aptible ssh`](/reference/aptible-cli/cli-commands/cli-ssh), [`aptible logs`](/reference/aptible-cli/cli-commands/cli-logs), and other backend access functionality provided by the [Aptible CLI](/reference/aptible-cli/cli-commands/overview).

# Enabling IP Filtering

IP filtering is configured via the Aptible Dashboard on a per-Endpoint basis:

* Edit an existing Endpoint or Add a new Endpoint
* Under the **IP Filtering** section, click to enable IP filtering.
* Add the list of IPs in the input area that appears
* Add more sources (IPv4 addresses and CIDRs) by separating them with spaces or newlines
* You must allow traffic from at least one source to enable IP filtering.

When IP Filtering is enabled for an Endpoint, other Apps within the same [Aptible Stack](/core-concepts/architecture/stacks) will no longer be able to connect to the Endpoint. To allow other Apps to connect, just add the Stack's [outbound IP addresses](/core-concepts/apps/connecting-to-apps/outbound-ips) to the list of allowed IPs.
