# Source: https://www.aptible.com/docs/core-concepts/integrations/network-integrations.md

# Network Integrations: VPC Peering & VPN Tunnels

# VPC Peering

<Info> VPC Peering is only available on [Production and Enterprise plans.](https://www.aptible.com/pricing)</Info>

Aptible offers VPC Peering to connect a user’s existing network to their Aptible dedicated VPC. This lets users access internal Aptible resources such as [Internal Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview) and [Databases](/core-concepts/managed-databases/managing-databases/overview) from their network.

## Setup

VPC Peering connections can only be set up by contacting [Aptible Support](/how-to-guides/troubleshooting/aptible-support).

## Managing VPC Peering

VPC Peering connections can only be managed by the Aptible Support Team. This includes deprovisioning VPC Peering connections.

The details and status of VPC Peering connections can be viewed within the Aptible Dashboard by:

* Navigating to the respective Dedicated Stack
* Selecting the "VPC Peering" tab

# VPN Tunnels

<Info> VPN Tunnels are only available on [Production and Enterprise plans.](https://www.aptible.com/pricing) </Info>

Aptible supports site-to-site VPN Tunnels to connect external networks to your Aptible resources. VPN Tunnels are only available on dedicated stacks.

The default protocol for all new VPN Tunnels is IKEv2.

## Setup

VPN Tunnels can only be set up by contacting Aptible Support.

Please provide the following information when you contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) with your tunnel setup request:

* What resources on the Aptible Stack must be exposed over the tunnel? Aptible can expose:
  * Individual resources. Please share the hostname of the Internal [Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview) (elb-xxxxx.aptible.in) and the names of the [Databases](/core-concepts/managed-databases/overview) that need to be made accessible over the tunnel.
  * The entire Stack - only recommended if users own the network Aptible is integrating.
  * No resources - or users who need to access resources on the other end of the tunnel without exposing Aptible-side resources.
* Is outbound access from the Stack to the resources exposed on the other end of the tunnel required?

Aptible Support will follow up with a VPN Implementation Worksheet that can be shared with the tunnel partner.

> ❗️Road-warrior VPNs are **not** supported on Aptible. To provide road-warrior users with VPN access to Aptible resources, set up a VPN gateway on a user-owned network and have users connect there, then create a site-to-site VPN tunnel between the user-owned network and the Aptible Dedicated Stack.

## Managing VPN Tunnels

VPN Tunnels can only be managed by the Aptible Support Team. This includes deprovisioning VPN Tunnels.

The details and status of VPN Tunnels can be viewed within the Aptible Dashboard by:

* Navigating to the respective Dedicated Stack
* Selecting the "VPN Tunnels" tab

There are four statuses that you might see in this view:

* `Up`: The connection is fully up
* `Down`: The connection is fully down - consider contacting your partner or Aptible Support
* `Partial`: The connection is in a mixed up/down state, usually because your tunnel is configured as a "connect when there is activity" tunnel, and some connections are not being used
* `Unknown`: Something has gone wrong with the status check; please check again later or reach out to Aptible Support if you are having problems
