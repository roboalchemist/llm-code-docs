# Source: https://developers.cloudflare.com/magic-transit/llms.txt

# Magic Transit

Network functions at Cloudflare scale for on-premise, cloud-hosted, and hybrid networks

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/magic-transit/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Magic Transit llms-full.txt](https://developers.cloudflare.com/magic-transit/llms-full.txt) for the complete Magic Transit documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare Magic Transit](https://developers.cloudflare.com/magic-transit/index.md)

## About

- [About](https://developers.cloudflare.com/magic-transit/about/index.md)

## Get started

- [Get started](https://developers.cloudflare.com/magic-transit/get-started/index.md)

## Network health

- [Network health](https://developers.cloudflare.com/magic-transit/network-health/index.md)
- [Check tunnel health in the dashboard](https://developers.cloudflare.com/magic-transit/network-health/check-tunnel-health-dashboard/index.md)
- [Configure tunnel health alerts](https://developers.cloudflare.com/magic-transit/network-health/configure-tunnel-health-alerts/index.md): Set up and configure tunnel health alerts
- [How Cloudflare calculates tunnel health alerts](https://developers.cloudflare.com/magic-transit/network-health/magic-tunnel-health-check-calculation/index.md)
- [Run endpoint health checks (beta)](https://developers.cloudflare.com/magic-transit/network-health/run-endpoint-health-checks/index.md)
- [Update tunnel health checks frequency](https://developers.cloudflare.com/magic-transit/network-health/update-tunnel-health-checks-frequency/index.md)

## DDoS protection

- [DDoS protection](https://developers.cloudflare.com/magic-transit/ddos/index.md)

## Analytics

- [Analytics](https://developers.cloudflare.com/magic-transit/analytics/index.md): Use Magic Transit analytics to monitor network performance and troubleshoot potential issues.
- [Network Analytics](https://developers.cloudflare.com/magic-transit/analytics/network-analytics/index.md)
- [Packet captures](https://developers.cloudflare.com/magic-transit/analytics/packet-captures/index.md)
- [Query Magic Transit tunnel bandwidth analytics with GraphQL](https://developers.cloudflare.com/magic-transit/analytics/query-bandwidth/index.md)
- [Query Magic Transit tunnel health check results with GraphQL](https://developers.cloudflare.com/magic-transit/analytics/query-tunnel-health/index.md)
- [Traceroutes](https://developers.cloudflare.com/magic-transit/analytics/traceroutes/index.md)

## Network Flow

- [Network Flow](https://developers.cloudflare.com/magic-transit/network-flow/index.md)

## Cloudflare IPs

- [Cloudflare IPs](https://developers.cloudflare.com/magic-transit/cloudflare-ips/index.md)

## Magic Transit on-demand

- [Magic Transit on-demand](https://developers.cloudflare.com/magic-transit/on-demand/index.md)

## Network Interconnect (CNI)

- [Network Interconnect (CNI)](https://developers.cloudflare.com/magic-transit/network-interconnect/index.md)

## Alerts

- [Alerts](https://developers.cloudflare.com/magic-transit/alerts/index.md)

## Changelog

- [Changelog](https://developers.cloudflare.com/magic-transit/changelog/index.md): Review recent changes to Magic Transit.

## Glossary

- [Glossary](https://developers.cloudflare.com/magic-transit/glossary/index.md)

## how-to

- [Advertise prefixes](https://developers.cloudflare.com/magic-transit/how-to/advertise-prefixes/index.md)
- [Configure routes](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/index.md): Magic Transit uses a static configuration to route your traffic through anycast tunnels from Cloudflare's global network to your locations. If you are connected through CNI with Dataplane v2, you also have access to BGP peering (beta).
- [Configure tunnel endpoints](https://developers.cloudflare.com/magic-transit/how-to/configure-tunnel-endpoints/index.md): Cloudflare recommends two tunnels for each ISP and network location router combination, one per Cloudflare endpoint. Learn how to configure IPsec or GRE tunnels.
- [Enable Magic user roles](https://developers.cloudflare.com/magic-transit/how-to/enable-magic-roles/index.md): You can determine which users have, or do not have, configuration edit access for Magic products.
- [Configure IPv6 (beta)](https://developers.cloudflare.com/magic-transit/how-to/ipv6/index.md)
- [Safely withdraw a BYOIP prefix](https://developers.cloudflare.com/magic-transit/how-to/safely-withdraw-byoip-prefix/index.md)

## partners

- [Kentik](https://developers.cloudflare.com/magic-transit/partners/kentik/index.md): Kentik is a network observability company that helps detect attacks on your network and triggers Cloudflare's Magic Transit to begin advertisement. The example scenario includes two mitigations, one which pulls the advertisement from the router and a second mitigation that makes an API call to Cloudflare.

## reference

- [Anti-replay protection](https://developers.cloudflare.com/magic-transit/reference/anti-replay-protection/index.md): If you use Magic Transit and anycast IPsec tunnels, disable anti-replay protection. Review the information to learn more.
- [Bandwidth measurement](https://developers.cloudflare.com/magic-transit/reference/bandwidth-measurement/index.md)
- [Egress traffic](https://developers.cloudflare.com/magic-transit/reference/egress/index.md)
- [GRE and IPsec tunnels](https://developers.cloudflare.com/magic-transit/reference/gre-ipsec-tunnels/index.md): Magic Transit uses Generic Routing Encapsulation (GRE) and IPsec tunnels to transmit packets from Cloudflare's global network to your origin network.
- [How Cloudflare calculates tunnel health alerts](https://developers.cloudflare.com/magic-transit/reference/how-cloudflare-calculates-tunnel-health-alerts/index.md)
- [Maximum transmission unit and maximum segment size](https://developers.cloudflare.com/magic-transit/reference/mtu-mss/index.md)
- [Reference architecture](https://developers.cloudflare.com/magic-transit/reference/reference-architecture/index.md)
- [Traffic steering](https://developers.cloudflare.com/magic-transit/reference/traffic-steering/index.md): Magic Transit uses a static configuration to route traffic through anycast tunnels using the Generic Routing Encapsulation (GRE) and Internet Protocol Security (IPsec) protocols from Cloudflare's global network to your network.
- [Tunnel health checks](https://developers.cloudflare.com/magic-transit/reference/tunnel-health-checks/index.md): Magic Transit uses probes to check for tunnel health. Review information on this page to learn more.

## troubleshooting

- [Troubleshoot connectivity](https://developers.cloudflare.com/magic-transit/troubleshooting/connectivity/index.md)
- [Troubleshoot with IPsec logs](https://developers.cloudflare.com/magic-transit/troubleshooting/ipsec-troubleshoot/index.md)
- [Troubleshoot routing and BGP](https://developers.cloudflare.com/magic-transit/troubleshooting/routing-and-bgp/index.md)
- [Troubleshoot tunnel health](https://developers.cloudflare.com/magic-transit/troubleshooting/tunnel-health/index.md)