# Source: https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/outbound-ips.md

# Outbound IP Addresses

> Learn about using outbound IP addresses to create an allowlist

# Overview

You can share an app's outbound IP address pool with partners or vendors that use an allowlist.

<Note> [Stacks](/core-concepts/architecture/stacks) have a single NAT gateway, and all requests originating from an app use the outbound IP addresses associated with that NAT gateway's IP address.</Note>

These IP addresses are *different* from the IP addresses associated with an app's [Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview), which are used for *inbound* requests.

The outbound IP addresses for an app *may* change for the following reasons:

1. Aptible migrates the [Environment](/core-concepts/architecture/environments) the app is deployed on to a new [stack](/core-concepts/architecture/stacks)
2. Failure of the underlying NAT instance
3. Failover to minimize downtime during maintenance

In either case, Aptible selects the new IP address from a pool of pre-defined IP addresses associated with the NAT gateway. This set pool will not change without notification from Aptible.

<Warning> For this reason, when sharing IP addresses with vendors or partners for whitelisting, ensure all of the provided outbound IP addresses are whitelisted. </Warning>

# Determining Outbound IP Address Pool

Your outbound IP address pool can be identified by navigating to the [Stack](/core-concepts/architecture/stacks) with the Aptible Dashboard.
