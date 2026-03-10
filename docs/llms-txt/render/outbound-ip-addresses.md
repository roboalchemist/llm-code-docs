# Source: https://render.com/docs/outbound-ip-addresses.md

# Outbound IP Addresses — Render services send traffic from specific IP ranges.


> *Outbound IPs were recently updated to use new ranges for each region.*
>
> [See details.](#changes-to-outbound-ips)

Render services send outbound traffic through specific sets of IP ranges depending on their [region](regions). You can use these ranges to connect your service to IP-restricted environments outside of Render.

Each IP range uses [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation). As an example, the range `216.24.60.0/24` represents the IP addresses from `216.24.60.0` to `216.24.60.255`, inclusive. Your service might use _any_ IP address within its associated ranges.

Outbound IP ranges are shared across _all_ services in the same region.

> *Interested in unique, Render-native static IPs for your workspace?*
>
> - Please upvote [this feature request](https://feedback.render.com/features/p/exclusive-not-shared-static-outbound-ips).
> - To ensure unique outbound IPs at this time, you can configure a static IP provider like [QuotaGuard](quotaguard).

## Obtaining your outbound IPs

*To obtain a service's outbound IP ranges:*

1. Open the [Render Dashboard](https://dashboard.render.com).
2. Click a service to open its details page.
3. Open the *Connect* dropdown in the upper right.
4. Switch to the *Outbound* tab. Copy the list of IP ranges:

   [image: List of outbound IP addresses in the Render Dashboard]

*Don't see the Outbound tab?*

- Make sure you're viewing the details page for a particular service, not your workspace home.
   - Note that [static sites](static-sites) don't use outbound IP addresses, because they can't initiate outbound traffic.
   - If you created your workspace before *January 23, 2022*, [see below](#exception-for-some-oregon-services).

### Exception for some Oregon services

*For workspaces created before January 23, 2022,* services in the Oregon [region](regions) do _not_ use a fixed set of outbound IP addresses. This remains the case after recent [changes to outbound IPs](#changes-to-outbound-ips).

You can configure outbound IP addresses for these Oregon-region services in one of the following ways:

- Configure a static IP provider like [QuotaGuard](quotaguard).
- Create a _new_ workspace, then create replacement Oregon-region services in that workspace. Migrate over any data, domains, and configuration.

## Changes to outbound IPs

On *November 13, 2025*, Render completed a migration to new outbound IP ranges for each [region](regions). Prior the migration, each region used a different, fixed set of individual IP addresses. Those individual addresses are now retired.

If you use your service's outbound IPs to authorize access to an external system, make sure to add the new IP ranges to that system's access rules:

1. Open your service's settings in the [Render Dashboard](https://dashboard.render.com) and click the *Connect* dropdown in the upper right.
2. Switch to the *Outbound* tab to view your service's new IP ranges:

   [image: List of outbound IP addresses in the Render Dashboard]

*Don't see the Outbound tab?*

- Make sure you're viewing the details page for a particular service, not your workspace home.
   - Note that [static sites](static-sites) don't use outbound IP addresses, because they can't initiate outbound traffic.
   - If you created your workspace before *January 23, 2022*, [see above](#exception-for-some-oregon-services).

3. Configure your external system to allow traffic from the listed ranges. Your service might connect from any address within these ranges.

4. If your external system allows connections from any of Render's original IP addresses, you can safely remove those addresses from your access rules.

## FAQ

###### What if my external system doesn't support allowlisting an entire CIDR range?

To limit your service's outbound traffic to a smaller number of IP addresses, you can configure a static IP provider like [QuotaGuard](quotaguard).

If you do, your service's outbound traffic will flow through your provider-managed IP(s), which you can then allow in your external system.

> *Interested in unique, Render-native static IPs for your workspace?*
>
> Please upvote [this feature request](https://feedback.render.com/features/p/exclusive-not-shared-static-outbound-ips).

