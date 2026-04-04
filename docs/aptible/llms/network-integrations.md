# Source: https://www.aptible.com/docs/core-concepts/integrations/network-integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Network Integrations: VPC Peering & VPN Tunnels

# VPC Peering

<Info> VPC Peering is only available on [Production and Enterprise plans.](https://www.aptible.com/pricing)</Info>

Aptible offers VPC Peering to connect a user’s existing network to their Aptible dedicated VPC. This lets users access internal Aptible resources such as [Internal Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview) and [Databases](/core-concepts/managed-databases/managing-databases/overview) from their network.

## Setup

VPC Peering requests can be submitted through the Aptible Dashboard:

<Steps>
  <Step title="Navigate to VPC Peering">
    Go to the Dedicated Stack where you want to create the peering connection and select the **VPC Peering** tab.
  </Step>

  <Step title="Create VPC Peering Request">
    Click **Create VPC Peering Request**. Only Account Owners can create VPC peering requests.
  </Step>

  <Step title="Select Peering Type">
    Choose your peering destination:

    * **Peer to AWS Account**: Connect your Aptible stack to an external AWS VPC you own
    * **Peer to Aptible Dedicated Stack**: Connect two of your Aptible dedicated stacks together
  </Step>
</Steps>

### Peering to an AWS Account

When peering to an external AWS VPC:

1. The Dashboard displays your Aptible VPC information (AWS Account ID, VPC ID, Region, and CIDR) needed to create the peering connection in AWS.
2. Go to the [Peering Connections page](https://console.aws.amazon.com/vpc/home#PeeringConnections) in the AWS VPC Dashboard and click **Create VPC Peering Connection**.
3. Select your own VPC as the local VPC and enter the Aptible VPC details (shown in the Dashboard) for the peer VPC.
4. After creating the peering connection in AWS, copy the **VPC Peering Connection ID** (starts with `pcx-`) and enter it in the Aptible Dashboard form.
5. Submit the request. The Aptible team will accept the peering connection and follow up with next steps.

### Peering to Another Aptible Dedicated Stack

When peering two Aptible dedicated stacks together:

1. Select the target dedicated stack from the dropdown.
2. Submit the request. The Aptible team will configure the peering connection between your stacks.

<Note>
  You must have at least two dedicated stacks to use this option.
</Note>

## Managing VPC Peering

The details and status of VPC Peering connections can be viewed within the Aptible Dashboard by:

* Navigating to the respective Dedicated Stack
* Selecting the "VPC Peering" tab

### Requesting Deletion

To request deletion of a VPC peering connection:

1. Navigate to the Dedicated Stack and select the **VPC Peering** tab.
2. Find the peering connection you want to delete and click **Request Deletion**.
3. Confirm by typing the connection ID.
4. Submit the request. The Aptible team will process the deletion.

<Note>
  Only Account Owners can request VPC peering deletion.
</Note>

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
