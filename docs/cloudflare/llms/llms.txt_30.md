# Source: https://developers.cloudflare.com/cloudflare-wan/llms.txt

# Cloudflare WAN

Replace legacy WAN and securely connect any traffic source to Cloudflare's network

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/cloudflare-wan/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Cloudflare WAN llms-full.txt](https://developers.cloudflare.com/cloudflare-wan/llms-full.txt) for the complete Cloudflare WAN documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/index.md)

## WAN transformation

- [WAN transformation](https://developers.cloudflare.com/cloudflare-wan/wan-transformation/index.md)

## Get started

- [Get started](https://developers.cloudflare.com/cloudflare-wan/get-started/index.md)

## On-ramps

- [On-ramps](https://developers.cloudflare.com/cloudflare-wan/on-ramps/index.md)

## Security filters

- [Security filters](https://developers.cloudflare.com/cloudflare-wan/security/index.md)

## Cloudflare One integration

- [Cloudflare One integration](https://developers.cloudflare.com/cloudflare-wan/zero-trust/index.md): Learn how to integrate Cloudflare WAN (formerly Magic WAN) with other Cloudflare Cloudflare One products, such as Cloudflare Gateway and the Cloudflare One Client.
- [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-gateway/index.md)
- [WARP](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-one-client/index.md): Use the Cloudflare One Client as an on-ramp to Cloudflare WAN and route traffic from user devices with the Cloudflare One Client installed to any network connected with Cloudflare Tunnel or Magic IP-layer tunnels (anycast GRE, IPsec, or CNI).
- [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-tunnel/index.md)
- [Connectivity options](https://developers.cloudflare.com/cloudflare-wan/zero-trust/connectivity-options/index.md)
- [Secure WAN traffic](https://developers.cloudflare.com/cloudflare-wan/zero-trust/security-services/index.md): Which security services apply to WAN traffic and when to use them.

## Network Interconnect (CNI)

- [Network Interconnect (CNI)](https://developers.cloudflare.com/cloudflare-wan/network-interconnect/index.md)

## Load Balancing

- [Load Balancing](https://developers.cloudflare.com/cloudflare-wan/load-balancing/index.md)

## Analytics

- [Analytics](https://developers.cloudflare.com/cloudflare-wan/analytics/index.md): Use Cloudflare WAN analytics to monitor site performance and troubleshoot issues.
- [NetFlow statistics](https://developers.cloudflare.com/cloudflare-wan/analytics/netflow-analytics/index.md)
- [Network analytics](https://developers.cloudflare.com/cloudflare-wan/analytics/network-analytics/index.md)
- [Packet captures](https://developers.cloudflare.com/cloudflare-wan/analytics/packet-captures/index.md)
- [Querying Cloudflare WAN IPsec/GRE tunnel bandwidth analytics with GraphQL](https://developers.cloudflare.com/cloudflare-wan/analytics/query-bandwidth/index.md)
- [Querying Cloudflare WAN IPsec/GRE tunnel health check results with GraphQL](https://developers.cloudflare.com/cloudflare-wan/analytics/query-tunnel-health/index.md)
- [Network overview](https://developers.cloudflare.com/cloudflare-wan/analytics/site-analytics/index.md)
- [Traceroutes](https://developers.cloudflare.com/cloudflare-wan/analytics/traceroutes/index.md)

## Changelog

- [Changelog](https://developers.cloudflare.com/cloudflare-wan/changelog/index.md): Review recent changes to Cloudflare WAN (formerly Magic WAN).

## Glossary

- [Glossary](https://developers.cloudflare.com/cloudflare-wan/glossary/index.md)

## configuration

- [Configure with Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/index.md)
- [Configure hardware Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/index.md)
- [SFP+ port information](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/sfp-port-information/index.md)
- [Configure Virtual Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/index.md): Learn how to configure Cloudflare One Virtual Appliance on VMWare ESXi or Proxmox Virtual Environment
- [Device metrics](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/device-metrics/index.md)
- [Activate Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/activate-appliance/index.md)
- [Deactivate Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/deactivate-appliance/index.md)
- [Default password](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/default-password/index.md): Information about Cloudflare One Appliance's default password.
- [Edit basic information](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/edit-basic-info/index.md)
- [Edit network settings](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/edit-network-settings/index.md)
- [Edit sites](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/edit-sites/index.md)
- [Edit traffic steering settings](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/edit-traffic-steering-settings/index.md)
- [Heartbeat](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/heartbeat/index.md)
- [Interrupt window](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/index.md): Learn how to set up when Cloudflare One Appliance can update its systems.
- [Register a hardware Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/register-appliance/index.md)
- [Remove appliances](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/remove-appliances/index.md)
- [Application-aware policies](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/index.md)
- [Breakout traffic](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/index.md): Breakout traffic allows you to define which applications should bypass Cloudflare's security filtering.
- [Prioritized traffic](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/index.md): Prioritized traffic allows you to define which applications are processed first by Cloudflare One Appliance.
- [DHCP relay](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-relay/index.md)
- [DHCP server](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/index.md)
- [DHCP static address reservation](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-static-address-reservation/index.md)
- [Enable NAT for a subnet](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/nat-subnet/index.md): Enable static NAT for subnets in Cloudflare One Appliance to re-use address spaces locally.
- [Network segmentation](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/network-segmentation/index.md): Define policies to determine if traffic should flow between your LANs without leaving your local premises, or if traffic should be forwarded to Cloudflare for additional security configurations.
- [Routed subnets](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/routed-subnets/index.md): Learn how to configure routed subnets on a Cloudflare One Appliance, including setting static routes and next-hop addresses for complex LAN setups.
- [Reference](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/reference/index.md)
- [Troubleshooting](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/troubleshooting/index.md)
- [Check tunnel health in the dashboard](https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/index.md)
- [Configure Tunnel Health Alerts](https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/configure-tunnel-health-alerts/index.md): Use the API to set up and configure Tunnel Health Alerts
- [Custom IKE ID for IPsec](https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/custom-ike-id-ipsec/index.md)
- [Enable user roles](https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/enable-roles/index.md): You can determine which users have, or do not have, configuration edit access for Magic products.
- [Set up a site](https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/sites/index.md)
- [Update tunnel health checks frequency](https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/update-tunnel-health-checks-frequency/index.md)
- [Configure Cloudflare source IPs (beta)](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/how-to/configure-cloudflare-source-ips/index.md): Configure the Cloudflare source IP range used when you receive traffic from Cloudflare services sent to your Cloudflare One private networks.
- [Configure routes](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/how-to/configure-routes/index.md): Cloudflare WAN uses a static configuration to route your traffic through anycast tunnels from Cloudflare's global network to your locations. If you are connected through CNI with Dataplane v2, you also have access to BGP peering (beta). Learn how to configure routing.
- [Configure tunnel endpoints](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/how-to/configure-tunnel-endpoints/index.md): Cloudflare recommends two tunnels for each ISP and network location router combination, one per Cloudflare endpoint. Learn how to configure IPsec or GRE tunnels.
- [Run traceroute](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/how-to/traceroute/index.md): Learn what settings you need to change to perform a useful `traceroute` to an endpoint behind a Cloudflare Tunnel.
- [Alibaba Cloud VPN Gateway](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/alibaba-cloud/index.md)
- [Aruba EdgeConnect Enterprise](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/aruba-edgeconnect/index.md)
- [Amazon AWS Transit Gateway](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/aws/index.md)
- [Microsoft Azure Virtual WAN](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/azure/azure-virtual-wan/index.md)
- [Microsoft Azure VPN Gateway](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/azure/azure-vpn-gateway/index.md)
- [Cisco IOS XE](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/cisco-ios-xe/index.md)
- [Furukawa Electric FITELnet](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/fitelnet/index.md)
- [Fortinet](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/fortinet/index.md)
- [Google Cloud VPN](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/google/index.md)
- [Juniper Networks SRX Series Firewalls](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/juniper/index.md)
- [Oracle Cloud](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/oracle/index.md)
- [Palo Alto Networks NGFW](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/palo-alto/index.md)
- [pfSense](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/pfsense/index.md)
- [SonicWall](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/sonicwall/index.md)
- [Sophos Firewall](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/sophos-firewall/index.md)
- [strongSwan](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/strongswan/index.md)
- [Ubiquiti](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/ubiquiti/index.md)
- [Velocloud](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/velocloud/index.md)
- [Cisco SD-WAN](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/viptela/index.md)
- [VyOS](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/vyos/index.md)
- [Yamaha RTX Router](https://developers.cloudflare.com/cloudflare-wan/configuration/manually/third-party/yamaha/index.md)
- [Configure cloud on-ramps](https://developers.cloudflare.com/cloudflare-wan/configuration/multi-cloud-networking/index.md): Use Multi-Cloud Networking to quickly and easily discover resources on your cloud provider, and configure them automatically.

## legal

- [Third party licenses](https://developers.cloudflare.com/cloudflare-wan/legal/3rdparty/index.md)

## reference

- [Anti-replay protection](https://developers.cloudflare.com/cloudflare-wan/reference/anti-replay-protection/index.md): If you use Cloudflare WAN and anycast IPsec tunnels, you will need to disable anti-replay protection. Review the information here to learn more.
- [Bandwidth measurement](https://developers.cloudflare.com/cloudflare-wan/reference/bandwidth-measurement/index.md)
- [Device compatibility](https://developers.cloudflare.com/cloudflare-wan/reference/device-compatibility/index.md)
- [GRE and IPsec tunnels](https://developers.cloudflare.com/cloudflare-wan/reference/gre-ipsec-tunnels/index.md): Cloudflare WAN uses Generic Routing Encapsulation (GRE) and IPsec tunnels to transmit packets from Cloudflare's global network to your origin network.
- [How Cloudflare calculates tunnel health alerts](https://developers.cloudflare.com/cloudflare-wan/reference/how-cloudflare-calculates-tunnel-health-alerts/index.md)
- [Maximum transmission unit and maximum segment size](https://developers.cloudflare.com/cloudflare-wan/reference/mtu-mss/index.md)
- [Traffic steering](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/index.md): Cloudflare WAN uses a static configuration to route traffic through anycast tunnels using the Generic Routing Encapsulation (GRE) and Internet Protocol Security (IPsec) protocols from Cloudflare's global network to your network.
- [Tunnel health checks](https://developers.cloudflare.com/cloudflare-wan/reference/tunnel-health-checks/index.md): Cloudflare WAN uses probes to check for tunnel health. Review information on this page to learn more.

## troubleshooting

- [Troubleshoot connectivity](https://developers.cloudflare.com/cloudflare-wan/troubleshooting/connectivity/index.md)
- [Troubleshoot with IPsec logs](https://developers.cloudflare.com/cloudflare-wan/troubleshooting/ipsec-troubleshoot/index.md)
- [Troubleshoot routing and BGP](https://developers.cloudflare.com/cloudflare-wan/troubleshooting/routing-and-bgp/index.md)
- [Troubleshoot tunnel health](https://developers.cloudflare.com/cloudflare-wan/troubleshooting/tunnel-health/index.md)