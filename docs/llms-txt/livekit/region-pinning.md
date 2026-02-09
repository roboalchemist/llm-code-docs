# Source: https://docs.livekit.io/telephony/features/region-pinning.md

# Source: https://docs.livekit.io/deploy/admin/regions/region-pinning.md

# Source: https://docs.livekit.io/telephony/features/region-pinning.md

LiveKit docs › Features › Region pinning

---

# Region pinning for telephony

> Learn how to isolate LiveKit telephony traffic to a specific region.

## Overview

LiveKit SIP is part of LiveKit Cloud and runs as a globally distributed service, providing redundancy and high availability. By default, SIP endpoints are global, and calls are routed through the region closest to the origination point. Incoming calls are routed to the region closest to the SIP trunking provider's endpoint. Outgoing calls originate from the same region where the `CreateSIPParticipant` API call is made.

In most cases, using the global endpoint is the recommended approach. However, if you need to exercise more control over call routing—for example, to comply with local telephony regulations—LiveKit SIP supports region pinning. This allows you to restrict both incoming and outgoing calls to a specific region.

## Region pinning

Region pinning allows you to restrict calls to a specific region to comply with local telephony regulations. The following sections describe how to enable region pinning for inbound and outbound calls.

> ℹ️ **Protocol-based region pinning**
> 
> For realtime SDKs, you can use protocol-based region pinning to restrict traffic to a specific region. To learn more, see [Region pinning](https://docs.livekit.io/deploy/admin/regions/region-pinning.md).

### Inbound calls

To enable region pinning for incoming calls, configure your SIP trunking provider to use a region-based endpoint. A region-based endpoint is configured to direct traffic only to nodes within a specific region.

#### Region-based endpoint format

The endpoint format is as follows:

```
{sip_subdomain}.{region_name}.sip.livekit.cloud

```

Where:

- `{sip_subdomain}` is your LiveKit SIP URI subdomain. This is also your project ID without the `p_` prefix. You can find your SIP URI on the [Project settings](https://cloud.livekit.io/projects/p_/settings/project) page.

For example, if your SIP URI is `sip:bwwn08a2m4o.sip.livekit.cloud`, your SIP subdomain is `bwwn08a2m4o`.
- `{region_name}` is one of the following [regions](#available-regions):

`eu`, `india`, `sa`, `us`

For example to create a SIP endpoint for India, see the following:

> 💡 **Tip**
> 
> Sign in to LiveKit Cloud to automatically include the subdomain for your project in the example.

```shell
%{regionalEndpointSubdomain}%.india.sip.livekit.cloud

```

Use the region-based endpoint to configure your SIP trunking provider. Follow the instructions for external provider setup in [SIP trunk setup](https://docs.livekit.io/telephony/start/sip-trunk-setup.md).

### Outbound calls

To originate calls from the same region as the destination phone number, set the `destination_country` parameter for an outbound trunk. This applies region pinning to all calls made through the trunk. When `destination_country` is enabled, outbound calls are routed based on location:

- For countries that LiveKit operates data centers in, calls originate from a server within the country.
- For other countries, calls originate from a server that is closest to that country.

In the unlikely event that the preferred region is non-operational or offline, calls originate from another region nearby. For a full list of supported regions, see [Available regions](#available-regions).

The `destination_country` parameter accepts a two-letter [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). To learn more, see [CreateSIPOutboundTrunk](https://docs.livekit.io/reference/telephony/sip-api.md#createsipoutboundtrunk).

#### Example outbound trunk

Create an outbound trunk with the `destination_country` parameter set to India, `india`.

1. Create a file named `outbound-trunk.json`, replacing the phone number with your SIP provider phone number and username and password:

```json
{
  "trunk": {
    "name": "My outbound trunk",
    "phone_number": "+15105550100",
    "username": "myusername",
    "password": "mypassword",
    "destination_country": "in"
  }
}

```
2. Create the outbound trunk using the CLI:

```shell
lk sip outbound create outbound-trunk.json

```

To learn more, see [Outbound trunks](https://docs.livekit.io/telephony/making-calls/outbound-trunk.md).

### Available regions

The following regions are available for region pinning for SIP:

| Region name | Region locations |
| `eu` | France, Germany, Zurich |
| `india` | India |
| `sa` | Saudi Arabia |
| `us` | US Central, US East B, US West B |
| `aus` | Australia |
| `uk` | United Kingdom |

> ℹ️ **Note**
> 
> This list of regions is subject to change. Last updated 2025-09-29.

## Additional resources

The following additional topics provide more information about regions and region pinning.

- **[Region pinning](https://docs.livekit.io/deploy/admin/regions/region-pinning.md)**: Restrict network traffic to specific regions with protocol-based region pinning and realtime SDKs.

- **[Agent deployment](https://docs.livekit.io/deploy/admin/regions/agent-deployment.md)**: Deploy agents to specific regions to optimize latency and manage regional deployments.

---

This document was rendered at 2026-02-03T03:25:11.183Z.
For the latest version of this document, see [https://docs.livekit.io/telephony/features/region-pinning.md](https://docs.livekit.io/telephony/features/region-pinning.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).